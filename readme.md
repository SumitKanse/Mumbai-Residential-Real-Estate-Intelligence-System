# 🌇️ Mumbai Real Estate Rental Intelligence System

This is a data analysis project focused on **Mumbai’s real estate rental/rooms market**. It includes modules for price insights, advanced analytics, and a dataset-based assistant — all tied together with a Streamlit frontend.

---

## 📌 Problem Statement

The Mumbai rental market is vast and highly dynamic. People often struggle to:
- Understand room/rental availability by locality
- Explore meaningful trends (price vs area/BHK/furnishing/age)
- Quickly summarize listing descriptions and common features

---

## ✅ Proposed Solution

This project provides a rental intelligence dashboard that:
- Analyzes locality-wise room/rental availability
- Visualizes key market patterns and trends
- Answers user queries using the local dataset (with optional external API support)

All these components are unified in a clean, interactive Streamlit dashboard.

---

## 🧠 Project Workflow

### 📂 Dataset Used

We used `mumbaipropdataset.csv`, a structured dataset containing:
- Property details like `AREA`, `BHK`, `FACING`, `AGE`, `PRICE`, `DESCRIPTION`, `LAT`, `LONG`, etc.
- Listings from across **Mumbai residential sectors**

---

## 💪 Modules Description

### 1️⃣ Price Prediction / Price Insights (ML)
- Uses a machine learning pipeline trained on Mumbai listing data
- Input: area, locality, BHK, furnishing, floor category, etc.
- Output: predicted price estimate

### 2️⃣ Analytics (Data Visualization)
- Built with **Plotly** inside **Streamlit**
-- Shows:
  - Scatter plots: Area vs Price
  - Sunburst: City → Locality → BHK
  - Radial charts: Price by Facing
  - Line charts: Price vs Age
  - Word cloud from descriptions
  - Pie charts: BHK filtered by locality

### 3️⃣ Assistant (Dataset-Powered)
- Answers Q&A using the local dataset (availability, pricing patterns, summaries)
- Optional: can be connected to an external API if you provide a URL in the sidebar

---

## ⚙️ Implementation Steps

### ✅ 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### ✅ 2. (Optional) Connect an external chatbot API

- Open the app and paste your API URL in the **RealtEase sidebar** (optional).

---

## ▶️ Running the App Locally(For Windows)

1. **Create your environment** (e.g., `dslab`) and install dependencies:

```bash
pip install virtualenv
```

```bash
virtualenv dslab
```

```bash
cd dslab/Scripts && activate
```

2. **Install the required packages:**

```bash
pip install -r requirements.txt
```

3. **Launch the Streamlit app:**

```bash
streamlit run Real_Estate_Project.py
```

🎉 That's it! Your Mumbai Real Estate Intelligence App is now live.

---

## 🛠️ Tech Stack

| Component     | Tools Used                                      |
|---------------|-------------------------------------------------|
| Language      | Python                                          |
| Visualization | Plotly, Matplotlib, Seaborn                     |
| Web App       | Streamlit                                       |
| ML Model      | Scikit-learn (Random Forest Regressor)          |
| NLP           | TF-IDF, NLTK                                    |
| LLM API       | Colab + custom Python Flask/NLP logic           |
| Hosting       | Local + Colab API for GPU-based chatbot         |

---

## 🚧 Future Scope

- Replace RF with **XGBoost or CatBoost**
- Improve chatbot with **LLM fine-tuning** or **LangChain**
- Deploy chatbot via WhatsApp/Telegram

---

## 👤 Author

- **Sumit Kanse**

---

## 📜 License

This project is for academic and research purposes only.

---

