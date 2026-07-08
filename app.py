import streamlit as st
import pickle
import numpy as np

# Load saved model
model = pickle.load(open('crop_model.pkl', 'rb'))

# ── MAIN PAGE ─────────────────────────────────────────────
st.title("🌾 AgroMind — Crop Recommendation System")
st.write("Enter your soil and weather details in the **sidebar** on the left.")

# ── SIDEBAR INPUTS ────────────────────────────────────────
st.sidebar.title("🧪 Input Parameters")
st.sidebar.markdown("---")

st.sidebar.markdown("**🌿 Soil Nutrients**")
st.sidebar.caption("Nitrogen (N) — Range: 0 to 140 kg/ha")
N = st.sidebar.number_input("Nitrogen (N)", min_value=0, max_value=140, value=0)

st.sidebar.caption("Phosphorus (P) — Range: 0 to 145 kg/ha")
P = st.sidebar.number_input("Phosphorus (P)", min_value=0, max_value=145, value=0)

st.sidebar.caption("Potassium (K) — Range: 0 to 205 kg/ha")
K = st.sidebar.number_input("Potassium (K)", min_value=0, max_value=205, value=0)

st.sidebar.caption("Soil pH — Range: 0.0 to 14.0")
ph = st.sidebar.number_input("Soil pH", min_value=0.0, max_value=14.0, value=0.0)

st.sidebar.markdown("---")
st.sidebar.markdown("**🌦️ Weather Conditions**")

st.sidebar.caption("Temperature — Range: 0.0 to 50.0 °C")
temp = st.sidebar.number_input("Temperature (°C)", min_value=0.0, max_value=50.0, value=0.0)

st.sidebar.caption("Humidity — Range: 0.0 to 100.0 %")
humidity = st.sidebar.number_input("Humidity (%)", min_value=0.0, max_value=100.0, value=0.0)

st.sidebar.caption("Rainfall — Range: 0.0 to 300.0 mm")
rainfall = st.sidebar.number_input("Rainfall (mm)", min_value=0.0, max_value=300.0, value=0.0)

st.sidebar.markdown("---")


# ── SHOW INPUT SUMMARY ON MAIN PAGE ──────────────────────
st.subheader("📋 Your Entered Values")
col1, col2 = st.columns(2)

with col1:
    st.metric("Nitrogen (N)",    f"{N} kg/ha")
    st.metric("Phosphorus (P)",  f"{P} kg/ha")
    st.metric("Potassium (K)",   f"{K} kg/ha")
    st.metric("Soil pH",         f"{ph}")

with col2:
    st.metric("Temperature",     f"{temp} °C")
    st.metric("Humidity",        f"{humidity} %")
    st.metric("Rainfall",        f"{rainfall} mm")

st.markdown("---")


# ── VALIDATION FUNCTION ───────────────────────────────────
def validate_inputs(N, P, K, temp, humidity, ph, rainfall):
    errors = []

    if N == 0 and P == 0 and K == 0 and temp == 0 and humidity == 0 and ph == 0 and rainfall == 0:
        errors.append("❌ All values are zero. Please enter actual soil and weather values.")
        return errors

    if temp < 5:
        errors.append("❌ Temperature too low (below 5°C). No common crop grows in such conditions.")
    if temp > 45:
        errors.append("❌ Temperature too high (above 45°C). No crop grows in such extreme heat.")
    if humidity < 10:
        errors.append("❌ Humidity too low (below 10%). Please enter a realistic value.")
    if ph < 3.5:
        errors.append("❌ Soil pH too acidic (below 3.5). No crop grows in such conditions.")
    if ph > 9.5:
        errors.append("❌ Soil pH too alkaline (above 9.5). No crop grows in such conditions.")
    if rainfall < 15:
        errors.append("❌ Rainfall too low (below 15mm). Please enter a valid rainfall value.")

    return errors


# ── CROP CONDITION VALIDATION ─────────────────────────────
def validate_crop_conditions(crop, temp, humidity, rainfall, ph):
    warnings = []
    crop = crop.lower()

    if crop == "apple":
        if temp > 25:
            warnings.append(f"⚠️ Apple grows in cold climates (7°C–25°C). Your temperature ({temp}°C) is too high.")
        if rainfall < 100:
            warnings.append(f"⚠️ Apple needs moderate rainfall (100mm+). Your rainfall ({rainfall}mm) is low.")
    elif crop == "rice":
        if rainfall < 150:
            warnings.append(f"⚠️ Rice needs high rainfall (150mm+). Your rainfall ({rainfall}mm) is low.")
        if humidity < 60:
            warnings.append(f"⚠️ Rice needs high humidity (60%+). Your humidity ({humidity}%) is low.")
    elif crop == "cotton":
        if temp < 20:
            warnings.append(f"⚠️ Cotton grows best in warm conditions (20°C+). Your temperature ({temp}°C) is low.")
        if rainfall > 150:
            warnings.append(f"⚠️ Cotton prefers low to moderate rainfall. Your rainfall ({rainfall}mm) is too high.")
    elif crop == "mango":
        if temp < 20:
            warnings.append(f"⚠️ Mango grows in hot climates (20°C+). Your temperature ({temp}°C) is too low.")
        if humidity > 90:
            warnings.append(f"⚠️ Mango does not prefer very high humidity ({humidity}%).")
    elif crop == "grapes":
        if temp > 35:
            warnings.append(f"⚠️ Grapes prefer moderate temperature (15°C–35°C). Your temperature ({temp}°C) is too high.")
    elif crop == "coconut":
        if temp < 22:
            warnings.append(f"⚠️ Coconut grows in tropical climates (22°C+). Your temperature ({temp}°C) is low.")
        if rainfall < 100:
            warnings.append(f"⚠️ Coconut needs good rainfall (100mm+). Your rainfall ({rainfall}mm) is low.")
    elif crop == "coffee":
        if temp > 35:
            warnings.append(f"⚠️ Coffee grows in mild climates (15°C–30°C). Your temperature ({temp}°C) is too high.")
        if humidity < 50:
            warnings.append(f"⚠️ Coffee needs moderate humidity (50%+). Your humidity ({humidity}%) is low.")
    elif crop == "wheat":
        if temp > 30:
            warnings.append(f"⚠️ Wheat prefers cool climates (10°C–25°C). Your temperature ({temp}°C) is too high.")
    elif crop == "maize":
        if temp < 15:
            warnings.append(f"⚠️ Maize grows best above 15°C. Your temperature ({temp}°C) is too low.")
    elif crop == "chickpea":
        if rainfall > 150:
            warnings.append(f"⚠️ Chickpea prefers dry conditions. Your rainfall ({rainfall}mm) is too high.")
        if temp > 35:
            warnings.append(f"⚠️ Chickpea prefers cooler temperatures. Your temperature ({temp}°C) is too high.")
    elif crop == "banana":
        if temp < 20:
            warnings.append(f"⚠️ Banana grows in tropical climates (20°C+). Your temperature ({temp}°C) is low.")
        if humidity < 60:
            warnings.append(f"⚠️ Banana needs high humidity (60%+). Your humidity ({humidity}%) is low.")

    return warnings


# ── PREDICT BUTTON ────────────────────────────────────────
if st.button("🌱 Recommend Crop"):

    errors = validate_inputs(N, P, K, temp, humidity, ph, rainfall)

    if errors:
        for error in errors:
            st.error(error)

    else:
        input_data = np.array([[N, P, K, temp, humidity, ph, rainfall]])
        result = model.predict(input_data)
        crop_name = result[0]

        warnings = validate_crop_conditions(crop_name, temp, humidity, rainfall, ph)

        if warnings:
            st.warning(f"🌾 Model predicted: **{crop_name.upper()}** — but inputs may not be realistic:")
            for w in warnings:
                st.warning(w)
            st.info("💡 Please re-check your values in the sidebar and try again.")
        else:
            st.success(f"✅ Best Crop to Grow: **{crop_name.upper()}**")
            st.balloons()