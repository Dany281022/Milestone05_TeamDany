# tests/test_integration.py
"""
Weekly Sales Forecaster — Integration Test Suite
AIE1014 | Assignment 04 | Team Dany

Run with:  python -m pytest tests/test_integration.py -v

Note: 127.0.0.1 is used instead of localhost to avoid a ~2 s IPv6 DNS fallback
delay on Windows systems.
"""

import time

import pytest
import requests

API_URL = "http://127.0.0.1:8000"

# ---------------------------------------------------------------------------
# Valid payload — all 13 features the model expects.
# Values match the default inputs in the UI.
# ---------------------------------------------------------------------------
VALID_PAYLOAD = {
    "lag_1":      100.0,
    "lag_2":       95.0,
    "lag_4":       90.0,
    "lag_8":       88.0,
    "lag_12":      85.0,
    "lag_26":      80.0,
    "lag_52":      75.0,
    "ma_4":        93.0,
    "ma_12":       87.0,
    "std_4":        5.0,
    "weekofyear":  12,
    "month":        3,
    "year":      2026,
}

# ── Fixture: skip all tests if the API is offline ───────────────────────────
@pytest.fixture(autouse=True)
def api_must_be_running():
    try:
        requests.get(f"{API_URL}/health", timeout=3)
    except requests.exceptions.ConnectionError:
        pytest.skip("API is offline — start it with: python app_api.py")


# ── Happy Path ───────────────────────────────────────────────────────────────

def test_health_check():
    """Health endpoint returns 200 and status=='healthy'."""
    r = requests.get(f"{API_URL}/health")
    assert r.status_code == 200
    assert r.json()["status"] == "healthy"


def test_info_endpoint():
    """★ NEW — /info returns all required fields including description."""
    r = requests.get(f"{API_URL}/info")
    assert r.status_code == 200
    data = r.json()
    assert "model_type"        in data
    assert "features_expected" in data
    assert "version"           in data
    assert "description"       in data   # required by Assignment 04 checklist


def test_valid_prediction():
    """A complete, valid payload returns 200 with prediction and status=='success'."""
    r = requests.post(f"{API_URL}/predict", json=VALID_PAYLOAD)
    assert r.status_code == 200
    data = r.json()
    assert "prediction" in data
    assert data["status"] == "success"
    assert isinstance(data["prediction"], float)


def test_confidence_returned():
    """confidence must be present — string interval is valid for regressors."""
    r = requests.post(f"{API_URL}/predict", json=VALID_PAYLOAD)
    assert r.status_code == 200
    data = r.json()
    assert "confidence" in data
    # RandomForestRegressor returns a string interval; None is also acceptable
    assert data["confidence"] is None or isinstance(data["confidence"], (float, str))


# ── Edge Cases ───────────────────────────────────────────────────────────────

def test_minimum_values():
    """All-zero lag/ma/std values must still return 200."""
    payload = {k: 0.0 for k in VALID_PAYLOAD}
    payload["weekofyear"] = 1
    payload["month"]      = 1
    payload["year"]       = 2024
    r = requests.post(f"{API_URL}/predict", json=payload)
    assert r.status_code == 200


def test_maximum_values():
    """Very large lag values must still return 200."""
    payload = {**VALID_PAYLOAD,
               "lag_1":  99999.0,
               "lag_2":  99999.0,
               "lag_52": 99999.0}
    r = requests.post(f"{API_URL}/predict", json=payload)
    assert r.status_code == 200


# ── Error Handling ───────────────────────────────────────────────────────────

def test_missing_required_field():
    """Omitting lag_4 (a required field) must return 400 or 422."""
    payload = {k: v for k, v in VALID_PAYLOAD.items() if k != "lag_4"}
    r = requests.post(f"{API_URL}/predict", json=payload)
    assert r.status_code in [400, 422]


def test_empty_request_body():
    """An empty body must return 400 or 422."""
    r = requests.post(f"{API_URL}/predict", json={})
    assert r.status_code in [400, 422]


def test_wrong_data_type():
    """Sending a string where a float is expected must return 400, 422, or 500."""
    payload = {**VALID_PAYLOAD, "lag_1": "not_a_number"}
    r = requests.post(f"{API_URL}/predict", json=payload)
    assert r.status_code in [400, 422, 500]


# ── Performance ──────────────────────────────────────────────────────────────

def test_response_time_under_2_seconds():
    """★ NEW — each prediction must respond in under 2 seconds."""
    start   = time.time()
    r       = requests.post(f"{API_URL}/predict", json=VALID_PAYLOAD)
    elapsed = time.time() - start
    assert r.status_code == 200
    assert elapsed < 2.0, f"Response took {elapsed:.2f}s — exceeds 2 s limit"


def test_consistent_predictions():
    """★ NEW — same input must always produce the same prediction."""
    predictions = set()
    for _ in range(5):
        r = requests.post(f"{API_URL}/predict", json=VALID_PAYLOAD)
        assert r.status_code == 200
        predictions.add(round(r.json()["prediction"], 2))
    assert len(predictions) == 1, f"Inconsistent predictions detected: {predictions}"


# ── 🏆 Challenge — Average response time over 20 calls ──────────────────────

def test_average_response_time():
    """🏆 CHALLENGE — average over 20 calls must be under 1 second."""
    times = []
    for _ in range(20):
        start = time.time()
        requests.post(f"{API_URL}/predict", json=VALID_PAYLOAD)
        times.append(time.time() - start)
    avg = sum(times) / len(times)
    print(f"\nMin: {min(times):.3f}s  Max: {max(times):.3f}s  Avg: {avg:.3f}s")
    assert avg < 1.0, f"Average response too slow: {avg:.3f}s"
