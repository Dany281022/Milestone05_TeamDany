# Weekly Sales Forecaster — Final Technical Report
AIE1014 — AI Applied Project Course | Milestone 5

**Team:** Team Dany
**Student:** Dany Deugoue | A00316024
**Date:** April 6, 2026
**Deployed:** https://weekly-sales-forecaster-teamdany.streamlit.app/

---

## 1. Project Overview

### 1.1 Problem Statement
Retail Business Managers collect years of sales data but lack accessible
tools to convert it into reliable weekly forecasts. Manual forecasting
using spreadsheets is slow, inaccurate, and requires expertise most
managers do not have. This creates costly inventory and staffing decisions.

### 1.2 Solution
The Weekly Sales Forecaster is a deployed machine learning application
that predicts next-week store sales from 13 historical lag and moving
average features, with AI-powered business recommendations via
OpenAI GPT-4o-mini.

### 1.3 Stakeholder
**Role:** Retail Business Manager
**Need:** Monday morning sales forecasts to plan inventory orders and staffing
**Value delivered:** Accurate forecast in <1 second vs 2 hours of manual work

---

## 2. Technical Architecture

### 2.1 System Overview
User Browser
↓
Streamlit Cloud (app.py)          Render Docker (api/main.py)
↓                                      ↓
model.pkl (RandomForest v2)        FastAPI /predict + /explain
↓                                      ↓
src/llm_client.py              OpenAI GPT-4o-mini → Ollama fallback

### 2.2 Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| ML Framework | scikit-learn 1.7.2 | RandomForestRegressor |
| Model Boost | XGBoost 3.2.0 | Tested (RF outperformed) |
| Web Framework | Streamlit 1.55.0 | Primary user interface |
| API Framework | FastAPI 0.135.2 | REST API on Render |
| LLM | OpenAI GPT-4o-mini | AI Sales Advisor |
| LLM Fallback | Ollama llama3.2 | Local offline fallback |
| Deployment 1 | Streamlit Cloud | Primary interface |
| Deployment 2 | Render + Docker | REST API |
| Data Processing | pandas 2.3.3 | Feature engineering |
| Testing | pytest 9.0.2 | 24 automated tests |

### 2.3 File Structure
Milestone06_TeamDany/
├── app.py                    ← Streamlit (4 tabs + LLM advisor)
├── model.pkl                 ← RandomForestRegressor v2 (R²=0.9812)
├── api/main.py               ← FastAPI endpoints
├── src/llm_client.py         ← OpenAI + Ollama fallback
├── static/index.html         ← Render dashboard
├── code/
│   ├── train_model.ipynb     ← v1 training (R²=0.2829)
│   └── train_model_v2.ipynb  ← v2 training (R²=0.9812)
├── data/
│   ├── raw/Walmart.csv       ← Source data (6,435 rows)
│   └── processed/            ← X_train, X_test, y_train, y_test
├── tests/
│   ├── test_predict.py       ← 14 model unit tests
│   └── test_integration.py   ← 10 pipeline tests
└── docs/                     ← All documentation