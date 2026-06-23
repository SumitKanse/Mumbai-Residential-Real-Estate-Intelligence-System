# Mumbai-Residential-Real-Estate-Intelligence-System
A data science project that analyzes Mumbai real estate price trends using Python. Data is collected via web scraping with BeautifulSoup and processed using Pandas and NumPy. Visualization and model training are performed using Matplotlib, Seaborn, and PyTorch.

The Mumbai Residential Real Estate Intelligence System is a data-driven project designed to analyze and understand Mumbai’s residential property market. It combines machine learning, data visualization, and a chatbot interface to provide property price predictions, market insights, and quick answers to user queries through an interactive Streamlit dashboard.

---

## Problem Statement

Mumbai’s housing market is large and constantly changing, making it difficult for buyers and investors to evaluate property prices and trends. Users often face challenges such as:

* Estimating the correct property value
* Understanding trends based on locality, property size, or age
* Getting quick answers related to property listings

---

## Proposed Solution

This project introduces an intelligent real estate analysis system that:

* Predicts residential property prices using machine learning
* Provides interactive analytics and visualizations of market trends
* Includes a chatbot assistant that answers property-related questions using dataset knowledge

All modules are integrated into a user-friendly **Streamlit web application**.

---

## Dataset

The system uses the **mumbaipropdataset.csv** dataset which contains residential property information across Mumbai.

Key attributes include:

* Area of the property
* Number of BHK rooms
* Property facing direction
* Property age
* Price
* Description text
* Latitude and longitude coordinates

---

## Project Modules

### 1. Property Price Prediction

A machine learning model was developed to estimate property prices based on important features such as area, location, BHK, and age.

Model used:

* **Random Forest Regressor (500 estimators)**

Performance:

* Achieved approximately **91% prediction accuracy**

Input:

* Property features (area, locality, BHK, age, etc.)

Output:

* Estimated property price

---

### 2. Data Analytics and Visualization

Interactive visualizations were created using **Plotly within Streamlit** to explore patterns in the dataset.

The analytics dashboard includes:

* Scatter plots showing **area vs price relationship**
* Sunburst charts displaying **city → locality → BHK hierarchy**
* Radial charts representing **price distribution by property facing**
* Line graphs illustrating **price trends based on property age**
* Word clouds generated from property descriptions
* Pie charts showing **BHK distribution by locality**

These visualizations help users understand the real estate market more clearly.

---

### 3. AI Chatbot Assistant

A lightweight chatbot system was implemented to answer user questions about Mumbai properties.

Key capabilities:

* Responds to real estate related questions
* Retrieves insights directly from the dataset
* Handles both text-based queries and requests for visual insights

The chatbot is deployed on **Google Colab using GPU support** and connected to the Streamlit frontend via an API.

---

## Implementation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo.git
cd your-repo
```

### 2. Start the Chatbot (Google Colab)

Open the notebook **RealEstateChatbot.ipynb** on Google Colab and run all cells using a GPU runtime.
After execution, an API link will be generated.

Copy the generated API URL.

---

### 3. Connect the Chatbot with the Frontend

Open the file:

```
pages/RealtEase.py
```

Update the API endpoint:

```python
url = "https://your-colab-api.ngrok-free.app"
```

Note: The chatbot remains active while the Colab session is running.

---

## Running the Application Locally (Windows)

### Step 1 – Create a Virtual Environment

```bash
pip install virtualenv
virtualenv dslab
```

Activate the environment:

```bash
cd dslab/Scripts
activate
```

---

### Step 2 – Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Step 3 – Run the Streamlit Application

```bash
streamlit run Real_Estate_Project.py
```

After running the command, the web dashboard will launch locally in your browser.

---

## Technology Stack

| Component            | Tools Used                             |
| -------------------- | -------------------------------------- |
| Programming Language | Python                                 |
| Data Visualization   | Plotly, Matplotlib, Seaborn            |
| Web Interface        | Streamlit                              |
| Machine Learning     | Scikit-learn (Random Forest Regressor) |
| NLP Processing       | TF-IDF, NLTK                           |
| Chatbot Hosting      | Google Colab + API                     |
| Deployment           | Local Streamlit App                    |

---

## Future Enhancements

Possible improvements for the project include:

* Using advanced models like **XGBoost or CatBoost** for better prediction accuracy
* Enhancing the chatbot using **LLM frameworks such as LangChain**
* Integrating messaging platforms like **WhatsApp or Telegram** for chatbot access
* Deploying the full system on a cloud platform for public use

---

## Acknowledgements

Guide: **Ms. Sonal Balpande**
Institute: **A.P. Shah Institute of Technology, Mumbai**

This project was developed as part of the **Data Science Lab mini project for TE IT (2024–2025).**

---

## License

This project is intended for academic and research purposes only.
