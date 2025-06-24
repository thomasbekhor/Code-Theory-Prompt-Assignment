# 🛍️ AI-Powered Product Review Explorer  
Code and Theory Prompt Assignment_

A creative AI-powered experience that turns chaotic Amazon product reviews into narrative, insight, and interactivity.

---

## 👋 About This Project

This project started with a simple question:  
**How can messy databases — filled with noise, contradictions, and scattered opinions — be transformed into something useful, insightful, and maybe even beautiful?**

The result is an Streamlit app that surfaces product stories, user sentiments, and data-driven insights in a human-centered way using AI to analyze the users reviews.

---

## 🚀 Try It Live

> 🌐 [Launch the live app](https://code-theory-prompt-assignment.streamlit.app/)

Explore products like the Kindle Oasis, Fire HD, or Echo, and let AI reveal what real people are saying about them.

---

## 🧠 My Process

### 1. 🧹 Data Exploration & Brainstorming

I began by cleaning and exploring a Kaggle dataset of Amazon reviews using `pandas`. After analyzing the content, I selected key variables like:
- `name`
- `brand`
- `categories`
- `manufacturer`
- `reviews rating`
- `revies description`
- `review date`
- `recommendation count`

This informed early design questions:
- What matters to users when choosing a product?
- How can I help designers or marketers understand concise perceptions of the products based on the reviews?
- How can the interface feel alive — not just analytical?

These ideas shaped the interface design:  
**Product selection → Product description and overview → GPT analysis (pros, cons and insights)

To simplify the user experience and reduce redundancy, I used GPT to analyze and group technically similar product variants. This helped consolidate scattered listings into 5 unified products:

- Echo (Black)
- Fire HD 8 Tablet 16GB
- Fire Tablet 7
- Kindle Oasis
- Kindle Paperwhite

This clustering allowed for cleaner insights and a smoother interface, especially when multiple SKUs were nearly identical in user perception but had different listings.
---

### 2. 🤖 GPT-Powered Insight Extraction

Next, I experimented with OpenAI’s GPT-4o API to extract:
- 🔎 Product **descriptions**
- ✅ Lists of **pros**
- ❌ Common **cons**
- 💡 Hidden **usage insights**

After iterating and refining the prompt, I processed each product through the API, which directly saved the outputs to JSON.

---

### 3. 🖥️ Interface Development with Streamlit

The frontend was built in Streamlit with an emphasis on speed, exploration, and creativity. Features include:
- 📅 Time-based filters by **year and multiple months**
- 📊 Rating distribution with **Plotly**
- 💬 Surface-level **most helpful reviews**

Finally, I deployed the app to Streamlit Cloud for live access.

---

## 🧩 Key Features

| Feature | Description |
|--------|-------------|
| 🧾 **Summarization** | GPT-generated product description, pros, cons, and usage insights |
| 📅 **Time-Based Filtering** | Interactive filters by year and multiple months in the side bar |
| 📊 **Rating Distribution** | Histogram of review scores over selected periods |
| 📈 **Sentiment Over Time** | Line graph of average rating by month |
| 📊 **Most Helpful Comments** | Most helpful comments of each product from the database  |

---

## 🛠️ Tech Stack

- 🧰 **Frontend:** Streamlit  
- 🧠 **AI Engine:** OpenAI GPT-4o API  
- 📊 **Visualization:** Plotly  
- 📁 **Data:** Kaggle Amazon Reviews Dataset and analyzis using Pandas. 

---

## 📁 Project Files

- `frontend.py` — Streamlit app  
- `amazon_reviews_selected.csv` — Raw data  
- `amazon_reviews_summary_with_gpt.json` — GPT output  
- `requirements.txt` — Dependencies  
- `README.md` — Project overview (this file)
- `Images` — Product images

---

## 🙋‍♂️ About Me

Built by **Thomas Bekhor** as a creative prototype and proof-of-concept submission for the Junior Creative Technologist role at Code and Theory.

> [🔗 LinkedIn](https://www.linkedin.com/in/thomasbekhor/)  

---




