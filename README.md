# 📊 Financial Risk Analytics Dashboard

> **Real-time financial risk intelligence** — live equity data, volatility analysis, correlation heatmaps, and Value at Risk calculations. Built for financial analysts who need insight, not just charts.

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-Deployed-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-Interactive-3F4F75?style=flat&logo=plotly&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data_Pipeline-150458?style=flat&logo=pandas&logoColor=white)
![yfinance](https://img.shields.io/badge/yfinance-Live_Data-6929C4?style=flat)
![License](https://img.shields.io/badge/License-MIT-green?style=flat)

🔴 **[Live Demo →](https://your-app-link.streamlit.app)** &nbsp;|&nbsp; 📁 **[View Code →](./app.py)**

---

## 🎯 The Problem

Financial analysts juggle dozens of assets, risk reports, and market signals daily. Existing tools are either too complex (Bloomberg terminals), too expensive, or too generic to give a fast, clear picture of portfolio risk exposure.

This dashboard gives you **one screen, live data, and actionable risk metrics** — in seconds, not hours.

---

## ✨ What It Does

```
Upload nothing. Configure nothing. Open the dashboard → risk intelligence, instantly.
```

| Module | What You Get |
|---|---|
| 📈 **Live Price Tracker** | Real-time prices for 10 equities via yfinance API |
| 🌊 **Volatility Analysis** | 30-day rolling volatility — see which assets are moving |
| 🔥 **Correlation Heatmap** | Cross-asset correlation matrix — spot diversification gaps |
| ⚠️ **Value at Risk (VaR)** | 95% confidence VaR — worst expected daily loss per asset |
| 🎛️ **Dynamic Filtering** | Filter by ticker, date range, and time window in real time |

---

## 📸 Dashboard Preview

> *Screenshot coming — deploy link above for live view*

```
┌─────────────────────────────────────────────────────────────┐
│  📊 Financial Risk Analytics Dashboard                       │
│  ─────────────────────────────────────────────────────────  │
│                                                             │
│  Tickers: [AAPL] [MSFT] [GOOGL] [JPM] [GS] ...            │
│  Date Range: [2024-01-01] → [2025-01-01]                   │
│                                                             │
│  ┌──────────────────────┐  ┌──────────────────────────┐   │
│  │   Price Performance  │  │   30-Day Volatility      │   │
│  │   [Line Chart]       │  │   [Area Chart]           │   │
│  └──────────────────────┘  └──────────────────────────┘   │
│                                                             │
│  ┌──────────────────────┐  ┌──────────────────────────┐   │
│  │  Correlation Heatmap │  │  Value at Risk (95%)     │   │
│  │  [Heatmap Grid]      │  │  [Bar Chart per Asset]   │   │
│  └──────────────────────┘  └──────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
```

---

## 🏗️ Architecture

```
yfinance API (Live Market Data)
        │
        ▼
┌───────────────────┐
│   Data Pipeline   │  ← Pandas: fetch, clean, resample, validate
│   (pipeline.py)   │
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│  Risk Engine      │  ← Rolling volatility, Pearson correlation,
│  (risk.py)        │    Historical VaR at 95% confidence
└────────┬──────────┘
         │
         ▼
┌───────────────────┐
│  Streamlit App    │  ← Interactive UI, Plotly charts,
│  (app.py)         │    dynamic sidebar filters
└────────┬──────────┘
         │
         ▼
  Streamlit Cloud
  (public live URL)
```

---

## 📐 Risk Calculations

### Rolling Volatility
```python
# 30-day annualised rolling volatility
returns = prices.pct_change().dropna()
volatility = returns.rolling(window=30).std() * (252 ** 0.5)
```

### Value at Risk (Historical, 95% Confidence)
```python
# Worst expected daily loss at 95% confidence
VaR_95 = returns.quantile(0.05)
```

### Correlation Matrix
```python
# Pearson correlation across all assets
correlation = returns.corr()
```

---

## 🚀 Run Locally

### 1. Clone the repo
```bash
git clone https://github.com/Bhawani-Lal/financial-risk-analytics.git
cd financial-risk-analytics
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the dashboard
```bash
streamlit run app.py
```

Navigate to `http://localhost:8501` — live data loads automatically, no API key needed.

---

## 📁 Project Structure

```
financial-risk-analytics/
├── app.py                  # Streamlit app — UI, layout, sidebar filters
├── pipeline.py             # Data fetching & cleaning via yfinance + Pandas
├── risk.py                 # Volatility, VaR, correlation calculations
├── config.py               # Default tickers, date ranges, window sizes
├── requirements.txt
└── README.md
```

---

## 📦 Requirements

```txt
streamlit==1.35.0
pandas==2.2.0
plotly==5.22.0
yfinance==0.2.40
numpy==1.26.4
```

---

## 💡 Key Design Decisions

**Why Historical VaR over Parametric?**
Historical VaR makes no assumptions about return distribution — it uses actual past returns, which captures fat tails and non-normal behaviour that parametric methods miss. More honest for real financial data.

**Why yfinance?**
Free, no API key required, covers 10,000+ global equities with daily/hourly/minute granularity. Production systems would use Bloomberg or Refinitiv — but for demonstrating the analytics pipeline, yfinance is the right pragmatic choice.

**Why Streamlit over Dash?**
Streamlit's reactive model means zero boilerplate for interactivity — a sidebar filter automatically reruns the full pipeline. For a single-analyst tool, that's the right tradeoff. Dash would be preferable for multi-user production apps.

---

## 🎯 Relevance to Financial Services

This project directly demonstrates:
- **Quantitative risk thinking** — VaR, volatility, and correlation are core concepts in any financial risk team
- **Live data engineering** — API ingestion, cleaning, and transformation pipeline
- **Analyst-grade visualisation** — communicating complex risk metrics clearly to decision-makers
- **Production deployment** — live on Streamlit Cloud, accessible without setup

Aligned with quantitative analytics workflows at firms like **JPMorgan Chase**, **Goldman Sachs**, and **McKinsey's Financial Services practice**.

---

## 🔮 Roadmap

- [ ] Monte Carlo VaR simulation
- [ ] Portfolio-level combined risk metrics
- [ ] Sector breakdown and industry correlation analysis
- [ ] Alert system — flag assets breaching volatility thresholds
- [ ] Export report as PDF (one-click)
- [ ] Add options Greeks (Delta, Gamma) for derivatives exposure

---

## 👨‍💻 Author

**Bhawani Lal**
MSc Advanced Computer Science with Data Science — University of Strathclyde, Glasgow

[![LinkedIn](https://img.shields.io/badge/LinkedIn-bhawani--lal-0A66C2?style=flat&logo=linkedin)](https://linkedin.com/in/bhawani-lal)
[![GitHub](https://img.shields.io/badge/GitHub-Bhawani--Lal-181717?style=flat&logo=github)](https://github.com/Bhawani-Lal)
[![Portfolio](https://img.shields.io/badge/Portfolio-Live-D97706?style=flat)](https://bhawani-portfolio.vercel.app)

---

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

> *Built as part of a portfolio targeting quantitative and software engineering roles in financial services.*
