# Weekly Sales Forecaster — Team Dany
AIE1014 — AI Applied Project Course | Milestone 5

## Live Application
🔗 https://weekly-sales-forecaster-teamdany.streamlit.app/

## What This Project Does
This application predicts next-week retail sales for a Retail Business Manager using a RandomForestRegressor model trained on 13 historical lag and moving average features. Users enter sales history values through a web interface and receive instant sales forecasts formatted in dollars with a ±10% prediction interval, percentage change vs last week, and colour-coded demand signals to support inventory and staffing decisions.

**Stakeholder:** Retail Business Manager  
**GitHub:** https://github.com/Dany281022/Milestone05_TeamDany  
**Deployed URL:** https://weekly-sales-forecaster-teamdany.streamlit.app/

## Team
| Name | Student ID | Role |
|------|------------|------|
| Dany Deugoue | A00316024 | Solo Developer / MLOps Engineer |

## Architecture
This is a single-file Streamlit application — no separate API server required.

```
[User Browser] → [Streamlit Cloud] → [app.py + model.pkl] → [Prediction Output]
```

## Prerequisites
- Python 3.10 or higher
- pip
- Git

## Installation
1. Clone the repository
```bash
git clone https://github.com/Dany281022/Milestone05_TeamDany.git
cd Milestone05_TeamDany
```

2. Create and activate a virtual environment
```bash
python -m venv venv

# Windows:
venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## Running Locally
```bash
streamlit run app.py
```
App runs at: http://localhost:8501

## Project Structure
```
Milestone05_TeamDany/
├── app.py               ← Combined Streamlit app + model inference
├── model.pkl            ← Trained RandomForestRegressor (13 features, log1p)
├── requirements.txt     ← Dependencies (no version pins for Streamlit Cloud)
├── README.md
├── code/
│   ├── data_pipeline.ipynb   ← Data preprocessing pipeline
│   └── train_model.ipynb     ← Model training and evaluation
├── data/
│   └── processed/       ← X_train, X_test, y_train, y_test CSV files
├── docs/
│   └── TeamDany_Milestone4_Report.pdf
├── tests/
│   ├── test_integration.py
│   └── test_predict.py
└── ui/
    └── app_ui.py        ← Legacy Assignment04 UI (FastAPI version)
```

## Model Information
- **Algorithm:** RandomForestRegressor
- **Hyperparameters:** n_estimators=200, max_depth=None, min_samples_split=10, random_state=42
- **Target transformation:** log1p(y) at training, expm1() at inference
- **Features (13):** lag_1, lag_2, lag_4, lag_8, lag_12, lag_26, lag_52, ma_4, ma_12, std_4, weekofyear, month, year
- **Dataset:** Walmart Stores Weekly Sales (Kaggle, 6,436 rows)
- **Train/Test split:** Chronological cutoff January 1, 2012
- **R2 Score:** 0.2829
- **RMSE:** \$2,062,567
- **MAE:** \$1,488,586
- **Baseline RMSE (Naive):** \$2,481,007 (33.5% improvement)
- **Response time:** ~10-60ms (Streamlit Cloud)

## Features
- 🔮 **Prediction Tab** — Enter 13 lag features, get instant dollar forecast
- 📊 **Dashboard Tab** — Model performance metrics + real feature importance chart
- 📋 **History Tab** — Track all predictions with CSV download
- 🟢🟡🔵 **Colour-coded signals** — Stable / Higher demand / Lower demand
- 📈 **Contextual framing** — % change vs last week + plain-language advice

## Deployment
Deployed on Streamlit Cloud via GitHub integration:
1. Push code + model.pkl to GitHub
2. Connect repo at share.streamlit.io
3. Set main file to app.py
4. Streamlit Cloud auto-installs requirements.txt

## Known Issues & Limitations
- Model trained on Walmart aggregate data — predictions are directional estimates
- R2 of 0.28 indicates moderate fit with 48 training points
- No authentication — public access
- Cold start on first load: ~2s (subsequent calls ~10ms)

## Error Handling
| Situation | Behaviour |
|-----------|-----------|
| Model fails to load | Error message + app stops |
| Invalid input | Streamlit min_value=0.0 prevents negatives |
| Prediction error | Friendly error message displayed |

---
AIE1014 — AI Applied Project Course | Team Dany | Winter 2026
