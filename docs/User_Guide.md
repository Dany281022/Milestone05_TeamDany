# Weekly Sales Forecaster
## User Guide

**Version:** 3.0
**Last Updated:** April 6, 2026
**Team:** Team Dany | Dany Deugoue (A00316024)
**Course:** AIE1014 — AI Applied Project | Cambrian College

---

## Table of Contents

1. Introduction
2. Getting Started
3. Using the Application
4. Understanding Your Results
5. AI Sales Advisor
6. Troubleshooting
7. Frequently Asked Questions
8. Getting Help

---

## 1. Introduction

### 1.1 About This Application

The **Weekly Sales Forecaster** is a machine learning-powered prediction
tool that helps Retail Business Managers predict next week's store sales
instantly. By entering 13 weeks of historical sales figures, you receive
a dollar forecast with a ±10% confidence interval, a colour-coded demand
signal, and AI-powered business recommendations to support your Monday
morning inventory and staffing decisions.

**Stakeholder:** Retail Business Manager
**Live Application:**
- 🔗 https://weekly-sales-forecaster-teamdany.streamlit.app/
- 🔗 https://weekly-sales-forecaster-team-dany-aie1014.onrender.com

### 1.2 Who Should Use This Guide

- Retail Business Managers forecasting weekly store sales
- Store managers planning inventory and staffing
- Anyone evaluating the application

### 1.3 What You Will Need

- A computer, tablet, or smartphone
- An internet connection
- A modern web browser (Chrome, Firefox, Safari, or Edge)
- Your store's weekly sales figures for the last 1–52 weeks

### 1.4 Quick Start

1. Go to: https://weekly-sales-forecaster-teamdany.streamlit.app/
2. Enter your store's recent weekly sales figures
3. Click **"🔮 Get Prediction"**
4. Read your forecast and demand signal
5. Click **"💬 AI Advisor"** for business recommendations

---

## 2. Getting Started

### 2.1 Accessing the Application

**Step 1:** Open Chrome (recommended)
**Step 2:** Go to https://weekly-sales-forecaster-teamdany.streamlit.app/
**Step 3:** Wait 10–30 seconds for the app to load

> **Tip:** Bookmark the URL for quick access every Monday morning.

> **Note:** First visit after inactivity may take 30–60 seconds
> as the server "wakes up." This is normal on the free hosting plan.

### 2.2 Browser Compatibility

| Browser | Supported | Notes |
|---------|-----------|-------|
| Google Chrome | ✅ Yes | Recommended |
| Mozilla Firefox | ✅ Yes | Fully supported |
| Safari | ✅ Yes | Fully supported |
| Microsoft Edge | ✅ Yes | Fully supported |
| Internet Explorer | ❌ No | Use a modern browser |

### 2.3 Mobile Access

The app works on smartphones and tablets.
- **Portrait** orientation for data entry
- **Landscape** orientation for charts and results
- Stable internet connection recommended

---

## 3. Using the Application

### 3.1 Application Overview

| Tab | Purpose |
|-----|---------|
| 🔮 Prediction | Enter sales data, get your weekly forecast |
| 📊 Dashboard | Model performance + prediction history charts |
| 📋 History | All predictions this session + CSV download |
| 💬 AI Advisor | AI-powered business recommendations |

### 3.2 Step-by-Step Instructions

#### Step 1 — Read the Welcome Message
A blue info box at the top guides you. All values are in **US dollars ($)**
for **one store only**.

#### Step 2 — Enter Your Sales History

| Field | What to Enter | Example |
|-------|--------------|---------|
| Last week's sales ($) | Total sales last week | $1,500,000 |
| Sales 2 weeks ago ($) | Total sales 2 weeks ago | $1,480,000 |
| Sales 4 weeks ago ($) | Total sales 4 weeks ago | $1,450,000 |
| Sales 8 weeks ago ($) | Total sales 8 weeks ago | $1,430,000 |
| Sales 12 weeks ago ($) | Total sales ~3 months ago | $1,400,000 |
| Sales 26 weeks ago ($) | Total sales ~6 months ago | $1,390,000 |
| Sales 1 year ago ($) | Total sales 1 year ago | $1,380,000 |

> ⚠️ **Important:** Enter values for **one store only**.
> Typical range: **$500,000 — $3,000,000 per week.**

#### Step 3 — Enter Moving Averages & Variability

| Field | What to Enter | How to Calculate |
|-------|--------------|-----------------|
| 4-week average sales ($) | Average of last 4 weeks | (W1+W2+W3+W4) ÷ 4 |
| 12-week average sales ($) | Average of last 12 weeks | Sum ÷ 12 |
| Sales variability ($) | Week-to-week variation | ~2–5% of your weekly average |

> **Tip:** For a $1,500,000/week store, enter $25,000–$75,000
> for sales variability if you are unsure of the exact figure.

#### Step 4 — Confirm Date (Auto-filled)
Week, Month, and Year are set to today automatically.
Adjust only if forecasting a different date.

#### Step 5 — Click Get Prediction
Click **"🔮 Get Prediction"**. Results appear in under 2 seconds.

#### Step 6 — Make Another Prediction
Change your input values and click the button again.
Previous results are saved in the **📋 History** tab.

---

## 4. Understanding Your Results

### 4.1 Demand Signal

| Signal | Meaning | Recommended Action |
|--------|---------|-------------------|
| 🟢 Stable | Within ±5% of last week | Maintain current inventory and staffing |
| 🟡 Higher demand | More than 5% above last week | Increase inventory; add staffing shifts |
| 🔵 Lower demand | More than 5% below last week | Reduce perishable orders; review staffing |

### 4.2 Prediction Interval

The ±10% interval shows the realistic sales range.

**Example:**
Forecast:            $1,420,688
Prediction Interval: $1,278,619 — $1,562,757
Actual sales will likely fall within this range.

### 4.3 Result Metrics

| Metric | Description |
|--------|-------------|
| Forecast | Predicted next-week sales |
| Week | Week of year being predicted |
| % vs Last Week | Change compared to last week |
| Response Time | How fast the model answered |

### 4.4 Model Accuracy

| Metric | Value | Plain English |
|--------|-------|---------------|
| R² Score | 0.9812 | Explains 98.1% of sales patterns |
| RMSE | $73,473 | Average prediction error per store |
| MAE | $47,281 | Typical prediction error per store |

> For a $1.5M/week store, the average error is approximately 5%.

### 4.5 Limitations

- Predictions are estimates based on historical patterns
- Unusual events (holidays, promotions, weather) may not be captured
- Model trained on Walmart data — most reliable for similar retail formats
- Always apply professional judgment alongside the forecast

---

## 5. AI Sales Advisor

### 5.1 Explain My Last Prediction
After a prediction, click **"🤖 Generate AI Business Analysis"** to receive:
- Plain-English explanation of what the forecast means
- Why sales may be trending this way
- Specific inventory recommendation
- Specific staffing recommendation
- Key risk to watch for

### 5.2 Ask the AI Anything
Type any retail question. Examples:
- *"What does a 15% sales increase mean for my inventory?"*
- *"How should I adjust staffing for a slower week?"*

### 5.3 Quick Recommendation Buttons

| Button | What You Get |
|--------|-------------|
| 📦 Inventory Advice | 3 specific inventory actions |
| 👥 Staffing Advice | 3 specific staffing adjustments |
| ⚠️ Risk Assessment | Top 3 risks for next week |

> **Note:** AI Advisor requires OpenAI API access.
> Core prediction always works regardless.

---

## 6. Troubleshooting

### 6.1 The App Won't Load

| Symptom | Solution |
|---------|---------|
| Blank page | Check internet; press Ctrl+R to refresh |
| Loading 60+ seconds | Server waking up — wait, then refresh |
| Error on screen | Try Chrome; clear browser cache |

### 6.2 Error Messages

| Message | Cause | Solution |
|---------|-------|---------|
| "Model not loaded" | Server restarting | Refresh the page |
| "Prediction failed" | Invalid input | Check all fields are filled |
| "LLM not available" | AI service down | Prediction still works |

### 6.3 Prediction Seems Wrong

1. Verify values are for **one store** (not combined totals)
2. Check values are in the $500K–$3M range per week
3. Confirm date fields match the week you are forecasting
4. Note: average error is ±$73,473 (~5% at $1.5M/week)

### 6.4 Results Disappeared

Results reset when the browser closes.
- ☑ Use **📋 History** tab — all session predictions saved there
- ☑ Click **"📥 Download History as CSV"** to save permanently
- ☑ Take a screenshot before closing

---

## 7. Frequently Asked Questions

**Q: How accurate is this tool?**
A: R²=0.9812 with average error of $73,473 per store —
approximately 5% error at typical sales volumes.

**Q: Do I need to fill all 13 fields?**
A: Yes. All fields are required. Date fields are auto-filled.

**Q: Can I forecast multiple stores?**
A: Yes — run the prediction separately for each store.

**Q: Is my data stored?**
A: No. Data is processed in real-time only. Nothing is saved
between sessions.

**Q: Why are default values around $1.5M and not $40M?**
A: The model is trained per individual store. A typical Walmart
store does $500K–$3M per week. $40M would be the aggregate
of ~45 stores combined.

**Q: Can I use this on my phone?**
A: Yes. Fully mobile-friendly.

**Q: Why does it take 30–60 seconds to load sometimes?**
A: Free hosting sleeps after 15 minutes of inactivity.
Wakes up automatically on the next visit.

**Q: What if AI Advisor doesn't respond?**
A: Refresh the page. Core prediction still works if AI is unavailable.

**Q: How often should I use this?**
A: Every Monday morning before placing weekly inventory orders.

---

## 8. Getting Help

**Developer:** Dany Deugoue
**Student ID:** A00316024
**Course:** AIE1014 — AI Applied Project | Cambrian College

**When reporting an issue, please include:**
- What you were trying to do
- What happened instead
- Any error messages displayed
- Browser and device (e.g., Chrome on Windows 11)
- Screenshots if possible

---

*AIE1014 — AI Applied Project | AIE1017 — Generative AI and LLMs*
*Team Dany | Cambrian College | Winter 2026*