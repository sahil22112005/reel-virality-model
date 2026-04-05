# 📱 Trending Reel on Instagram Modelling

This repository contains a mathematical simulation built with Python and Streamlit. It models the lifecycle of a trending Instagram Reel, predicting its virality using a continuous deterministic Growth-Decay mathematical model.

## 📌 Project Overview
In the modern digital era, understanding social media algorithms is crucial for content distribution. This project translates abstract algorithmic signals (sharing velocity and user fatigue) into a predictable time-series curve. 

**Use Cases:**
- 📈 Predicting the Peak Viral Day of a video.
- ⚙️ Calculating maximum potential views based on initial traction.
- 🚀 Optimizing content posting schedules and digital marketing ad spend.

## 📘 Mathematical Model
The simulation is driven by a modified Gamma-distribution formula:
`V(t) = A * t^k * e^(-λt)`

**Variables:**
- `V(t)` = Total daily views on day `t`.
- `A` = Initial Hook Factor (Algorithm's initial testing reach).
- `k` = Share Rate (The growth coefficient driven by users sharing the reel).
- `λ` = Decay Rate (The fatigue constant pulling views down as the trend dies).

**Peak Analysis:**
Using differential calculus, the exact peak of virality is derived as `t_peak = k / λ`.

## 🚀 How to Run the Application Locally
To run this dashboard on your own machine, follow these steps:

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
   cd your-repo-name
