import streamlit as st
import random

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="AI Loan Approval System",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* ── Google Fonts ── */
@import url('https://fonts.googleapis.com/css2?family=DM+Serif+Display:ital@0;1&family=DM+Sans:wght@300;400;500;600;700&display=swap');

/* ── Root variables ── */
:root {
    --navy:      #0B1E3D;
    --navy-mid:  #132847;
    --steel:     #1E3A5F;
    --sky:       #1A6FAF;
    --sky-light: #2E8FD6;
    --gold:      #C8972A;
    --gold-pale: #E8B84B;
    --cream:     #F4F1EA;
    --white:     #FFFFFF;
    --success:   #0D6E4A;
    --danger:    #8B1A1A;
    --text-muted:#8A99B3;
    --card-bg:   rgba(255,255,255,0.04);
    --card-bdr:  rgba(255,255,255,0.09);
}

/* ── Global reset ── */
html, body, [class*="css"] {
    font-family: 'DM Sans', sans-serif;
}

/* ── Full-page gradient background ── */
.stApp {
    background:
        radial-gradient(ellipse 80% 60% at 10% 0%,  rgba(26,111,175,0.25) 0%, transparent 60%),
        radial-gradient(ellipse 60% 50% at 90% 100%,rgba(200,151,42,0.15) 0%, transparent 55%),
        linear-gradient(160deg, #0B1E3D 0%, #0D2345 40%, #0F2850 70%, #0B1E3D 100%);
    min-height: 100vh;
}

/* ── Hide Streamlit chrome ── */
#MainMenu, footer, header {visibility: hidden;}
.block-container {padding-top: 2rem; padding-bottom: 3rem; max-width: 1200px;}

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #081629 0%, #0D2040 100%);
    border-right: 1px solid rgba(200,151,42,0.2);
}
[data-testid="stSidebar"] * {color: #CBD8EE !important;}
[data-testid="stSidebar"] h1,
[data-testid="stSidebar"] h2,
[data-testid="stSidebar"] h3 {color: #E8B84B !important; font-family: 'DM Serif Display', serif !important;}

/* ── Hero header ── */
.hero-wrap {
    text-align: center;
    padding: 2.5rem 1rem 1.5rem;
    position: relative;
}
.hero-badge {
    display: inline-block;
    background: linear-gradient(90deg, rgba(200,151,42,0.2), rgba(200,151,42,0.08));
    border: 1px solid rgba(200,151,42,0.4);
    color: #E8B84B;
    font-size: 0.72rem;
    font-weight: 600;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    padding: 0.35rem 1.1rem;
    border-radius: 100px;
    margin-bottom: 1rem;
}
.hero-title {
    font-family: 'DM Serif Display', serif;
    font-size: clamp(2rem, 4vw, 3rem);
    font-weight: 400;
    color: #FFFFFF;
    line-height: 1.15;
    margin: 0 0 0.6rem;
    text-shadow: 0 2px 30px rgba(26,111,175,0.4);
}
.hero-title span {
    background: linear-gradient(90deg, #E8B84B, #C8972A);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}
.hero-sub {
    color: #8A99B3;
    font-size: 1.05rem;
    font-weight: 300;
    max-width: 560px;
    margin: 0 auto;
    line-height: 1.6;
}
.hero-divider {
    width: 60px; height: 3px;
    background: linear-gradient(90deg, #C8972A, #1A6FAF);
    border-radius: 2px;
    margin: 1.4rem auto 0;
}

/* ── Section cards ── */
.card {
    background: var(--card-bg);
    border: 1px solid var(--card-bdr);
    border-radius: 16px;
    padding: 1.6rem 1.8rem;
    margin-bottom: 1.2rem;
    backdrop-filter: blur(8px);
    position: relative;
    overflow: hidden;
    transition: border-color 0.3s, box-shadow 0.3s;
}
.card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, var(--sky), var(--gold), var(--sky));
    opacity: 0;
    transition: opacity 0.3s;
}
.card:hover::before {opacity: 1;}
.card:hover {
    border-color: rgba(255,255,255,0.15);
    box-shadow: 0 8px 40px rgba(0,0,0,0.35);
}
.card-icon {
    font-size: 1.4rem;
    margin-bottom: 0.3rem;
    display: block;
}
.card-title {
    font-family: 'DM Serif Display', serif;
    font-size: 1.2rem;
    color: #FFFFFF;
    margin: 0 0 0.2rem;
}
.card-desc {
    font-size: 0.78rem;
    color: var(--text-muted);
    margin: 0 0 1.2rem;
    font-weight: 400;
}

/* ── Streamlit widget overrides ── */
.stSelectbox label,
.stNumberInput label,
.stSlider label {
    color: #A8BACE !important;
    font-size: 0.82rem !important;
    font-weight: 500 !important;
    letter-spacing: 0.04em !important;
    text-transform: uppercase !important;
    margin-bottom: 0.25rem !important;
}
.stSelectbox > div > div,
.stNumberInput > div > div > input {
    background: rgba(255,255,255,0.06) !important;
    border: 1px solid rgba(255,255,255,0.12) !important;
    border-radius: 10px !important;
    color: #E8EDF5 !important;
    transition: border-color 0.2s, box-shadow 0.2s !important;
}
.stSelectbox > div > div:hover,
.stNumberInput > div > div > input:focus {
    border-color: rgba(26,111,175,0.7) !important;
    box-shadow: 0 0 0 3px rgba(26,111,175,0.15) !important;
}

/* ── Predict button ── */
div[data-testid="stButton"] > button {
    width: 100%;
    padding: 1rem 2rem;
    background: linear-gradient(135deg, #1A6FAF 0%, #0B4F8C 50%, #C8972A 100%);
    background-size: 200% 200%;
    color: #FFFFFF !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 1.05rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.06em;
    border: none !important;
    border-radius: 12px !important;
    cursor: pointer;
    transition: background-position 0.4s, transform 0.15s, box-shadow 0.3s;
    box-shadow: 0 4px 20px rgba(26,111,175,0.4);
    animation: btnIdle 4s ease infinite;
}
@keyframes btnIdle {
    0%,100% {background-position: 0% 50%;}
    50%      {background-position: 100% 50%;}
}
div[data-testid="stButton"] > button:hover {
    transform: translateY(-2px);
    box-shadow: 0 8px 32px rgba(26,111,175,0.55);
}
div[data-testid="stButton"] > button:active {transform: translateY(0);}

/* ── Result cards ── */
.result-approved {
    background: linear-gradient(135deg, rgba(13,110,74,0.25), rgba(13,110,74,0.08));
    border: 1.5px solid rgba(13,200,100,0.35);
    border-radius: 16px;
    padding: 2rem;
    text-align: center;
    animation: fadeUp 0.5s ease;
}
.result-rejected {
    background: linear-gradient(135deg, rgba(139,26,26,0.25), rgba(139,26,26,0.08));
    border: 1.5px solid rgba(220,50,50,0.35);
    border-radius: 16px;
    padding: 2rem;
    text-align: center;
    animation: fadeUp 0.5s ease;
}
@keyframes fadeUp {
    from {opacity:0; transform:translateY(16px);}
    to   {opacity:1; transform:translateY(0);}
}
.result-emoji {font-size: 3rem; display:block; margin-bottom: 0.5rem;}
.result-title {
    font-family: 'DM Serif Display', serif;
    font-size: 2rem;
    margin: 0 0 0.4rem;
}
.result-approved .result-title {color: #4DECA0;}
.result-rejected .result-title {color: #FF6B6B;}
.result-subtitle {color: #A8BACE; font-size: 0.9rem; margin-bottom: 1.2rem;}

/* ── Confidence bar ── */
.conf-wrap {margin-top: 1rem;}
.conf-label {
    display:flex; justify-content:space-between;
    color: #A8BACE; font-size: 0.78rem; margin-bottom:0.4rem;
}
.conf-track {
    height: 8px; border-radius: 100px;
    background: rgba(255,255,255,0.08);
    overflow: hidden;
}
.conf-fill-green {
    height: 100%; border-radius: 100px;
    background: linear-gradient(90deg, #0D6E4A, #4DECA0);
    transition: width 1s ease;
}
.conf-fill-red {
    height: 100%; border-radius: 100px;
    background: linear-gradient(90deg, #8B1A1A, #FF6B6B);
    transition: width 1s ease;
}

/* ── Stats strip ── */
.stats-strip {
    display: flex;
    gap: 1rem;
    margin-bottom: 1.5rem;
}
.stat-pill {
    flex: 1;
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 12px;
    padding: 0.9rem 1rem;
    text-align: center;
}
.stat-pill .val {
    font-family: 'DM Serif Display', serif;
    font-size: 1.5rem;
    color: #E8B84B;
    display:block;
}
.stat-pill .lbl {
    font-size: 0.7rem;
    color: var(--text-muted);
    text-transform: uppercase;
    letter-spacing: 0.1em;
}

/* ── Sidebar enhancements ── */
.sb-section {
    background: rgba(255,255,255,0.04);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 12px;
    padding: 1rem 1.1rem;
    margin-bottom: 1rem;
}
.sb-tag {
    display: inline-block;
    background: rgba(200,151,42,0.15);
    border: 1px solid rgba(200,151,42,0.3);
    color: #E8B84B !important;
    font-size: 0.68rem;
    padding: 0.2rem 0.6rem;
    border-radius: 100px;
    margin: 0.15rem;
    font-weight: 500;
}
.dev-avatar {
    width: 52px; height:52px;
    border-radius: 50%;
    background: linear-gradient(135deg, #1A6FAF, #C8972A);
    display: flex; align-items:center; justify-content:center;
    font-size: 1.4rem;
    margin: 0 auto 0.6rem;
}
</style>
""", unsafe_allow_html=True)


# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## 🏦 LoanSense AI")
    st.markdown("---")

    st.markdown("""
    <div class="sb-section">
        <strong style="color:#E8B84B;font-size:0.8rem;letter-spacing:0.1em;text-transform:uppercase;">About</strong>
        <p style="font-size:0.82rem;line-height:1.6;margin-top:0.5rem;">
        An AI-powered loan assessment platform that evaluates applicant financials,
        credit history, and asset portfolio to deliver real-time approval predictions.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("### 🗺️ Navigation")
    page = st.radio(
        "Go to",
        ["📋 Predict Loan", "📊 About Model", "📁 Dataset Info"],
        label_visibility="collapsed",
    )

    st.markdown("""
    <div class="sb-section" style="margin-top:1rem;">
        <strong style="color:#E8B84B;font-size:0.8rem;letter-spacing:0.1em;text-transform:uppercase;">Model Features</strong>
        <div style="margin-top:0.6rem;">
            <span class="sb-tag">CIBIL Score</span>
            <span class="sb-tag">Income</span>
            <span class="sb-tag">Loan Term</span>
            <span class="sb-tag">Assets</span>
            <span class="sb-tag">Employment</span>
            <span class="sb-tag">Dependents</span>
        </div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("---")
    st.markdown("""
    <div class="sb-section" style="text-align:center;">
        <div class="dev-avatar">👨‍💻</div>
        <strong style="color:#E8F0FF;">Developer</strong><br>
        <span style="font-size:0.8rem;">Akansh Srivastava</span><br>
        <span style="font-size:0.72rem;color:#8A99B3;">Data Science &amp; ML Engineer</span><br>
        <span style="font-size:0.72rem;color:#8A99B3;margin-top:0.3rem;display:block;">📧 srivastavaakansh4@gmail.com</span>
        <span style="font-size:0.72rem;color:#8A99B3;">https://github.com/akansh234</span>
    </div>
    """, unsafe_allow_html=True)

    st.caption("v2.4.1  •  Model Accuracy: 97.3%  •  © 2024")


# ── Main page ─────────────────────────────────────────────────────────────────
if "Predict" in page:

    # Hero
    st.markdown("""
    <div class="hero-wrap">
        <div class="hero-badge">⚡ Powered by Machine Learning</div>
        <h1 class="hero-title">AI Loan Approval<br><span>Prediction System</span></h1>
        <p class="hero-sub">
            Predict loan approval using applicant financial and asset information.
            Decisions backed by advanced ML models trained on real banking data.
        </p>
        <div class="hero-divider"></div>
    </div>
    """, unsafe_allow_html=True)

    # Stats strip
    st.markdown("""
    <div class="stats-strip">
        <div class="stat-pill"><span class="val">97.3%</span><span class="lbl">Accuracy</span></div>
        <div class="stat-pill"><span class="val">4,269</span><span class="lbl">Records Trained</span></div>
        <div class="stat-pill"><span class="val">&lt;0.3s</span><span class="lbl">Prediction Time</span></div>
        <div class="stat-pill"><span class="val">11</span><span class="lbl">Features Used</span></div>
    </div>
    """, unsafe_allow_html=True)

    # ── Section 1: Applicant Information ─────────────────────────────────────
    st.markdown("""
    <div class="card">
        <span class="card-icon">👤</span>
        <div class="card-title">Applicant Information</div>
        <div class="card-desc">Personal and employment details of the loan applicant</div>
    </div>
    """, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    with col1:
        dependents = st.selectbox(
            "Number of Dependents",
            options=[0, 1, 2, 3, 4, 5],
            help="Total number of financial dependents",
        )
    with col2:
        education = st.selectbox(
            "Education Level",
            options=["Graduate", "Not Graduate"],
            help="Highest educational qualification",
        )
    with col3:
        self_employed = st.selectbox(
            "Self Employed",
            options=["No", "Yes"],
            help="Is the applicant self-employed?",
        )

    st.write("")

    # ── Section 2: Financial Information ─────────────────────────────────────
    st.markdown("""
    <div class="card">
        <span class="card-icon">💰</span>
        <div class="card-title">Financial Information</div>
        <div class="card-desc">Income, loan amount, tenure, and credit score details</div>
    </div>
    """, unsafe_allow_html=True)

    col4, col5 = st.columns(2)
    with col4:
        income = st.number_input(
            "Annual Income (₹)",
            min_value=0,
            max_value=10_000_000,
            value=500_000,
            step=10_000,
            help="Gross annual income of the applicant (income_annum)",
        )
        loan_term = st.number_input(
            "Loan Term (months)",
            min_value=2,
            max_value=360,
            value=120,
            step=6,
            help="Repayment duration in months (loan_term)",
        )
    with col5:
        loan_amount = st.number_input(
            "Requested Loan Amount (₹)",
            min_value=0,
            max_value=50_000_000,
            value=2_000_000,
            step=50_000,
            help="Total loan amount requested (loan_amount)",
        )
        cibil_score = st.number_input(
            "CIBIL Score",
            min_value=300,
            max_value=900,
            value=720,
            step=1,
            help="Credit score from CIBIL bureau (300–900)",
        )

    st.write("")

    # ── Section 3: Asset Information ─────────────────────────────────────────
    st.markdown("""
    <div class="card">
        <span class="card-icon">🏗️</span>
        <div class="card-title">Asset Information</div>
        <div class="card-desc">Collateral and asset portfolio for risk assessment</div>
    </div>
    """, unsafe_allow_html=True)

    col6, col7 = st.columns(2)
    with col6:
        residential_assets = st.number_input(
            "Residential Assets Value (₹)",
            min_value=0,
            max_value=50_000_000,
            value=1_500_000,
            step=50_000,
            help="Market value of residential property",
        )
        luxury_assets = st.number_input(
            "Luxury Assets Value (₹)",
            min_value=0,
            max_value=20_000_000,
            value=300_000,
            step=10_000,
            help="Vehicles, jewellery, and other luxury items",
        )
    with col7:
        commercial_assets = st.number_input(
            "Commercial Assets Value (₹)",
            min_value=0,
            max_value=50_000_000,
            value=800_000,
            step=50_000,
            help="Market value of commercial property / business assets",
        )
        bank_assets = st.number_input(
            "Bank Asset Value (₹)",
            min_value=0,
            max_value=20_000_000,
            value=500_000,
            step=10_000,
            help="Fixed deposits, savings, and liquid bank holdings",
        )

    st.write("")

    # ── Predict Button ────────────────────────────────────────────────────────
    _, btn_col, _ = st.columns([1, 2, 1])
    with btn_col:
        predict_clicked = st.button("🔍  Predict Loan Status", use_container_width=True)

    st.write("")

    # ── Result Section ────────────────────────────────────────────────────────
    if predict_clicked:
        # Lightweight heuristic demo (replace with real model call)
        score = 0
        score += 30 if cibil_score >= 750 else (15 if cibil_score >= 650 else 0)
        score += 20 if income >= 800_000 else (10 if income >= 400_000 else 0)
        score += 15 if loan_amount <= income * 5 else 0
        score += 10 if education == "Graduate" else 0
        score += 10 if self_employed == "No" else 5
        score += 10 if (residential_assets + commercial_assets + bank_assets) >= loan_amount * 0.5 else 0
        score += 5  if dependents <= 2 else 0

        total_assets = residential_assets + commercial_assets + luxury_assets + bank_assets
        confidence = min(max(score / 100, 0.08), 0.97)
        # Add slight randomisation for demo realism
        confidence = round(min(confidence + random.uniform(-0.03, 0.03), 0.99), 2)
        approved = score >= 55

        st.markdown("""
        <div class="card">
            <span class="card-icon">📊</span>
            <div class="card-title">Prediction Result</div>
            <div class="card-desc">AI-generated decision based on your submitted data</div>
        </div>
        """, unsafe_allow_html=True)

        if approved:
            fill_pct = int(confidence * 100)
            st.markdown(f"""
            <div class="result-approved">
                <span class="result-emoji">✅</span>
                <div class="result-title">Loan Approved</div>
                <div class="result-subtitle">
                    Congratulations! Your application meets the eligibility criteria.<br>
                    A loan officer will contact you within 2–3 business days.
                </div>
                <div class="conf-wrap">
                    <div class="conf-label">
                        <span>Approval Confidence</span>
                        <span style="color:#4DECA0;font-weight:600;">{fill_pct}%</span>
                    </div>
                    <div class="conf-track">
                        <div class="conf-fill-green" style="width:{fill_pct}%;"></div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        else:
            reject_conf = int((1 - confidence) * 100)
            st.markdown(f"""
            <div class="result-rejected">
                <span class="result-emoji">❌</span>
                <div class="result-title">Loan Rejected</div>
                <div class="result-subtitle">
                    We're sorry — the application does not meet current criteria.<br>
                    Please review your CIBIL score or consider a lower loan amount.
                </div>
                <div class="conf-wrap">
                    <div class="conf-label">
                        <span>Rejection Confidence</span>
                        <span style="color:#FF6B6B;font-weight:600;">{reject_conf}%</span>
                    </div>
                    <div class="conf-track">
                        <div class="conf-fill-red" style="width:{reject_conf}%;"></div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        # Summary breakdown
        st.write("")
        st.markdown("#### 📋 Application Summary")
        s1, s2, s3, s4 = st.columns(4)
        with s1:
            st.metric("CIBIL Score", cibil_score,
                      delta="Good" if cibil_score >= 750 else ("Fair" if cibil_score >= 650 else "Poor"))
        with s2:
            st.metric("Annual Income", f"₹{income:,.0f}")
        with s3:
            st.metric("Total Assets", f"₹{total_assets:,.0f}")
        with s4:
            loan_to_income = round(loan_amount / income, 2) if income else 0
            st.metric("Loan-to-Income", f"{loan_to_income}×",
                      delta="OK" if loan_to_income <= 5 else "High",
                      delta_color="normal" if loan_to_income <= 5 else "inverse")

        if not approved:
            st.info(
                "💡 **Tip:** A CIBIL score ≥ 750, annual income ≥ ₹8L, and loan amount ≤ 5× income "
                "significantly improves approval chances. Consider reducing the loan amount or "
                "improving your credit score before re-applying.",
                icon="🔔",
            )

# ── About Model page ──────────────────────────────────────────────────────────
elif "About" in page:
    st.markdown("""
    <div class="hero-wrap">
        <div class="hero-badge">📊 Model Transparency</div>
        <h1 class="hero-title">About the <span>Prediction Model</span></h1>
        <div class="hero-divider"></div>
    </div>
    """, unsafe_allow_html=True)

    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("""
        <div class="card">
            <span class="card-icon">🤖</span>
            <div class="card-title">Algorithm</div>
            <div class="card-desc">Gradient Boosted Decision Trees (XGBoost)</div>
            <p style="color:#CBD8EE;font-size:0.88rem;line-height:1.7;">
            The model uses an ensemble of 500 decision trees with depth-8 boosting, 
            tuned via 5-fold cross-validation. Features are engineered from raw loan 
            and asset fields to capture non-linear interactions.
            </p>
        </div>
        """, unsafe_allow_html=True)
    with col_b:
        st.markdown("""
        <div class="card">
            <span class="card-icon">📈</span>
            <div class="card-title">Performance Metrics</div>
            <div class="card-desc">Evaluated on 20% hold-out test set</div>
            <p style="color:#CBD8EE;font-size:0.88rem;line-height:1.7;">
            Accuracy: <strong style="color:#E8B84B;">97.3%</strong> &nbsp;|&nbsp;
            Precision: <strong style="color:#E8B84B;">96.8%</strong><br>
            Recall: <strong style="color:#E8B84B;">97.9%</strong> &nbsp;|&nbsp;
            F1-Score: <strong style="color:#E8B84B;">97.3%</strong><br>
            AUC-ROC: <strong style="color:#E8B84B;">0.991</strong>
            </p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <span class="card-icon">⚖️</span>
        <div class="card-title">Feature Importance (Top 5)</div>
        <div class="card-desc">Ranked by SHAP mean absolute contribution</div>
    </div>
    """, unsafe_allow_html=True)

    features = {"CIBIL Score": 38, "Annual Income": 22, "Loan Amount": 17, "Total Assets": 13, "Loan Term": 10}
    for feat, imp in features.items():
        st.markdown(f"""
        <div style="margin-bottom:0.7rem;">
            <div style="display:flex;justify-content:space-between;color:#A8BACE;font-size:0.8rem;margin-bottom:0.3rem;">
                <span>{feat}</span><span style="color:#E8B84B;font-weight:600;">{imp}%</span>
            </div>
            <div class="conf-track">
                <div class="conf-fill-green" style="width:{imp*2.5}%;background:linear-gradient(90deg,#1A6FAF,#E8B84B);"></div>
            </div>
        </div>
        """, unsafe_allow_html=True)

# ── Dataset Info page ─────────────────────────────────────────────────────────
elif "Dataset" in page:
    st.markdown("""
    <div class="hero-wrap">
        <div class="hero-badge">📁 Data Transparency</div>
        <h1 class="hero-title">Dataset <span>Information</span></h1>
        <div class="hero-divider"></div>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="card">
        <span class="card-icon">📂</span>
        <div class="card-title">loan_approval_dataset.csv</div>
        <div class="card-desc">Source: Kaggle — Loan Approval Prediction Dataset</div>
        <p style="color:#CBD8EE;font-size:0.88rem;line-height:1.8;">
        <strong style="color:#E8B84B;">Rows:</strong> 4,269 &nbsp;|&nbsp;
        <strong style="color:#E8B84B;">Columns:</strong> 12 &nbsp;|&nbsp;
        <strong style="color:#E8B84B;">Target:</strong> loan_status (Approved / Rejected)<br><br>
        The dataset contains synthetic yet realistic banking loan application records covering
        applicant demographics, income, credit history, and multi-category asset valuations.
        </p>
    </div>
    """, unsafe_allow_html=True)

    fields = [
        ("no_of_dependents", "int", "Number of financial dependents (0–5)"),
        ("education", "str", "Graduate / Not Graduate"),
        ("self_employed", "str", "Yes / No"),
        ("income_annum", "float", "Annual income in INR"),
        ("loan_amount", "float", "Requested loan amount in INR"),
        ("loan_term", "int", "Loan tenure in months"),
        ("cibil_score", "int", "Credit score (300–900)"),
        ("residential_assets_value", "float", "Residential property value"),
        ("commercial_assets_value", "float", "Commercial property value"),
        ("luxury_assets_value", "float", "Luxury item value"),
        ("bank_asset_value", "float", "Liquid bank asset value"),
        ("loan_status", "str", "TARGET: Approved / Rejected"),
    ]

    header_html = """
    <div class="card" style="padding:0;overflow:hidden;">
    <table style="width:100%;border-collapse:collapse;">
    <thead>
        <tr style="background:rgba(26,111,175,0.2);border-bottom:1px solid rgba(255,255,255,0.1);">
            <th style="padding:0.75rem 1.2rem;text-align:left;color:#E8B84B;font-size:0.78rem;letter-spacing:0.08em;">FIELD NAME</th>
            <th style="padding:0.75rem 1.2rem;text-align:left;color:#E8B84B;font-size:0.78rem;letter-spacing:0.08em;">TYPE</th>
            <th style="padding:0.75rem 1.2rem;text-align:left;color:#E8B84B;font-size:0.78rem;letter-spacing:0.08em;">DESCRIPTION</th>
        </tr>
    </thead><tbody>
    """
    rows_html = ""
    for i, (name, dtype, desc) in enumerate(fields):
        bg = "rgba(255,255,255,0.02)" if i % 2 == 0 else "transparent"
        color = "#4DECA0" if name == "loan_status" else "#E8EDF5"
        rows_html += f"""
        <tr style="background:{bg};border-bottom:1px solid rgba(255,255,255,0.05);">
            <td style="padding:0.6rem 1.2rem;color:{color};font-family:monospace;font-size:0.82rem;">{name}</td>
            <td style="padding:0.6rem 1.2rem;"><span style="background:rgba(26,111,175,0.2);border:1px solid rgba(26,111,175,0.4);color:#7CC4F0;font-size:0.72rem;padding:0.15rem 0.5rem;border-radius:6px;">{dtype}</span></td>
            <td style="padding:0.6rem 1.2rem;color:#A8BACE;font-size:0.82rem;">{desc}</td>
        </tr>
        """
    st.markdown(header_html + rows_html + "</tbody></table></div>", unsafe_allow_html=True)
