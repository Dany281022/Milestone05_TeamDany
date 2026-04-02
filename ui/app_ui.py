"""
Weekly Sales Forecaster — Team Dany
AIE1014 - AI Applied Project Course | Assignment 04

Streamlit UI — connects to FastAPI backend at http://127.0.0.1:8000
Stage 2 additions: prediction history, live model info panel, colour-coded results.

Note: 127.0.0.1 is used instead of localhost to avoid a ~2 s IPv6 DNS fallback
delay on Windows systems.
"""

import streamlit as st
import requests
import pandas as pd
import plotly.express as px
from datetime import datetime

# ============================================================================
# CONFIGURATION
# ============================================================================

APP_TITLE = "📈 Weekly Sales Forecaster"
APP_ICON  = "📈"
VERSION   = "2.0.0"
API_URL   = "http://127.0.0.1:8000"   # 127.0.0.1 avoids Windows IPv6 delay

# ============================================================================
# PAGE CONFIG — must be the very first Streamlit command
# ============================================================================

st.set_page_config(
    page_title="Weekly Sales Forecaster",
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================================
# SESSION STATE — Stage 2.1
# Initialise history list on first load only.
# Subsequent reruns skip this block because the key already exists.
# ============================================================================

if "history" not in st.session_state:
    st.session_state.history = []

# ============================================================================
# API HELPER — Stage 2.1 (call_predict_api used by batch CSV too)
# ============================================================================

def call_predict_api(payload: dict) -> dict:
    """POST payload to /predict and return a normalised result dict."""
    try:
        response = requests.post(f"{API_URL}/predict", json=payload, timeout=10)
        if response.status_code == 200:
            return {"success": True, "data": response.json()}
        error_detail = response.json().get("detail", f"HTTP {response.status_code}")
        return {"success": False, "error": error_detail}
    except requests.exceptions.ConnectionError:
        return {"success": False, "error": "Cannot connect to API. Start it with: python app_api.py"}
    except requests.exceptions.Timeout:
        return {"success": False, "error": "API took too long to respond. Try again."}
    except Exception as exc:
        return {"success": False, "error": f"Unexpected error: {exc}"}

# ============================================================================
# SIDEBAR — Stage 2.2: live model info panel fetched from /info
# ============================================================================

with st.sidebar:
    st.title(APP_TITLE)
    st.markdown("**Team Dany | AIE1014**")
    st.divider()

    # ── API health status ──────────────────────────────────────────────────
    try:
        health_resp = requests.get(f"{API_URL}/health", timeout=5)
        if health_resp.status_code == 200:
            st.success("✅ API Connected")
        else:
            st.error(f"❌ API Error: {health_resp.status_code}")
    except requests.exceptions.ConnectionError:
        st.error("❌ API Offline")
        st.code("python app_api.py", language="bash")
    except requests.exceptions.Timeout:
        st.warning("⚠️ API Slow to Respond")

    st.divider()

    # ── Live model info panel (Stage 2.2) — fetched from /info, not hardcoded ──
    st.header("📊 Model Information")
    try:
        info_resp = requests.get(f"{API_URL}/info", timeout=5)
        if info_resp.status_code == 200:
            info = info_resp.json()
            st.write(f"**Type:** {info.get('model_type', 'Unknown')}")
            st.write(f"**Version:** {info.get('version', 'Unknown')}")
            st.write(f"**Description:** {info.get('description', 'N/A')}")

            perf = info.get("performance", {})
            if perf:
                st.metric(label="R² SCORE",  value=f"{perf.get('r2', 0):.4f}")
                st.metric(label="RMSE",       value=f"${perf.get('rmse', 0):,.0f}")
                st.metric(label="MAE",        value=f"${perf.get('mae', 0):,.0f}")

            features = info.get("features_expected", [])
            with st.expander(f"View {len(features)} features"):
                for feat in features:
                    st.write(f"• {feat}")
        else:
            st.warning("Could not load model info.")
    except Exception:
        st.write("Model info unavailable — is the API running?")

    st.divider()
    st.caption(f"Version {VERSION} | AIE1014 Capstone")

# ============================================================================
# MAIN TITLE
# ============================================================================

st.title(APP_TITLE)
st.write("Predict next week's retail sales using historical lag features and moving averages.")
st.divider()

# ============================================================================
# TABS
# ============================================================================

tab1, tab2, tab3 = st.tabs(["🔮 Prediction", "📊 Dashboard", "📋 History"])

# ══════════════════════════════════════════════════════════════════════════════
# TAB 1 — PREDICTION
# ══════════════════════════════════════════════════════════════════════════════

with tab1:
    st.markdown("### 📝 Enter Your Sales Data")

    now = datetime.now()

    with st.form("prediction_form"):
        st.markdown("#### Lag Features")
        col1, col2 = st.columns(2)
        with col1:
            lag_1  = st.number_input("Lag 1 — Previous week ($)",  min_value=0.0, value=100.0)
            lag_4  = st.number_input("Lag 4 — 4 weeks ago ($)",    min_value=0.0, value=100.0)
            lag_12 = st.number_input("Lag 12 — 12 weeks ago ($)",  min_value=0.0, value=100.0)
            lag_52 = st.number_input("Lag 52 — 1 year ago ($)",    min_value=0.0, value=100.0)
        with col2:
            lag_2  = st.number_input("Lag 2 — 2 weeks ago ($)",    min_value=0.0, value=100.0)
            lag_8  = st.number_input("Lag 8 — 8 weeks ago ($)",    min_value=0.0, value=100.0)
            lag_26 = st.number_input("Lag 26 — 26 weeks ago ($)",  min_value=0.0, value=100.0)

        st.markdown("#### Moving Averages & Volatility")
        col3, col4, col5 = st.columns(3)
        with col3:
            ma_4  = st.number_input("MA 4 weeks ($)",  min_value=0.0, value=100.0)
        with col4:
            ma_12 = st.number_input("MA 12 weeks ($)", min_value=0.0, value=100.0)
        with col5:
            std_4 = st.number_input("Std Dev 4 weeks", min_value=0.0, value=10.0)

        st.markdown("#### Date Features (Auto-filled)")
        col6, col7, col8 = st.columns(3)
        with col6:
            weekofyear = st.number_input("Week of Year", min_value=1,    max_value=52,   value=int(now.isocalendar()[1]))
        with col7:
            month      = st.number_input("Month",        min_value=1,    max_value=12,   value=now.month)
        with col8:
            year       = st.number_input("Year",         min_value=2000, max_value=2100, value=now.year)

        submitted = st.form_submit_button("🔮 Get Prediction", use_container_width=True)

    # ── Handle form submission ─────────────────────────────────────────────
    if submitted:
        payload = {
            "lag_1": lag_1, "lag_2": lag_2, "lag_4": lag_4,
            "lag_8": lag_8, "lag_12": lag_12, "lag_26": lag_26,
            "lag_52": lag_52, "ma_4": ma_4, "ma_12": ma_12,
            "std_4": std_4, "weekofyear": int(weekofyear),
            "month": int(month), "year": int(year),
        }

        with st.spinner("Generating sales forecast…"):
            result = call_predict_api(payload)

        if result["success"]:
            data       = result["data"]
            prediction = data["prediction"]
            confidence = data.get("confidence")
            resp_time  = data.get("response_time_ms", "N/A")
            formatted  = f"${prediction:,.2f}"

            # ── Stage 2.3 — Colour-coded results for regression ──────────
            # Baseline comparison: prediction vs last week (lag_1)
            if lag_1 > 0:
                pct_change = ((prediction - lag_1) / lag_1) * 100
                direction  = "above" if pct_change >= 0 else "below"
                abs_change = abs(pct_change)

                if abs_change <= 5:
                    st.success(
                        f"🟢 Stable week ahead — Forecast is {abs_change:.1f}% {direction} "
                        f"last week. Continue routine inventory and staffing."
                    )
                elif pct_change > 5:
                    st.warning(
                        f"🟡 Higher demand expected — Forecast is {abs_change:.1f}% above "
                        f"last week. Consider increasing inventory and staffing."
                    )
                else:
                    st.info(
                        f"🔵 Lower demand expected — Forecast is {abs_change:.1f}% below "
                        f"last week. Consider reducing perishable orders."
                    )

                st.info(
                    f"📊 Forecast **{formatted}** is **{abs_change:.1f}% {direction}** "
                    f"last week's sales of **${lag_1:,.2f}**. "
                    f"Use this to adjust inventory and staffing for next week."
                )
            else:
                st.success(f"✅ Predicted Next-Week Sales: **{formatted}**")

            # Prediction interval
            if confidence:
                st.markdown(f"**Prediction Interval:** {confidence}")

            # Metric tiles
            c1, c2, c3, c4 = st.columns(4)
            with c1:
                st.metric("Forecast",      formatted)
            with c2:
                st.metric("Week",          f"W{weekofyear}")
            with c3:
                st.metric("Model",         "Random Forest")
            with c4:
                st.metric("Response Time", f"{resp_time} ms")

            # ── Stage 2.1 — Save to session history ───────────────────────
            st.session_state.history.append({
                "Timestamp":          datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Week":               int(weekofyear),
                "Month":              int(month),
                "Year":               int(year),
                "Lag 1 ($)":          lag_1,
                "Lag 52 ($)":         lag_52,
                "Prediction ($)":     round(prediction, 2),
                "Response Time (ms)": resp_time,
            })

        else:
            st.error(f"❌ Prediction failed: {result['error']}")

    # ── Stage 2.1 — Prediction history table ──────────────────────────────
    if st.session_state.history:
        st.divider()
        st.subheader("📋 Prediction History (this session)")
        history_df = pd.DataFrame(st.session_state.history)
        st.dataframe(history_df, use_container_width=True)

        csv = history_df.to_csv(index=False)
        st.download_button(
            label="⬇️  Download history as CSV",
            data=csv,
            file_name="prediction_history.csv",
            mime="text/csv",
        )
        if st.button("🗑️  Clear history"):
            st.session_state.history = []
            st.rerun()

    # ── 🏆 Challenge — Batch CSV prediction ───────────────────────────────
    st.divider()
    st.markdown("#### 📁 Batch Prediction from CSV (optional)")
    uploaded = st.file_uploader("Upload CSV for batch predictions", type=["csv"])
    if uploaded is not None:
        batch_df = pd.read_csv(uploaded)
        required_cols = set([
            "lag_1","lag_2","lag_4","lag_8","lag_12","lag_26","lag_52",
            "ma_4","ma_12","std_4","weekofyear","month","year"
        ])
        missing_cols = required_cols - set(batch_df.columns)
        if missing_cols:
            st.error(f"❌ CSV is missing required columns: {missing_cols}")
        else:
            st.write(f"Loaded {len(batch_df)} rows — running predictions…")
            batch_results = []
            for _, row in batch_df.iterrows():
                r = call_predict_api(row.to_dict())
                batch_results.append(
                    r["data"].get("prediction", "error") if r["success"] else "error"
                )
            batch_df["prediction ($)"] = batch_results
            st.dataframe(batch_df, use_container_width=True)
            st.download_button(
                "Download batch results",
                batch_df.to_csv(index=False),
                "batch_results.csv",
            )

# ══════════════════════════════════════════════════════════════════════════════
# TAB 2 — DASHBOARD
# ══════════════════════════════════════════════════════════════════════════════

with tab2:
    st.markdown("### 📊 Model Performance Dashboard")

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.metric("R² Score", "0.2829",     help="Higher is better (max 1.0)")
    with c2:
        st.metric("RMSE",     "$2,062,567", help="Root Mean Squared Error")
    with c3:
        st.metric("MAE",      "$1,488,586", help="Mean Absolute Error")
    with c4:
        st.metric("Features", "13",         help="Number of input features")

    st.divider()

    # Feature importance — live from /info
    st.markdown("#### 🎯 Feature Importance")
    try:
        info_resp = requests.get(f"{API_URL}/info", timeout=5)
        if info_resp.status_code == 200:
            info_data   = info_resp.json()
            df_imp = pd.DataFrame({
                "Feature":    info_data["features_expected"],
                "Importance": info_data["feature_importances"],
            }).sort_values("Importance", ascending=True)
            fig_imp = px.bar(
                df_imp, x="Importance", y="Feature", orientation="h",
                title="Feature Importance — Random Forest",
                color="Importance", color_continuous_scale="blues",
                text="Importance",
            )
            fig_imp.update_traces(texttemplate="%{text:.3f}", textposition="outside")
            fig_imp.update_layout(showlegend=False, height=500)
            st.plotly_chart(fig_imp, use_container_width=True)
    except Exception:
        st.info("Feature importance will appear once the API is connected.")

    st.divider()
    st.markdown("#### 📈 Prediction History Chart")
    if st.session_state.history:
        df_h = pd.DataFrame(st.session_state.history)
        fig_h = px.line(
            df_h, x="Timestamp", y="Prediction ($)",
            title="Sales Predictions Over Time",
            markers=True, line_shape="spline",
        )
        fig_h.update_traces(line_color="#1f77b4", marker_size=8)
        fig_h.update_layout(height=400)
        st.plotly_chart(fig_h, use_container_width=True)
    else:
        st.info("Make predictions in the Prediction tab to see the chart here.")

    st.divider()
    st.markdown("#### ⚡ Response Time History")
    if st.session_state.history:
        df_h = pd.DataFrame(st.session_state.history)
        fig_rt = px.bar(
            df_h, x="Timestamp", y="Response Time (ms)",
            title="API Response Time per Prediction (ms)",
            color="Response Time (ms)", color_continuous_scale="greens",
        )
        fig_rt.add_hline(y=1000, line_dash="dash", line_color="orange",
                         annotation_text="Target < 1000 ms")
        fig_rt.update_layout(height=350)
        st.plotly_chart(fig_rt, use_container_width=True)
    else:
        st.info("Make predictions to see response time chart.")

# ══════════════════════════════════════════════════════════════════════════════
# TAB 3 — HISTORY
# ══════════════════════════════════════════════════════════════════════════════

with tab3:
    st.markdown("### 📋 Prediction History")

    if st.session_state.history:
        df_h = pd.DataFrame(st.session_state.history)

        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.metric("Total Predictions", len(df_h))
        with c2:
            st.metric("Avg Forecast", f"${df_h['Prediction ($)'].mean():,.2f}")
        with c3:
            st.metric("Max Forecast", f"${df_h['Prediction ($)'].max():,.2f}")
        with c4:
            st.metric("Min Forecast", f"${df_h['Prediction ($)'].min():,.2f}")

        st.dataframe(df_h, use_container_width=True)

        csv = df_h.to_csv(index=False)
        st.download_button(
            label="📥 Download History as CSV",
            data=csv,
            file_name="predictions_history.csv",
            mime="text/csv",
        )

        if st.button("🗑️ Clear History"):
            st.session_state.history = []
            st.rerun()
    else:
        st.info("No predictions yet. Go to the Prediction tab to get started!")

# ============================================================================
# FOOTER
# ============================================================================

st.divider()
c1, c2, c3 = st.columns(3)
with c1:
    st.caption("AIE1014 Capstone Project")
with c2:
    st.caption(f"Version {VERSION} | Team Dany")
with c3:
    st.caption("Stakeholder: Retail Business Manager")
