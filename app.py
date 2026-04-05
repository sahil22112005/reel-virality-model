import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import numpy as np

# --- 1. Page Setup ---
st.set_page_config(page_title="Reel Virality Simulator", layout="wide")

# --- 2. Sidebar (User Inputs) ---
st.sidebar.header("⚙️ Simulation Controls")

A = st.sidebar.slider("Initial Hook (A)", min_value=100, max_value=5000, value=1000, step=100)
k = st.sidebar.slider("Share Rate / Growth (k)", min_value=0.5, max_value=8.0, value=3.5, step=0.1)
lam = st.sidebar.slider("Decay Rate / Fatigue (λ)", min_value=0.1, max_value=3.0, value=0.8, step=0.1)
days = st.sidebar.slider("Days to Simulate", min_value=5, max_value=30, value=15, step=1)

# --- 3. Mathematical Engine ---
def calculate_virality(hook, share_rate, decay_rate, total_days):
    # Create an array of time points from 0.1 to the chosen number of days
    t = np.linspace(0.1, total_days, 200)
    
    # Mathematical Formula: V(t) = A * t^k * e^(-λt)
    views = hook * (t**share_rate) * np.exp(-decay_rate * t)
    
    return pd.DataFrame({"Day": t, "Daily Views": views})

# Run the function to generate data
df = calculate_virality(A, k, lam, days)

# --- 4. Dashboard Layout ---
chart_col, analysis_col = st.columns([2.5, 1])

with chart_col:
    st.subheader("📈 Viral Growth & Decay Curve")
    
    # Draw the Plotly chart
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=df['Day'], y=df['Daily Views'], mode='lines', 
                             name='Daily Views', line=dict(width=4, color='#E1306C'))) # Instagram Pink color
    
    fig.update_layout(xaxis_title="Days Since Upload", yaxis_title="Daily Views", height=500)
    st.plotly_chart(fig, use_container_width=True)

with analysis_col:
    st.subheader("📉 Peak Analysis")
    
    # Calculate exact peak day and max views
    peak_day = k / lam
    max_views = A * (peak_day**k) * np.exp(-lam * peak_day)
    
    # Display the metrics
    st.metric("🔥 Peak Viral Day", f"Day {peak_day:.1f}")
    st.metric("👀 Max Views on Peak Day", f"{int(max_views):,}")
    
    st.markdown("---")
    st.subheader("💡 Insights")
    
    # Dynamic logic for the insights text
    if k < lam:
        st.error("🚨 Content is decaying faster than it is being shared. The Reel will not go viral.")
    elif lam < 0.5:
        st.success("✅ Excellent retention! This is 'Evergreen' content that will get views for weeks.")
    else:
        st.info("📌 Standard viral trend detected. Prepare follow-up content for the peak day.")
