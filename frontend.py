import streamlit as st
import pandas as pd
import json
import plotly.express as px
import plotly.graph_objects as go

# ✅ Load local files (relative paths)
df = pd.read_csv("amazon_reviews_selected.csv")

with open("amazon_reviews_summary_with_gpt.json", encoding="utf-8") as f:
    gpt_data = json.load(f)


df['reviews.date'] = pd.to_datetime(df['reviews.date'], errors='coerce')
df['name_clean'] = df['name_clean'].astype(str)

# Create year-month column for filtering
df['year_month'] = df['reviews.date'].dt.to_period('M').astype(str)

# === Sidebar ===
st.sidebar.title("🛍️ Product Selection")

product = st.sidebar.selectbox(
    "Select a product",
    sorted(df['name_clean'].dropna().unique())
)

# === Year-Month or All Time Filter ===
# Get available periods
available_periods = sorted(df[df['name_clean'] == product]['year_month'].dropna().unique())
period_options = ["All Time"] + available_periods

selected_periods = st.sidebar.multiselect(
    "Select period(s):",
    period_options,
    default="All Time"
)

# === Filter Data ===
if "All Time" in selected_periods or not selected_periods:
    filtered_df = df[df['name_clean'] == product]
else:
    filtered_df = df[
        (df['name_clean'] == product) &
        (df['year_month'].isin(selected_periods))
    ]

# === GPT Data ===
gpt = gpt_data.get(product, {
    "description": "No description available.",
    "pros": [],
    "cons": [],
    "insights": []
})

# === Custom CSS for artistic header ===
st.markdown(
    """
    <style>
    .title {
        font-size: 2.8rem;
        font-weight: 700;
        color: #4a90e2;
        text-align: center;
        margin-bottom: 0.2rem;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .subtitle {
        font-size: 1.3rem;
        font-weight: 400;
        color: #6c757d;
        text-align: center;
        margin-top: 0;
        margin-bottom: 2rem;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# === Artistic Header ===
st.markdown('<h1 class="title">📚✨ Product Reviews Explorer</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Deep insights powered by GPT & interactive visualizations</p>', unsafe_allow_html=True)

# === Category and Manufacturer ===
manufacturer = df[df['name_clean'] == product]['manufacturer'].dropna().unique()

st.markdown(f"**Manufacturer:** {manufacturer[0] if len(manufacturer) > 0 else 'N/A'}")

# === Collapsible GPT summaries ===
with st.expander("📄 Product Description"):
    st.write(gpt.get("description", "No description available."))

with st.expander("✅ Pros"):
    pros = gpt.get("pros", [])
    if pros:
        for p in pros:
            st.write(f"- {p}")
    else:
        st.write("No pros listed.")

with st.expander("❌ Cons"):
    cons = gpt.get("cons", [])
    if cons:
        for c in cons:
            st.write(f"- {c}")
    else:
        st.write("No cons listed.")

with st.expander("💡 Major Insights"):
    insights = gpt.get("insights", [])
    if insights:
        for i in insights:
            st.write(f"- {i}")
    else:
        st.write("No insights available.")

# === Recommendation Gauge ===
st.subheader("👍 Recommendation Rate")
if not filtered_df.empty and 'reviews.doRecommend' in filtered_df.columns:
    recommend_rate = filtered_df['reviews.doRecommend'].mean() * 100
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=recommend_rate,
        gauge={
            'axis': {'range': [None, 100]},
            'bar': {'color': "#4a90e2"},
            'steps': [
                {'range': [0, 50], 'color': "lightgray"},
                {'range': [50, 100], 'color': "lightgreen"}
            ],
            'threshold': {'line': {'color': "red", 'width': 4}, 'thickness': 0.75, 'value': 70}
        }
    ))
    fig.update_layout(title={'text': "Recommendation Rate (%)"})
    st.plotly_chart(fig, use_container_width=True)
else:
    st.write("No recommendation data available.")

# === Ratings Distribution ===
st.subheader("⭐ Rating Distribution")
fig_hist = px.histogram(
    filtered_df,
    x="reviews.rating",
    nbins=5,
    title="Rating Distribution",
    labels={'reviews.rating': 'Rating'}
)
st.plotly_chart(fig_hist, use_container_width=True)

# === Rating Over Time ===
st.subheader("📈 Average Rating Over Time")
if not filtered_df.empty:
    time_trend = (
        filtered_df.groupby(filtered_df['reviews.date'].dt.to_period('M'))
        .agg({'reviews.rating': 'mean'})
        .reset_index()
    )
    time_trend['reviews.date'] = time_trend['reviews.date'].dt.to_timestamp()

    fig_line = px.line(
        time_trend,
        x='reviews.date',
        y='reviews.rating',
        markers=True,
        title="Average Rating Over Time",
        labels={'reviews.date': 'Date', 'reviews.rating': 'Avg. Rating'}
    )
    st.plotly_chart(fig_line, use_container_width=True)
else:
    st.write("Not enough data for this period.")

# === Most Helpful Comments ===
st.subheader("💬 Most Helpful Reviews")
most_helpful = filtered_df.sort_values('reviews.numHelpful', ascending=False).head(3)

if not most_helpful.empty:
    for _, row in most_helpful.iterrows():
        st.markdown(f"**{row['reviews.title']}**")
        st.write(row['reviews.text'])
        st.write(f"👍 Helpful: {row['reviews.numHelpful']}")
        st.markdown("---")
else:
    st.write("No reviews available in this period.")

# === Interactive search inside reviews ===
search_term = st.text_input("🔍 Search reviews for keywords:")

if search_term:
    filtered_search = filtered_df[filtered_df['reviews.text'].str.contains(search_term, case=False, na=False)]
    st.write(f"Showing {len(filtered_search)} reviews matching '{search_term}':")

    for _, row in filtered_search.iterrows():
        review_text = row['reviews.text']
        highlighted = review_text.replace(search_term, f"**{search_term}**")
        st.markdown(f"**{row['reviews.title']}**")
        st.write(highlighted)
        st.write(f"👍 Helpful: {row['reviews.numHelpful']}")
        st.markdown("---")
