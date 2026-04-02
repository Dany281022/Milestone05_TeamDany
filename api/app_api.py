"""
Weekly Sales Forecaster — Team Dany
AIE1014 - AI Applied Project Course | Assignment 04

FastAPI backend — hardened with logging, /info endpoint, and confidence scores.
Model: RandomForestRegressor trained on log1p(weekly_sales) — predictions are
converted back to dollar scale using numpy.expm1().
"""

import logging
import os
import time

import joblib
import numpy as np
import pandas as pd
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# ============================================================================
# LOGGING  (Stage 1.1 — required by Assignment 04)
# ============================================================================

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)s  %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)
logger = logging.getLogger(__name__)

# ============================================================================
# APP & MODEL
# ============================================================================

app = FastAPI(
    title="Weekly Sales Prediction API",
    description="Predicts next-week retail sales for a retail business manager.",
    version="1.0",
)

BASE_DIR   = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(BASE_DIR, "model.pkl")
logger.info("Loading model from %s …", model_path)
model = joblib.load(model_path)
logger.info("Model loaded: %s", type(model).__name__)

# Feature list — must match training order exactly
FEATURES = [
    "lag_1", "lag_2", "lag_4", "lag_8", "lag_12", "lag_26", "lag_52",
    "ma_4", "ma_12", "std_4", "weekofyear", "month", "year",
]

# Pre-warm model to avoid cold-start latency on first real request
_dummy = pd.DataFrame([{f: 0.0 for f in FEATURES}])
_dummy["weekofyear"] = 1
_dummy["month"]      = 1
_dummy["year"]       = 2024
model.predict(_dummy)
logger.info("Model warm-up complete.")

# ============================================================================
# SCHEMAS
# ============================================================================

class PredictionRequest(BaseModel):
    lag_1:      float
    lag_2:      float
    lag_4:      float
    lag_8:      float
    lag_12:     float
    lag_26:     float
    lag_52:     float
    ma_4:       float
    ma_12:      float
    std_4:      float
    weekofyear: int
    month:      int
    year:       int


class PredictionResponse(BaseModel):
    prediction:      float
    confidence:      str | None   # None for regressors — string interval returned instead
    status:          str
    timestamp:       str
    response_time_ms: float

# ============================================================================
# ENDPOINTS
# ============================================================================

@app.get("/health")
def health():
    """Health check — returns {'status': 'healthy'} when the API is running."""
    return {
        "status":       "healthy",
        "model_loaded": model is not None,
        "version":      "1.0",
    }


@app.get("/info")
def info():
    """Return model metadata, feature list, and performance metrics.

    Required fields (Stage 1.2):
        model_type, features_expected, version, description, performance
    """
    return {
        "model_type":        type(model).__name__,
        "features_expected": model.feature_names_in_.tolist(),
        "feature_importances": model.feature_importances_.tolist(),
        "num_features":      int(len(model.feature_names_in_)),
        "version":           "1.0",
        # description is REQUIRED by the Assignment 04 /info checklist
        "description": (
            "Predicts next-week retail sales in dollars using 13 lag and "
            "moving-average features derived from historical weekly sales data."
        ),
        "performance": {
            "r2":   0.2829,
            "rmse": 2062567.0,
            "mae":  1488586.0,
        },
        "confidence_note": (
            "RandomForestRegressor does not support predict_proba(). "
            "A ±10 % prediction interval is returned as a string instead."
        ),
    }


@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    """Run a prediction and return the result with a ±10 % interval.

    Stage 1.1 — logs every incoming request and every result.
    Stage 1.3 — confidence is None for regressors (interval string returned).
    """
    logger.info("Received prediction request: %s", request)

    try:
        start = time.time()

        features = pd.DataFrame([{
            "lag_1":      request.lag_1,
            "lag_2":      request.lag_2,
            "lag_4":      request.lag_4,
            "lag_8":      request.lag_8,
            "lag_12":     request.lag_12,
            "lag_26":     request.lag_26,
            "lag_52":     request.lag_52,
            "ma_4":       request.ma_4,
            "ma_12":      request.ma_12,
            "std_4":      request.std_4,
            "weekofyear": request.weekofyear,
            "month":      request.month,
            "year":       request.year,
        }])

        # Model was trained on log1p(weekly_sales) — convert back to dollar scale
        log_pred   = float(model.predict(features)[0])
        prediction = float(np.expm1(log_pred))

        # Stage 1.3 — confidence for regressors
        # predict_proba() does not exist for RandomForestRegressor.
        # A ±10 % interval is returned as a human-readable string instead.
        if hasattr(model, "predict_proba"):
            probs      = model.predict_proba(features)[0]
            confidence = str(float(max(probs)))
        else:
            confidence = f"USD {prediction * 0.90:,.0f} – USD {prediction * 1.10:,.0f} (±10 % interval)"

        elapsed_ms = round((time.time() - start) * 1000, 2)

        logger.info(
            "Prediction result: $%,.2f  interval: %s  time: %sms",
            prediction, confidence, elapsed_ms,
        )

        return PredictionResponse(
            prediction=prediction,
            confidence=confidence,          # string interval (not None) for clarity
            status="success",
            timestamp=pd.Timestamp.now().isoformat(),
            response_time_ms=elapsed_ms,
        )

    except Exception as exc:
        logger.error("Prediction failed: %s", exc)
        raise HTTPException(status_code=500, detail=str(exc))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
