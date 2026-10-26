import streamlit as st

st.set_page_config(page_title="Advanced Metabolic Pathology Simulator", layout="centered")

st.title("🧬 Advanced Metabolic Pathology Simulator")
st.caption("Multifactorial Disease Modeling: Genetics × Environmental Load")
st.markdown("---")

# Section 1: Comprehensive Genetics
st.subheader("1. Genetic Susceptibility & Family History")
genetics = st.selectbox(
    "Polygenic Risk Score / Family Load:",
    [
        "Low (No family history / Protected variants)",
        "Moderate (Single parent with T2DM / Minor risk alleles)",
        "High (Both parents / Strong polygenic load & thrifty phenotype)"
    ]
)

# Section 2: Comprehensive Lifestyle & Environmental Load
st.subheader("2. Environmental & Lifestyle Load")

col1, col2 = st.columns(2)

with col1:
    exercise = st.slider("Weekly Physical Activity (Days/Week):", 0, 7, 2)
    diet = st.selectbox(
        "Dietary Pattern & Glycemic Index:",
        [
            "Balanced & High Fiber (Low Glycemic)",
            "Moderate / Standard Western Diet",
            "High Refined Sugars, Fructose & Processed Foods"
        ]
    )

with col2:
    sleep = st.selectbox(
        "Sleep Quality & Circadian Rhythm:",
        ["Good (7-8 hours, regular)", "Moderate (Chronic mild sleep restriction)", "Poor / Shift Work (Circadian Disruption)"]
    )
    stress = st.selectbox(
        "Chronic Psychosocial Stress (Cortisol Load):",
        ["Low", "Moderate", "High (Sustained HPA-axis activation)"]
    )

# Section 3: Additional Clinical / Environmental Factors
st.subheader("3. Secondary Pathology Load")
smoking = st.radio("High Oxidative Stress / Smoking / Vaping?", ["No", "Yes"])
visceral_fat = st.slider("Visceral Adiposity Level (Proxy for Low-grade Inflammation):", 1, 10, 3)

# Advanced Calculation Logic for Pathological Risk
score = 10

# Genetic weighting
if "Moderate" in genetics: score += 25
elif "High" in genetics: score += 50

# Lifestyle & Diet weighting
score -= (exercise * 5) # Exercise is protective

if "Moderate / Standard" in diet: score += 15
elif "High Refined" in diet: score += 30

if "Moderate" in sleep: score += 10
elif "Poor" in sleep: score += 20

if "Moderate" in stress: score += 10
elif "High" in stress: score += 20

if smoking == "Yes": score += 15
score += (visceral_fat * 3)

final_risk = max(5, min(100, score))

# Output Section
st.markdown("---")
st.subheader("📊 Cellular Pathology & Metabolic Fate Dashboard")

st.progress(final_risk / 100)
st.metric(label="Calculated Insulin Resistance & Beta-Cell Apoptosis Risk", value=f"{final_risk}%")

if final_risk < 30:
    st.success("🟢 **Homeostasis Maintained:** High insulin sensitivity and robust beta-cell compensation. Metabolic equilibrium is stable.")
elif final_risk < 65:
    st.warning("🟡 **Compensated Resistance:** Chronic low-grade inflammation, receptor downregulation, and compensatory hyperinsulinemia. Early beta-cell strain.")
else:
    st.error("🔴 **Critical Pathology (Point of No Return):** Severe receptor failure, glucolipotoxicity, and irreversible Beta-cell Apoptosis leading to overt Type 2 Diabetes.")
