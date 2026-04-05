import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# --- Simulation Function ---
def simulate_virality(initial_hook, share_rate, decay_rate, days):
    t = np.linspace(0.1, days, 200)
    views = initial_hook * (t**share_rate) * np.exp(-decay_rate * t)
    return t, views

# --- UI Layout ---
st.set_page_config(page_title="Instagram Reel Virality Model", layout="centered")

st.title("📱 Trending Reel on Instagram Modelling")
st.write("Model: Growth-Decay & Peak Analysis")

# --- Sidebar Inputs ---
st.sidebar.header("⚙️ Input Parameters")
initial_hook = st.sidebar.slider("Initial Hook (A)", 100, 5000, 1000, step=100)
share_rate = st.sidebar.slider("Share Rate / Growth (k)", 0.5, 8.0, 4.9, step=0.1)
decay_rate = st.sidebar.slider("Decay Rate / Fatigue (λ)", 0.1, 3.0, 0.6, step=0.1)
days = st.sidebar.slider("Simulation Days", 5, 30, 18, step=1)

# --- Project Overview ---
st.markdown("""
## 📌 Project Overview
This model predicts **Instagram Reel Virality** over time using:
- 📈 **Polynomial Growth** (Driven by user sharing and algorithm push)
- 📉 **Exponential Decay** (Driven by trend fatigue and audience saturation)
""")

# --- Run Simulation ---
t_data, views_data = simulate_virality(initial_hook, share_rate, decay_rate, days)

peak_day = share_rate / decay_rate
max_views = initial_hook * (peak_day**share_rate) * np.exp(-decay_rate * peak_day)

# --- Graph ---
st.subheader("📈 Viral Growth & Decay Curve")
fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(t_data, views_data, color="#E1306C", linewidth=2.5, label="Daily Views")
ax.axvline(x=peak_day, color='black', linestyle='--', label=f"Peak Day ({peak_day:.1f})")
ax.fill_between(t_data, views_data, color="#E1306C", alpha=0.2)
ax.set_xlabel("Days Since Upload")
ax.set_ylabel("Daily Views")
ax.legend()
st.pyplot(fig)

# --- Insights & Metrics ---
st.subheader("🔍 Key Insights")
col1, col2 = st.columns(2)
with col1:
    st.metric("🔥 Peak Viral Day", f"Day {peak_day:.1f}")
with col2:
    st.metric("👀 Max Views on Peak", f"{int(max_views):,}")

# --- Interpretation Logic ---
if share_rate < decay_rate:
    status = "Trend Failure (Shadowbanned)"
    color = "🚨"
elif decay_rate < 0.4:
    status = "Evergreen Content (Long Tail)"
    color = "✅"
else:
    status = "Standard Viral Hit"
    color = "🔥"

st.success(f"""
💡 **Interpretation:**
* **k < λ** → Content decays faster than it grows.
* **Low λ (< 0.4)** → Strong retention.
* **High k & High λ** → Massive immediate spike, rapid death.

Current Trend Status: **{color} {status}**
""")

# --- Mathematical Model ---
st.markdown("---")
st.subheader("📘 Mathematical Model")
st.latex(r"V(t) = A \cdot t^k \cdot e^{-\lambda t}")
st.latex(r"t_{peak} = \frac{k}{\lambda}")

# --- Conclusion ---
st.markdown("---")
st.subheader("📌 Conclusion")

st.write(f"""
🔹 **Initial Push:** The algorithm started by showing the reel to **{initial_hook}** users.  

🔹 **Virality Engine:** The share rate (k={share_rate}) drove the content to peak on **Day {peak_day:.1f}**.  

🔹 **Maximum Reach:** At its peak, the reel achieved **{int(max_views):,}** views in a single day.  

🔹 **Trend Lifespan:** Driven by a decay rate of λ={decay_rate}, the overall trend status is categorized as a **{status}**.  

👉 **Takeaway:** This model demonstrates that while the initial algorithmic hook is helpful, sustained virality depends entirely on maximizing the ratio of user sharing (k) against audience fatigue (λ).
""")
