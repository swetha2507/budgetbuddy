# 💸 BudgetBuddy

**An AI-powered spending insight tool — not just what you spent, but why and how to fix it.**

BudgetBuddy helps users analyze their personal expenses through smart visualizations and personalized insights. Upload your CSV file, and let the app break down your spending patterns, highlight behavioral trends, and offer actionable advice — all in one clean dashboard.

---

## 🔍 Features

- 📁 **CSV Upload** – Drop in your expense data (`Date, Category, Amount, Description`)
- 📊 **Interactive Visualizations** – View your spending by category, date, and more
- 🧠 **Smart Insight Generator** – Get rule-based suggestions like:
  - "You spent 40% more on food this month — try meal prepping."
  - "Weekend spending spikes detected."
- 🤖 **AI Q&A Assistant** – Ask questions like:
  - "Why is my transport spending high?"
  - "What's my biggest unnecessary expense?"

---

## 🛠 Tech Stack

- **Frontend**: Streamlit  
- **Backend**: Python (Pandas, NumPy)  
- **Visualization**: Plotly, Matplotlib  
- **AI/NLP**: Rule-based logic + optional OpenAI GPT  
- **Deployment**: Streamlit Cloud / GitHub  

---

## 🚀 Getting Started

### 1. Clone this repository
```bash
git clone https://github.com/swetha2507/budgetbuddy.git
cd budgetbuddy
```

### 2. Create & activate a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the app
```bash
streamlit run app.py
```

---

### 🔐 Setting up OpenAI API Key (For AI Q&A Assistant)
To enable the AI assistant, set your OpenAI API key as an environment variable before running the app:

```bash
export OPENAI_API_KEY="sk-xxxxxxxxxxxxxxxxxxxx"
```

⚠️ Your API key is not stored in the app. It stays safe in your local environment. 