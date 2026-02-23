import streamlit as st
import pickle
import numpy as np
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="CKD Clinical Decision System",
    page_icon="🏥",
    layout="wide"
)

# ---------------- LOAD MODEL ----------------
model = pickle.load(open("ckd_model.pkl", "rb"))

# ---------------- FEATURE NAMES ----------------
feature_names = [
'age','bp','sg','al','su','rbc','pc','pcc','ba','bgr',
'bu','sc','sod','pot','hemo','pcv','wc','rc',
'htn','dm','cad','appet','pe','ane'
]

# ---------------- PREMIUM HOSPITAL CSS ----------------
st.markdown("""
<style>

/* Main background */
.stApp {
    background: linear-gradient(to right, #f5f9ff, #e6f0ff);
}

/* Header */
.main-title {
    font-size:42px;
    font-weight:700;
    color:#0B3D91;
    text-align:center;
}

.sub-title {
    text-align:center;
    color:#4a4a4a;
    margin-bottom:25px;
}

/* Card styling */
.card {
    background-color:white;
    padding:20px;
    border-radius:15px;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
    margin-bottom:15px;
}

/* Button */
.stButton>button {
    background: linear-gradient(90deg,#0B3D91,#1976D2);
    color:white;
    font-size:18px;
    border-radius:10px;
    padding:10px 28px;
    border:none;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown('<p class="main-title">🏥  Chronic Kidney Disease Prediction</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">AI-powered Chronic Kidney Disease Risk Assessment</p>', unsafe_allow_html=True)

# ---------------- INPUT SECTIONS ----------------
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 🧪 Basic Parameters")
    age = st.number_input("Age", 1, 100, 45)
    bp = st.number_input("Blood Pressure", 50, 180, 80)
    sg = st.selectbox("Specific Gravity", [1.005,1.010,1.015,1.020,1.025])
    al = st.selectbox("Albumin", [0,1,2,3,4,5])
    su = st.selectbox("Sugar", [0,1,2,3,4,5])
    bgr = st.number_input("Blood Glucose Random", 50, 500, 120)
    bu = st.number_input("Blood Urea", 1, 200, 40)
    sc = st.number_input("Serum Creatinine", 0.1, 15.0, 1.2)

with col2:
    st.markdown("### 🧬 Blood Profile")
    sod = st.number_input("Sodium", 100, 200, 140)
    pot = st.number_input("Potassium", 2.0, 10.0, 4.5)
    hemo = st.number_input("Hemoglobin", 3.0, 20.0, 15.0)
    pcv = st.number_input("Packed Cell Volume", 20, 60, 44)
    wc = st.number_input("White Blood Cell Count", 2000, 20000, 8000)
    rc = st.number_input("Red Blood Cell Count", 2.0, 6.5, 5.0)

with col3:
    st.markdown("### 🏥 Clinical Indicators")
    rbc = st.selectbox("Red Blood Cells", ["normal","abnormal"])
    pc = st.selectbox("Pus Cell", ["normal","abnormal"])
    pcc = st.selectbox("Pus Cell Clumps", ["present","notpresent"])
    ba = st.selectbox("Bacteria", ["present","notpresent"])
    htn = st.selectbox("Hypertension", ["yes","no"])
    dm = st.selectbox("Diabetes Mellitus", ["yes","no"])
    cad = st.selectbox("Coronary Artery Disease", ["yes","no"])
    appet = st.selectbox("Appetite", ["good","poor"])
    pe = st.selectbox("Pedal Edema", ["yes","no"])
    ane = st.selectbox("Anemia", ["yes","no"])

# ---------------- ENCODER ----------------
def encode_binary(val, pos):
    return 1 if val == pos else 0

st.markdown("---")

# ---------------- PREDICTION ----------------
if st.button("🔍 Predict"):

    input_data = np.array([[
        age, bp, sg, al, su,
        encode_binary(rbc,"abnormal"),
        encode_binary(pc,"abnormal"),
        encode_binary(pcc,"present"),
        encode_binary(ba,"present"),
        bgr, bu, sc, sod, pot,
        hemo, pcv, wc, rc,
        encode_binary(htn,"yes"),
        encode_binary(dm,"yes"),
        encode_binary(cad,"yes"),
        encode_binary(appet,"poor"),
        encode_binary(pe,"yes"),
        encode_binary(ane,"yes")
    ]])

    prediction = model.predict(input_data)
    prob = model.predict_proba(input_data)[0][1]
    risk_percent = round(prob*100,2)

    st.markdown("## 🧾 Clinical Result")

    if prediction[0] == 1:
        st.error(f"⚠️ CKD Detected")
        st.warning(f"🔴 Risk Probability: {risk_percent}%")
    else:
        st.success("✅ No CKD Detected")
        st.info(f"🟢 Risk Probability: {risk_percent}%")

    # download report
    report = pd.DataFrame({
        "Parameter": feature_names,
        "Value": input_data.flatten()
    })

    st.download_button(
        "📥 Download Clinical Report",
        report.to_csv(index=False),
        file_name="ckd_clinical_report.csv",
        mime="text/csv"
    )

# ---------------- FOOTER ----------------
st.markdown("---")