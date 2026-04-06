# Weekly Sales Forecaster — Team Dany

AIE1014 — AI Applied Project Course | AIE1017 — Generative AI and LLMs | Winter 2026

---

## Impact

Training one model per store (45 models) instead of one aggregated model reduced RMSE by **96.4%** and pushed R² from 0.28 to **0.9812**.

| Metric | v1 — aggregated | v2 — per-store | Gain |
|--------|-----------------|----------------|------|
| R²     | 0.2829          | 0.9812         | +246.9% |
| RMSE   | $2,062,567      | $73,473        | -96.4% |
| MAE    | $1,488,586      | $47,281        | -96.8% |

Root cause of v1 failure: aggregating 45 stores into 143 weekly rows erased store-level patterns. Training per-store fixes this.

---

## Live Applications

| Interface | URL |
|-----------|-----|
| Streamlit | https://weekly-sales-forecaster-teamdany.streamlit.app/ |
| Render API | https://weekly-sales-forecaster-team-dany-aie1014.onrender.com |
| GitHub | https://github.com/Dany281022/Milestone05_TeamDany |

---

## What This Project Does

Predicts next-week retail sales for a Retail Business Manager.

The model is a RandomForestRegressor (v2) trained per-store on 13 lag and moving average features. Users input sales history through a web interface and receive an instant dollar forecast with a ±10% prediction interval, percentage change vs last week, colour-coded demand signals, and business recommendations via OpenAI GPT-4o-mini (Ollama fallback included).

**Stakeholder:** Retail Business Manager  
**Developer:** Dany Deugoue — A00316024 — Solo Developer / MLOps Engineer

---

## Architecture

### Streamlit (primary interface)

```
[User Browser] → [Streamlit Cloud] → [app.py + model.pkl + src/llm_client.py] → [Prediction + AI Advice]
```

### Render (REST API + dashboard)

```
[User Browser] → [Render Docker] → [FastAPI api/main.py] → [/predict + /explain + /health]
                                          ↓
                                   [model.pkl + src/llm_client.py]
```

---

## Prerequisites

- Python 3.10+
- pip
- Git

---

## Installation

**1. Clone the repo**

```bash
git clone https://github.com/Dany281022/Milestone05_TeamDany.git
cd Milestone05_TeamDany
```

**2. Create and activate a virtual environment**

```bash
python -m venv venv

# Windows
venv\Scripts\activate

```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Set environment variables**

```bash
cp .env.example .env
```

Edit `.env`:

```
OPENAI_API_KEY=sk-...
OLLAMA_MODEL=llama3.2:latest
OLLAMA_BASE_URL=http://localhost:11434
```

---

## Running Locally

```bash
# Streamlit
streamlit run app.py

# FastAPI
uvicorn api.main:app --reload
```

| Interface | URL |
|-----------|-----|
| Streamlit | http://localhost:8501 |
| FastAPI   | http://localhost:8000 |
| Swagger   | http://localhost:8000/docs |

---

## Project Structure

```
Milestone05_TeamDany/
├── app.py                    ← Streamlit app (4 tabs + LLM advisor)
├── model.pkl                 ← RandomForestRegressor v2 (per-store, R²=0.9812)
├── requirements.txt          ← Full dependencies
├── requirements_render.txt   ← Render-only dependencies
├── render.yaml               ← Render deployment config
├── Dockerfile                ← Docker container for Render
├── .env.example              ← Environment variable template
├── README.md
├── api/
│   ├── __init__.py
│   └── main.py               ← FastAPI: /predict, /explain, /health, /info
├── src/
│   ├── __init__.py
│   └── llm_client.py         ← OpenAI + Ollama fallback LLM client
├── static/
│   └── index.html            ← Dashboard HTML served by Render
├── code/
│   ├── data_pipeline.ipynb   ← Data preprocessing pipeline
│   ├── train_model.ipynb     ← Model v1 (RF aggregated, R²=0.2829)
│   └── train_model_v2.ipynb  ← Model v2 (RF per-store, R²=0.9812)
├── data/
│   ├── raw/
│   │   └── Walmart.csv       ← Raw Walmart dataset — Kaggle, 6,435 rows
│   └── processed/
│       ├── X_train.csv       ← Training features (2,160 rows)
│       ├── X_test.csv        ← Test features (1,935 rows)
│       ├── y_train.csv       ← Training targets
│       └── y_test.csv        ← Test targets
├── models/
│   ├── rf_model_v2.pkl       ← RandomForest v2 (reference)
│   └── xgb_model.pkl         ← XGBoost (reference)
├── docs/
│   └── TeamDany_Milestone5_Report.pdf
└── tests/
    ├── test_integration.py   ← 10 pipeline integration tests
    └── test_predict.py       ← 14 model unit tests
```

---

## Model — v2 (Production)

| Parameter | Value |
|-----------|-------|
| Algorithm | RandomForestRegressor |
| Training strategy | Per-store — 45 stores × ~143 weeks = 6,435 rows |
| n_estimators | 200 |
| max_depth | None |
| min_samples_split | 10 |
| random_state | 42 |
| Target transform | log1p(y) at training / expm1() at inference |
| Dataset | Walmart Stores Weekly Sales — Kaggle, 6,435 rows, 45 stores |
| Train/Test split | Chronological cutoff January 1, 2012 |
| R² Score | **0.9812** |
| RMSE | **$73,473** per store |
| MAE | **$47,281** per store |
| Test set size | 1,935 rows — 1,935 unique predictions validated |

**Features (13):**
`lag_1`, `lag_2`, `lag_4`, `lag_8`, `lag_12`, `lag_26`, `lag_52`, `ma_4`, `ma_12`, `std_4`, `weekofyear`, `month`, `year`

### Model v1 (archived)

| Metric | Value |
|--------|-------|
| R² | 0.2829 |
| RMSE | $2,062,567 |
| MAE | $1,488,586 |

Failure mode: one model trained on 143 aggregate weekly rows across 45 stores. Store-level variance was averaged out.

---

## API Endpoints (Render)

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Dashboard HTML |
| `/health` | GET | Health probe + model/LLM status |
| `/predict` | POST | Predict next-week sales — 13 features required |
| `/explain` | POST | LLM-powered business explanation |
| `/info` | GET | Model metadata |
| `/docs` | GET | Swagger UI |

---

## App Features

| Tab | What it does |
|-----|--------------|
| Prediction | Enter 13 lag features, get an instant per-store dollar forecast |
| Dashboard | v1 vs v2 comparison + feature importance chart |
| History | All predictions logged with CSV download |
| AI Advisor | GPT-4o-mini explanations + inventory / staffing / risk buttons |

Colour-coded demand signals: Stable / Higher demand / Lower demand  
LLM fallback chain: OpenAI GPT-4o-mini → Ollama (llama3.2)

---

## LLM Integration (AIE1017)

- **Explain prediction** — plain-English business analysis of the forecast
- **Ask AI anything** — custom retail business questions
- **Quick recommendations** — inventory, staffing, and risk assessment

---

## Deployment

### Streamlit Cloud

```
1. Push code + model.pkl to GitHub
2. Connect repo at share.streamlit.io
3. Set main file: app.py
4. Add secret: OPENAI_API_KEY
```

### Render (Docker)

```
1. Push code to GitHub
2. New Web Service → connect repo
3. Render auto-detects Dockerfile
4. Add env vars: OPENAI_API_KEY, MODEL_PATH=model.pkl
```

---

## Tests

```bash
python -m pytest tests/ -v -s
```

| Result | Detail |
|--------|--------|
| 24/24 tests passing | 10 integration + 14 unit |
| RMSE validated | $73,473 on 1,935 real test rows |
| Predictions | 1,935 unique outputs across test set |

---

## Error Handling

| Situation | Behaviour |
|-----------|-----------|
| Model fails to load | Error displayed, app continues |
| LLM unavailable | Warning shown, prediction still works |
| Invalid input | `min_value=0.0` blocks negatives |
| API error | Friendly error message displayed |

---

AIE1014 — AI Applied Project Course | AIE1017 — Generative AI and LLMs | Team Dany | Winter 2026
