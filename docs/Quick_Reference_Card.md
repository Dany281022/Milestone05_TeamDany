# Weekly Sales Forecaster
## Quick Reference Card

---

## 🔗 Access the Application

**Primary:** https://weekly-sales-forecaster-teamdany.streamlit.app/
**Backup:** https://weekly-sales-forecaster-team-dany-aie1014.onrender.com

> Bookmark the primary URL for quick Monday morning access!

---

## 📝 How to Use

| Step | Action |
|------|--------|
| 1 | Open the URL above in Chrome |
| 2 | Enter your store's weekly sales (see Input Fields below) |
| 3 | Click **"🔮 Get Prediction"** |
| 4 | Read your forecast + demand signal |
| 5 | Click **"💬 AI Advisor"** tab for business recommendations |

---

## 📊 Input Fields

| Field | What to Enter | Example |
|-------|--------------|---------|
| Last week's sales | Total store sales last week | $1,500,000 |
| Sales 2 weeks ago | Total store sales 2 weeks ago | $1,480,000 |
| Sales 4 weeks ago | Total store sales 4 weeks ago | $1,450,000 |
| Sales 8 weeks ago | Total store sales 8 weeks ago | $1,430,000 |
| Sales 12 weeks ago | Total store sales ~3 months ago | $1,400,000 |
| Sales 26 weeks ago | Total store sales ~6 months ago | $1,390,000 |
| Sales 1 year ago | Total store sales 1 year ago | $1,380,000 |
| 4-week average | (W1+W2+W3+W4) ÷ 4 | $1,465,000 |
| 12-week average | Sum of 12 weeks ÷ 12 | $1,430,000 |
| Sales variability | ~2–5% of weekly average | $25,000 |
| Week / Month / Year | Auto-filled — adjust if needed | 14 / 4 / 2026 |

> ⚠️ Enter values for **ONE store only** — typical range $500K–$3M/week

---

## 🎯 Understanding Results

| Signal | Meaning | Action |
|--------|---------|--------|
| 🟢 Stable | Within ±5% of last week | Maintain current operations |
| 🟡 Higher demand | More than 5% above last week | Increase inventory + add shifts |
| 🔵 Lower demand | More than 5% below last week | Reduce perishables + review staffing |

**Prediction Interval:** Shows the likely sales range (±10%)
Example: Forecast $1,420,688 → Range $1,278,619 — $1,562,757

---

## 🤖 AI Sales Advisor

After getting a prediction, go to the **💬 AI Advisor** tab:

| Button | What You Get |
|--------|-------------|
| Generate AI Business Analysis | Full explanation + inventory + staffing + risk |
| 📦 Inventory Advice | 3 specific inventory actions |
| 👥 Staffing Advice | 3 specific staffing adjustments |
| ⚠️ Risk Assessment | Top 3 risks for next week |

---

## ⚠️ Common Issues

| Problem | Solution |
|---------|---------|
| App takes 60s to load | Normal on first visit — server waking up. Wait and refresh |
| Results disappeared | Check **📋 History** tab or download CSV |
| Prediction seems off | Verify single-store values in $500K–$3M range |
| AI Advisor not responding | Refresh page — core prediction still works |

---

## 📋 Save Your Results

Go to **📋 History** tab → Click **"📥 Download History as CSV"**

---

## 📞 Need Help?

**Developer:** Dany Deugoue | A00316024
**Course:** AIE1014 | Cambrian College

---

## 📈 Model Performance

| Metric | Value |
|--------|-------|
| R² Score | 0.9812 |
| Average error (RMSE) | $73,473 per store |
| Typical error (MAE) | $47,281 per store |
| Training approach | Per-store (45 stores × 143 weeks) |

---

*Version 3.0 | April 6, 2026 | Team Dany | AIE1014 Cambrian College*