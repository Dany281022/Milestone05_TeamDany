"""
Weekly Sales Forecaster — Team Dany
AIE1014 - AI Applied Project Course | Milestone 5

Deployed ML Prediction Application — Combined Streamlit + Model
Stakeholder: Retail Business Manager
"""

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import plotly.express as px
from datetime import datetime

# ============================================================================
# CONFIGURATION
# ============================================================================

APP_TITLE    = "📈 Weekly Sales Forecaster"
APP_ICON     = "📈"
VERSION      = "2.0.0"
MODEL_PATH   = "model.pkl"
FEATURES     = ['lag_1', 'lag_2', 'lag_4', 'lag_8', 'lag_12', 'lag_26', 'lag_52',
                'ma_4', 'ma_12', 'std_4', 'weekofyear', 'month', 'year']

# ============================================================================
# PAGE CONFIG — must be first Streamlit command
# ============================================================================

st.set_page_config(
    page_title="Weekly Sales Forecaster",
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============================================================================
# LOAD MODEL — cached so it only loads once at startup
# ============================================================================

@st.cache_resource
def load_model():
    try:
        model = joblib.load(MODEL_PATH)
        return model, None
    except Exception as e:
        return None, str(e)

model, model_error = load_model()

# ============================================================================
# HELPER FUNCTIONS
# ============================================================================

def make_prediction(lag_1, lag_2, lag_4, lag_8, lag_12, lag_26, lag_52,
                    ma_4, ma_12, std_4, weekofyear, month, year):
    """Make prediction using the loaded model.
    Model was trained on log1p(y) — expm1 converts back to dollar scale.
    """
    try:
        import time
        start = time.time()

        features = pd.DataFrame([{
            "lag_1": lag_1, "lag_2": lag_2, "lag_4": lag_4,
            "lag_8": lag_8, "lag_12": lag_12, "lag_26": lag_26,
            "lag_52": lag_52, "ma_4": ma_4, "ma_12": ma_12,
            "std_4": std_4, "weekofyear": weekofyear,
            "month": month, "year": year
        }])

        # Model trained on log1p(y) — apply expm1 to get back to dollar scale
        prediction  = float(np.expm1(model.predict(features)[0]))
        log_pred = float(model.predict(features)[0])
        # Limit the raw prediction to avoid infinite values
        log_pred = min(log_pred, 17.5)  # Arbitrary limit to prevent 'inf' after expm1 transformation
        prediction = float(np.expm1(log_pred))
        # Limite la prédiction à ±50% de la valeur de lag_1 (vente de la semaine précédente)
        prediction = max(min(prediction, lag_1 * 1.5), lag_1 * 0.5)
        prediction = float(np.expm1(log_pred))
        elapsed_ms  = round((time.time() - start) * 1000, 2)
        lower       = prediction * 0.90
        upper       = prediction * 1.10
        confidence  = f"USD {lower:,.0f} - USD {upper:,.0f} (+-10% interval)"

        return {
            "success":          True,
            "prediction":       prediction,
            "confidence":       confidence,
            "response_time_ms": elapsed_ms
        }
    except Exception as e:
        return {"success": False, "error": str(e)}

# ============================================================================
# SIDEBAR
# ============================================================================

st.sidebar.title("📈 Weekly Sales Forecaster")
st.sidebar.markdown("**Team Dany | AIE1014**")
st.sidebar.divider()

if model is not None:
    st.sidebar.success("✅ Model Loaded")
else:
    st.sidebar.error(f"❌ Model Error: {model_error}")

st.sidebar.divider()

st.sidebar.markdown("### 📊 Model Info")
st.sidebar.write("**Model:** RandomForestRegressor")
st.sidebar.write("**Features:** 13")
st.sidebar.write("**R2 Score:** 0.3025")
st.sidebar.write("**RMSE:** $2,034,160")
st.sidebar.write("**MAE:** $1,472,779")
st.sidebar.write("**Avg Response:** ~10ms")

st.sidebar.divider()
st.sidebar.markdown("**Stakeholder:** Retail Business Manager")
st.sidebar.caption(f"Version {VERSION} | AIE1014 Capstone")

# ============================================================================
# MAIN TITLE
# ============================================================================

st.title("📈 Weekly Sales Forecaster — Team Dany")
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

    if model is None:
        st.error("Model failed to load. Please contact support.")
        st.stop()

    now = datetime.now()

    with st.form("prediction_form"):
        st.markdown("#### Lag Features")
        col1, col2 = st.columns(2)
        with col1:
            lag_1  = st.number_input("Lag 1 — Previous week ($)",  min_value=0.0, value=40000000.0)
            lag_4  = st.number_input("Lag 4 — 4 weeks ago ($)",    min_value=0.0, value=38000000.0)
            lag_12 = st.number_input("Lag 12 — 12 weeks ago ($)",  min_value=0.0, value=36000000.0)
            lag_52 = st.number_input("Lag 52 — 1 year ago ($)",    min_value=0.0, value=34000000.0)
        with col2:
            lag_2  = st.number_input("Lag 2 — 2 weeks ago ($)",    min_value=0.0, value=39000000.0)
            lag_8  = st.number_input("Lag 8 — 8 weeks ago ($)",    min_value=0.0, value=37000000.0)
            lag_26 = st.number_input("Lag 26 — 26 weeks ago ($)",  min_value=0.0, value=35000000.0)

        st.markdown("#### Moving Averages & Volatility")
        col3, col4, col5 = st.columns(3)
        with col3:
            ma_4  = st.number_input("MA 4 weeks ($)",  min_value=0.0, value=38500000.0)
        with col4:
            ma_12 = st.number_input("MA 12 weeks ($)", min_value=0.0, value=37000000.0)
        with col5:
            std_4 = st.number_input("Std Dev 4 weeks", min_value=0.0, value=500000.0)

        st.markdown("#### Date Features (Auto-filled)")
        col6, col7, col8 = st.columns(3)
        with col6:
            weekofyear = st.number_input("Week of Year", min_value=1,    max_value=52,   value=int(now.isocalendar()[1]))
        with col7:
            month      = st.number_input("Month",        min_value=1,    max_value=12,   value=now.month)
        with col8:
            year       = st.number_input("Year",         min_value=2000, max_value=2100, value=now.year)

        submitted = st.form_submit_button("🔮 Get Prediction", use_container_width=True)

    if submitted:
        with st.spinner("Generating sales forecast..."):
            result = make_prediction(
                lag_1, lag_2, lag_4, lag_8, lag_12, lag_26, lag_52,
                ma_4, ma_12, std_4, weekofyear, month, year
            )

        if result["success"]:
            prediction = result["prediction"]
            formatted  = f"${prediction:,.2f}"

            st.success(f"✅ Predicted Next-Week Sales: **{formatted}**")

            # Contextual interpretation — addresses M4 feedback
            if lag_1 > 1_000_000:
                pct_change = ((prediction - lag_1) / lag_1) * 100
                direction  = "above" if pct_change >= 0 else "below"

                # Colour-coded banner
                abs_change = abs(pct_change)
                if abs_change <= 5:
                    st.success(f"🟢 Stable week ahead — Forecast is {abs_change:.1f}% {direction} last week. Continue routine inventory and staffing.")
                elif pct_change > 5:
                    st.warning(f"🟡 Higher demand expected — Forecast is {abs_change:.1f}% above last week. Consider increasing inventory and staffing.")
                else:
                    st.info(f"🔵 Lower demand expected — Forecast is {abs_change:.1f}% below last week. Consider reducing perishable orders.")

                st.info(
                    f"📊 This forecast is **{abs_change:.1f}% {direction}** "
                    f"last week's sales of **${lag_1:,.2f}**. "
                    f"Use this to adjust inventory and staffing for next week."
                )

            st.markdown(f"**Prediction Interval:** {result['confidence']}")

            col1, col2, col3, col4 = st.columns(4)
            with col1:
                st.metric("Forecast",      formatted)
            with col2:
                st.metric("Week",          f"W{weekofyear}")
            with col3:
                st.metric("Model",         "Random Forest")
            with col4:
                st.metric("Response Time", f"{result['response_time_ms']} ms")

            # Save to history
            if "history" not in st.session_state:
                st.session_state.history = []
            st.session_state.history.append({
                "Timestamp":          datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "Week":               weekofyear,
                "Month":              month,
                "Year":               year,
                "Lag 1":              lag_1,
                "Lag 52":             lag_52,
                "Prediction ($)":     round(prediction, 2),
                "Response Time (ms)": result["response_time_ms"]
            })
        else:
            st.error(f"❌ Prediction failed: {result['error']}")

# ══════════════════════════════════════════════════════════════════════════════
# TAB 2 — DASHBOARD
# ══════════════════════════════════════════════════════════════════════════════
with tab2:
    st.markdown("### 📊 Model Performance Dashboard")

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("R2 Score", "0.3025",     help="Higher is better (max 1.0)")
    with col2:
        st.metric("RMSE",     "$2,034,160", help="Root Mean Squared Error")
    with col3:
        st.metric("MAE",      "$1,472,779", help="Mean Absolute Error")
    with col4:
        st.metric("Features", "13",         help="Number of input features")

    st.divider()

    st.markdown("#### 🎯 Feature Importance")
    if model is not None:
        try:
            df_imp = pd.DataFrame({
                "Feature":    model.feature_names_in_.tolist(),
                "Importance": model.feature_importances_.tolist()
            }).sort_values("Importance", ascending=True)

            fig_imp = px.bar(
                df_imp, x="Importance", y="Feature", orientation="h",
                title="Feature Importance — Random Forest",
                color="Importance", color_continuous_scale="blues",
                text="Importance"
            )
            fig_imp.update_traces(texttemplate='%{text:.3f}', textposition='outside')
            fig_imp.update_layout(showlegend=False, height=500)
            st.plotly_chart(fig_imp, use_container_width=True)
        except Exception as e:
            st.info("Feature importance chart unavailable.")

    st.divider()

    st.markdown("#### 📈 Prediction History Chart")
    if "history" in st.session_state and len(st.session_state.history) > 0:
        df_hist  = pd.DataFrame(st.session_state.history)
        fig_hist = px.line(
            df_hist, x="Timestamp", y="Prediction ($)",
            title="Sales Predictions Over Time",
            markers=True, line_shape="spline"
        )
        fig_hist.update_traces(line_color="#1f77b4", marker_size=8)
        fig_hist.update_layout(height=400)
        st.plotly_chart(fig_hist, use_container_width=True)
    else:
        st.info("Make predictions in the Prediction tab to see the chart here.")

    st.divider()

    st.markdown("#### ⚡ Response Time History")
    if "history" in st.session_state and len(st.session_state.history) > 0:
        df_hist = pd.DataFrame(st.session_state.history)
        fig_rt  = px.bar(
            df_hist, x="Timestamp", y="Response Time (ms)",
            title="Model Inference Time per Prediction (ms)",
            color="Response Time (ms)", color_continuous_scale="greens"
        )
        fig_rt.add_hline(y=100, line_dash="dash", line_color="orange",
                         annotation_text="Target < 100ms")
        fig_rt.update_layout(height=350)
        st.plotly_chart(fig_rt, use_container_width=True)
    else:
        st.info("Make predictions to see response time chart.")

# ══════════════════════════════════════════════════════════════════════════════
# TAB 3 — HISTORY
# ══════════════════════════════════════════════════════════════════════════════
with tab3:
    st.markdown("### 📋 Prediction History")

    if "history" in st.session_state and len(st.session_state.history) > 0:
        df_hist = pd.DataFrame(st.session_state.history)

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Predictions", len(df_hist))
        with col2:
            st.metric("Avg Forecast", f"${df_hist['Prediction ($)'].mean():,.2f}")
        with col3:
            st.metric("Max Forecast", f"${df_hist['Prediction ($)'].max():,.2f}")
        with col4:
            st.metric("Min Forecast", f"${df_hist['Prediction ($)'].min():,.2f}")

        st.dataframe(df_hist, use_container_width=True)

        csv = df_hist.to_csv(index=False)
        st.download_button(
            label="📥 Download History as CSV",
            data=csv,
            file_name="predictions_history.csv",
            mime="text/csv"
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
col1, col2, col3 = st.columns(3)
with col1:
    st.caption("AIE1014 Capstone Project")
with col2:
    st.caption(f"Version {VERSION} | Team Dany")
with col3:
    st.caption("Stakeholder: Retail Business Manager")