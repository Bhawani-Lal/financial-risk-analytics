import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import yfinance as yf
from datetime import datetime, timedelta

# ── Config ────────────────────────────────────────────────
st.set_page_config(
    page_title="Financial Risk Analytics",
    page_icon="📊",
    layout="wide"
)

DEFAULT_TICKERS = ["AAPL", "MSFT", "GOOGL", "JPM", "GS",
                   "AMZN", "TSLA", "META", "NVDA", "BAC"]

# ── Sidebar ───────────────────────────────────────────────
st.sidebar.title("⚙️ Controls")
tickers = st.sidebar.multiselect(
    "Select Tickers",
    DEFAULT_TICKERS,
    default=["AAPL", "MSFT", "JPM", "GS", "GOOGL"]
)
start_date = st.sidebar.date_input(
    "Start Date",
    datetime.today() - timedelta(days=365)
)
end_date = st.sidebar.date_input("End Date", datetime.today())
window = st.sidebar.slider("Volatility Window (days)", 10, 60, 30)

# ── Data Pipeline ─────────────────────────────────────────
@st.cache_data(ttl=300)
def fetch_data(tickers, start, end):
    raw = yf.download(tickers, start=start, end=end)["Close"]
    return raw.dropna()

# ── Risk Engine ───────────────────────────────────────────
def compute_returns(prices):
    return prices.pct_change().dropna()

def compute_volatility(returns, window):
    return returns.rolling(window).std() * (252 ** 0.5)

def compute_var(returns, confidence=0.95):
    return returns.quantile(1 - confidence)

def compute_correlation(returns):
    return returns.corr()

# ── Main App ──────────────────────────────────────────────
st.title("📊 Financial Risk Analytics Dashboard")
st.caption("Live equity data · Volatility · Correlation · Value at Risk")

if not tickers:
    st.warning("Select at least one ticker from the sidebar.")
    st.stop()

with st.spinner("Fetching live market data..."):
    prices = fetch_data(tickers, start_date, end_date)

if prices.empty:
    st.error("No data returned. Check tickers or date range.")
    st.stop()

returns = compute_returns(prices)
volatility = compute_volatility(returns, window)
var_95 = compute_var(returns)
correlation = compute_correlation(returns)

# ── Row 1: Price Performance + Volatility ─────────────────
col1, col2 = st.columns(2)

with col1:
    st.subheader("📈 Price Performance")
    normalised = prices / prices.iloc[0] * 100
    fig = px.line(normalised, title="Normalised Price (Base 100)")
    fig.update_layout(
        legend_title="Ticker",
        hovermode="x unified",
        plot_bgcolor="rgba(0,0,0,0)"
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    st.subheader("🌊 Rolling Volatility")
    fig2 = px.line(
        volatility,
        title=f"{window}-Day Annualised Volatility"
    )
    fig2.update_layout(
        legend_title="Ticker",
        hovermode="x unified",
        plot_bgcolor="rgba(0,0,0,0)"
    )
    st.plotly_chart(fig2, use_container_width=True)

# ── Row 2: Correlation + VaR ──────────────────────────────
col3, col4 = st.columns(2)

with col3:
    st.subheader("🔥 Correlation Heatmap")
    fig3 = go.Figure(data=go.Heatmap(
        z=correlation.values,
        x=correlation.columns,
        y=correlation.index,
        colorscale="RdBu",
        zmid=0,
        text=correlation.round(2).values,
        texttemplate="%{text}",
        showscale=True
    ))
    fig3.update_layout(title="Asset Correlation Matrix")
    st.plotly_chart(fig3, use_container_width=True)

with col4:
    st.subheader("⚠️ Value at Risk (95% Confidence)")
    var_df = pd.DataFrame({
        "Ticker": var_95.index,
        "VaR (95%)": (var_95.values * 100).round(3)
    }).sort_values("VaR (95%)")

    fig4 = px.bar(
        var_df,
        x="Ticker",
        y="VaR (95%)",
        title="Worst Expected Daily Loss (%)",
        color="VaR (95%)",
        color_continuous_scale="Reds_r"
    )
    fig4.update_layout(plot_bgcolor="rgba(0,0,0,0)")
    st.plotly_chart(fig4, use_container_width=True)

# ── Summary Metrics ───────────────────────────────────────
st.divider()
st.subheader("📋 Risk Summary")
summary = pd.DataFrame({
    "Latest Price": prices.iloc[-1].round(2),
    "Total Return (%)": ((prices.iloc[-1] / prices.iloc[0] - 1) * 100).round(2),
    "Avg Volatility (%)": (volatility.mean() * 100).round(2),
    "VaR 95% (%)": (var_95 * 100).round(3)
})
st.dataframe(summary.style.highlight_max(
    subset=["Avg Volatility (%)"],
    color="#ffcccc"
), use_container_width=True)

st.caption("Data sourced from Yahoo Finance via yfinance · Refreshes every 5 minutes")