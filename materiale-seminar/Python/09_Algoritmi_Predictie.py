import streamlit as st
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.metrics import (mean_squared_error, r2_score, mean_absolute_error,
                             accuracy_score, roc_auc_score)
import warnings
warnings.filterwarnings("ignore")

st.set_page_config(
    page_title="Algoritmi de Predictie",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap');
html, body, [class*="css"] { font-family: 'Space Grotesk', sans-serif; }

section[data-testid="stSidebar"] { background:#0F172A; border-right:1px solid #1E3A5F; }
section[data-testid="stSidebar"] * { color:#CBD5E1 !important; }
section[data-testid="stSidebar"] .stRadio label { color:#94A3B8 !important; font-size:14px; padding:5px 0; cursor:pointer; }
section[data-testid="stSidebar"] .stRadio label:hover { color:#E2E8F0 !important; }

.main .block-container { padding:2rem 2.5rem 3rem; max-width:1150px; }

.slide-header { padding:24px 28px 18px; border-radius:14px; margin-bottom:20px; }
.slide-header h1 { margin:0 0 4px; font-size:1.75rem; font-weight:700; color:#fff; letter-spacing:-0.3px; }
.slide-header p  { margin:0; font-size:13px; opacity:0.70; color:#fff; }

.info-card { background:#F8FAFC; border:1px solid #E2E8F0; border-radius:12px; padding:16px 18px; margin-bottom:10px; }
.info-card h3 { margin:0 0 8px; font-size:14px; font-weight:600; }
.info-card p, .info-card li { font-size:13px; color:#475569; line-height:1.65; margin:0; }
.info-card ul, .info-card ol { padding-left:18px; margin:0; }
.info-card li { margin-bottom:5px; }

.formula { background:#0F172A; color:#7DD3FC; font-family:'JetBrains Mono',monospace; font-size:12px;
    padding:11px 15px; border-radius:8px; margin:10px 0; border-left:3px solid #3B82F6; line-height:1.75; }

.concept-box { background:#F0F9FF; border:1px solid #BAE6FD; border-radius:10px; padding:13px 16px; margin:9px 0; }
.concept-box h4 { color:#0C4A6E; margin:0 0 6px; font-size:13px; font-weight:600; }
.concept-box p  { color:#0369A1; font-size:12.5px; margin:0; line-height:1.65; }

.verify-box { background:#FAFAF9; border:1px solid #D6D3D1; border-radius:10px; padding:13px 16px; margin:9px 0; }
.verify-box h4 { color:#1C1917; margin:0 0 7px; font-size:13px; font-weight:600; }
.verify-box p, .verify-box li { color:#44403C; font-size:12.5px; margin:0; line-height:1.65; }
.verify-box ul { padding-left:16px; margin-top:4px; }
.verify-box li { margin-bottom:6px; }

.case-box { background:#FFFBEB; border:1px solid #FDE68A; border-radius:10px; padding:13px 16px; margin:9px 0; }
.case-box h4 { color:#78350F; margin:0 0 6px; font-size:13px; font-weight:600; }
.case-box li { color:#92400E; font-size:12.5px; margin-bottom:5px; line-height:1.6; }
.case-box ul { padding-left:16px; margin:0; }

.pro-box { background:#F0FDF4; border:1px solid #86EFAC; border-radius:10px; padding:11px 14px; }
.con-box { background:#FFF1F2; border:1px solid #FDA4AF; border-radius:10px; padding:11px 14px; }
.pro-box h4 { color:#166534; margin:0 0 6px; font-size:12.5px; font-weight:600; }
.con-box h4 { color:#881337; margin:0 0 6px; font-size:12.5px; font-weight:600; }
.pro-box li, .con-box li { color:#374151; font-size:12px; margin-bottom:4px; }

.section-title { font-size:11px; font-weight:700; text-transform:uppercase; letter-spacing:1.2px;
    color:#94A3B8; margin:20px 0 9px; border-bottom:1px solid #F1F5F9; padding-bottom:5px; }

.warn-box { background:#FFFBEB; border:1px solid #FCD34D; border-radius:10px; padding:11px 15px; margin-top:10px; }
.warn-box p { color:#78350F; font-size:12.5px; margin:0; }

.concl-item { display:flex; gap:13px; align-items:flex-start; background:#F8FAFC; border:1px solid #E2E8F0;
    border-radius:12px; padding:14px 17px; margin-bottom:9px; }
.concl-num { font-size:16px; font-weight:700; min-width:24px; }
.concl-text { font-size:13px; color:#374151; line-height:1.65; margin:0; }
.concl-text strong { color:#0F172A; }

.progress-bar { height:4px; border-radius:2px; background:linear-gradient(90deg,#3B82F6,#8B5CF6); margin-bottom:2px; }
.quote-box { border-left:4px solid #3B82F6; background:#EFF6FF; padding:13px 17px;
    border-radius:0 10px 10px 0; margin-top:16px; }
.quote-box p { color:#1E3A8A; font-style:italic; font-size:13px; margin:0; }
</style>
""", unsafe_allow_html=True)

SLIDES = [
    ("I", "Introducere"),
    ("1", "Regresia Liniara"),
    ("2", "Arbori de Decizie"),
    ("3", "Random Forest"),
    ("4", "Gradient Boosting"),
    ("5", "Retele Neurale"),
    ("6", "Transformers"),
    ("C", "Comparatie"),
    ("F", "Concluzii"),
]

with st.sidebar:
    st.markdown("### Algoritmi de Predictie")
    st.markdown("*De la simplu la complex*")
    st.markdown("---")
    slide_labels = [f"{idx}.  {name}" for idx, name in SLIDES]
    choice = st.radio("Navigheaza", slide_labels, index=0, label_visibility="collapsed")
    current_idx = slide_labels.index(choice)
    current_name = SLIDES[current_idx][1]
    st.markdown("---")
    pct = int(current_idx / (len(SLIDES) - 1) * 100) if current_idx > 0 else 0
    st.markdown(f'<div class="progress-bar" style="width:{pct}%"></div>', unsafe_allow_html=True)
    st.caption(f"Slide {current_idx + 1} din {len(SLIDES)}")
    st.markdown("---")
    st.caption("Niveluri de complexitate:")
    levels = [
        ("1", "Regresia Liniara",  "#059669"),
        ("2", "Arbori Decizie",    "#0891B2"),
        ("3", "Random Forest",     "#2563EB"),
        ("4", "Grad. Boosting",    "#D97706"),
        ("5", "Retele Neurale",    "#7C3AED"),
        ("6", "Transformers",      "#0EA5E9"),
    ]
    for lvl, name, col in levels:
        bar = "█" * int(lvl) + "░" * (6 - int(lvl))
        st.markdown(f'<span style="font-family:monospace;font-size:11px;color:{col};">{bar} {name}</span>',
                    unsafe_allow_html=True)


def header(title, subtitle, color):
    st.markdown(f"""<div class="slide-header" style="background:linear-gradient(135deg,{color} 0%,{color}BB 100%);">
        <h1>{title}</h1><p>{subtitle}</p></div>""", unsafe_allow_html=True)

def card(html, border_color=None):
    b = f"border-left:4px solid {border_color};" if border_color else ""
    st.markdown(f'<div class="info-card" style="{b}">{html}</div>', unsafe_allow_html=True)

def concept(title, text):
    st.markdown(f'<div class="concept-box"><h4>Concept: {title}</h4><p>{text}</p></div>', unsafe_allow_html=True)

def case_study(title, items_html):
    st.markdown(f'<div class="case-box"><h4>Caz concret: {title}</h4>{items_html}</div>', unsafe_allow_html=True)

def verify_section(items_html):
    st.markdown(f'<div class="verify-box"><h4>Cum verifici modelul — in detaliu</h4>{items_html}</div>',
                unsafe_allow_html=True)

def section_title(t):
    st.markdown(f'<p class="section-title">{t}</p>', unsafe_allow_html=True)


# =============================================================================
# SLIDE 0 — INTRODUCERE
# =============================================================================
if current_name == "Introducere":
    header("Algoritmi de Predictie", "De la simplu la complex — ghid progresiv pas cu pas", "#1E3A5F")

    card("""<h3 style="color:#1E3A8A;">Despre ce invatam?</h3>
    <p>Fiecare algoritm <strong>adauga o idee noua</strong> deasupra celui anterior.
    Intelegi un nivel, esti gata pentru urmatorul. La final stii sa alegi instrumentul
    potrivit si stii exact cum sa verifici daca functioneaza cu adevarat in productie.</p>""", "#3B82F6")

    section_title("Harta complexitatii")

    algo_info = [
        ("Reg. Liniara",   1, "#059669", "Linie dreapta prin puncte. O formula simpla."),
        ("Arbori Decizie", 2, "#0891B2", "Intrebari DA/NU in cascada. Logica explicabila."),
        ("Random Forest",  3, "#2563EB", "Sute de arbori voteaza impreuna. Bagging."),
        ("Grad. Boosting", 4, "#D97706", "Arbori invata din erori. Boosting secvential."),
        ("Retele Neurale", 5, "#7C3AED", "Neuroni artificiali in straturi. Backpropagation."),
        ("Transformers",   6, "#0EA5E9", "Atentie globala. GPT, BERT, Claude."),
    ]
    fig = go.Figure()
    for name, lvl, col, desc in algo_info:
        fig.add_trace(go.Bar(
            name=name, x=[name], y=[lvl], marker_color=col, marker_line_width=0,
            text=[f"Nivel {lvl}"], textposition="outside",
            textfont=dict(size=12, color=col),
            hovertext=[desc], hoverinfo="text",
        ))
    fig.update_layout(
        showlegend=False, barmode="group",
        plot_bgcolor="white", paper_bgcolor="white",
        margin=dict(l=0, r=0, t=20, b=0), height=270,
        yaxis=dict(title="Nivel complexitate", range=[0, 7.5],
                   showgrid=True, gridcolor="#F1F5F9", tickfont=dict(size=11)),
        xaxis=dict(showgrid=False, tickfont=dict(size=12, color="#374151")),
    )
    st.plotly_chart(fig, use_container_width=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        card("""<h3 style="color:#059669;">De ce incepem simplu?</h3>
        <p>Regresia Liniara este atat de transparenta incat poti vedea exact de ce da o predictie.
        Daca un model complex da acelasi rezultat, nu ai nevoie de complexitate.</p>""", "#059669")
    with c2:
        card("""<h3 style="color:#D97706;">Cum crestem treptat?</h3>
        <p>Bagging, boosting, backpropagation, atentie — fiecare este o singura idee noua adaugata
        peste ce stii deja. Un concept per slide, explicat cu un caz real.</p>""", "#D97706")
    with c3:
        card("""<h3 style="color:#7C3AED;">Ce inseamna verificare?</h3>
        <p>La fiecare algoritm explicam exact ce metrici se folosesc, ce inseamna valorile lor
        si cum detectezi overfitting, underfitting sau data leakage.</p>""", "#7C3AED")


# =============================================================================
# SLIDE 1 — REGRESIA LINIARA
# =============================================================================
elif current_name == "Regresia Liniara":
    header("Regresia Liniara", "Nivelul 1 — Cea mai simpla forma de predictie: o linie dreapta prin puncte", "#059669")

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        card("""<h3 style="color:#059669;">Ce face algoritmul?</h3>
        <p>Gaseste cea mai buna linie dreapta printr-un nor de puncte astfel incat distanta
        totala dintre puncte si linie sa fie minima. Aceasta linie devine instrumentul de predictie.
        Minimizarea se face pe <strong>suma patratelor erorilor (MSE)</strong> — se pateaza erorile
        ca sa penalizeze mai mult greselile mari.</p>""", "#059669")

        st.markdown(
            '<div class="formula">'
            'y = b0 + b1*x1 + b2*x2 + ... + bn*xn\n\n'
            'MSE  = (1/n) * sum( (yi - yi_pred)^2 )\n'
            'MAE  = (1/n) * sum( |yi - yi_pred| )\n'
            'R2   = 1 - SS_res / SS_tot   (0=prost, 1=perfect)'
            '</div>', unsafe_allow_html=True)

        concept("Gradient Descent",
                "Algoritmul porneste cu coeficienti aleatori si ii corecteaza iterativ in directia "
                "care reduce MSE. Rata de invatare (learning rate) controleaza marimea fiecarui pas. "
                "Prea mare: oscileaza si nu converge. Prea mica: converge extrem de lent. "
                "In practica, pentru regresia liniara simpla exista si solutia analitica exacta: "
                "b = (X^T * X)^(-1) * X^T * y — dar gradient descent scala mai bine cu milioane de exemple.")

        concept("Multicolinearitate",
                "Daca doua features sunt puternic corelate (ex: suprafata mp si nr. camere), "
                "coeficientii devin instabili si greu de interpretat. "
                "Detectie: VIF (Variance Inflation Factor) — VIF > 10 semnaleaza problema. "
                "Solutii: elimini una dintre variabile, folosesti PCA, sau aplici regularizare Ridge.")

        case_study("Estimarea pretului chiriei in Bucuresti",
                   """<ul>
                   <li><strong>Date:</strong> 2.400 anunturi de inchiriere cu suprafata, camere, etaj, distanta metrou, zona</li>
                   <li><strong>Formula rezultata:</strong> Chirie = -120 + 8.5*mp + 40*camere + 3*etaj - 25*dist_metrou_km + 180*zona_centrala</li>
                   <li><strong>Interpretare directa:</strong> fiecare metru patrat adauga 8.5 EUR; fiecare km fata de metrou scade chiria cu 25 EUR</li>
                   <li><strong>R² obtinut:</strong> 0.81 — modelul explica 81% din variatia chiriilor</li>
                   <li><strong>Limitare observata:</strong> in zona Floreasca, apartamentele mici au un premium neliniar care nu poate fi capturat de linie dreapta</li>
                   <li><strong>Decizie:</strong> pentru portofoliul standard, modelul e suficient de bun si complet explicabil chiriasilor</li>
                   </ul>""")

        c_pro, c_con = st.columns(2)
        with c_pro:
            st.markdown("""<div class="pro-box"><h4>Avantaje</h4><ul>
            <li>Complet explicabil — fiecare coeficient are sens</li>
            <li>Antrenament in milisecunde</li>
            <li>Functioneaza bine cu 50+ exemple</li>
            <li>Coeficientii sunt interpretabili direct</li>
            </ul></div>""", unsafe_allow_html=True)
        with c_con:
            st.markdown("""<div class="con-box"><h4>Limitari</h4><ul>
            <li>Nu captureaza relatii nelineare</li>
            <li>Sensibil la outlieri — un apartament de lux strica tot</li>
            <li>Presupune ca variabilele sunt independente</li>
            </ul></div>""", unsafe_allow_html=True)

    with col2:
        np.random.seed(42)
        n = 60
        mp = np.random.uniform(30, 150, n)
        chiria = 120 + 8.5 * mp + np.random.normal(0, 60, n)
        reg = LinearRegression()
        reg.fit(mp.reshape(-1, 1), chiria)
        mp_line = np.linspace(28, 155, 100)
        chiria_pred = reg.predict(mp_line.reshape(-1, 1))

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=mp, y=chiria, mode='markers',
            marker=dict(color="#059669", size=7, opacity=0.6), name="Apartamente reale"))
        fig.add_trace(go.Scatter(x=mp_line, y=chiria_pred, mode='lines',
            line=dict(color="#1E3A5F", width=2.5), name="Regresia liniara"))
        for i in range(0, n, 4):
            pred_i = reg.predict([[mp[i]]])[0]
            fig.add_trace(go.Scatter(x=[mp[i], mp[i]], y=[chiria[i], pred_i], mode='lines',
                line=dict(color="#EF4444", width=1, dash="dot"),
                showlegend=False, hoverinfo='none'))
        fig.update_layout(
            plot_bgcolor="white", paper_bgcolor="white",
            height=240, margin=dict(l=0, r=0, t=10, b=0),
            xaxis=dict(title="Suprafata (mp)", showgrid=True, gridcolor="#F1F5F9"),
            yaxis=dict(title="Chirie (EUR/luna)", showgrid=True, gridcolor="#F1F5F9"),
            legend=dict(font=dict(size=11), orientation="h", y=1.08),
        )
        st.plotly_chart(fig, use_container_width=True)
        st.caption("Liniile rosii = rezidualuri (erori de predictie). Algoritmul minimizeaza suma patratelor acestora.")

        section_title("Cum verifici modelul — in detaliu")
        verify_section("""<ul>
        <li><strong>R² (R-squared):</strong> proportia din variatia lui y explicata de model. R²=0.81 inseamna
            ca 81% din variatia chiriei e explicata de suprafata, camere, etaj etc. Sub 0.5 e slab.
            Peste 0.8 e bun pentru date imobiliare. Atentie: R² creste automat cu mai multe variabile — foloseste R² ajustat.</li>
        <li><strong>RMSE (Root Mean Squared Error):</strong> radacina din MSE iti da eroarea medie in aceleasi
            unitati cu y. Daca RMSE=80 EUR, modelul greseste in medie cu 80 EUR pe luna — interpretabil direct.
            Util cand erorile mari sunt mai periculoase (penalizeaza outlieri).</li>
        <li><strong>MAE (Mean Absolute Error):</strong> mai robust la outlieri decat RMSE. Daca MAE=55 EUR
            dar RMSE=120 EUR, ai outlieri mari care influenteaza modelul. Compara ambele metrici intotdeauna.</li>
        <li><strong>Analiza rezidualurilor:</strong> traseaza rezidualuri vs valori prezise. Trebuie sa fie
            aleatoare in jurul lui 0 fara niciun pattern. Daca vezi o curba, relatia nu e liniara si ai nevoie
            de transformari (log, sqrt) sau de un model mai complex.</li>
        <li><strong>Train vs Test split:</strong> antreneaza pe 80% din date, evalueaza pe 20% nevazute.
            Daca RMSE_train=50 si RMSE_test=52 — model bun, generalizeaza. Daca RMSE_test=200 — overfitting sau data leakage.</li>
        <li><strong>Multicolinearitate (VIF):</strong> instaleaza statsmodels si calculeaza VIF pentru fiecare feature.
            VIF > 10 = problema — coeficientii sunt instabili. Elimini una dintre variabilele corelate sau folosesti Ridge.</li>
        </ul>""")

        X_tr, X_te, y_tr, y_te = train_test_split(mp.reshape(-1, 1), chiria, test_size=0.2, random_state=0)
        reg2 = LinearRegression().fit(X_tr, y_tr)
        y_pred_te = reg2.predict(X_te)
        r2  = r2_score(y_te, y_pred_te)
        rmse = np.sqrt(mean_squared_error(y_te, y_pred_te))
        mae  = mean_absolute_error(y_te, y_pred_te)

        m1, m2, m3 = st.columns(3)
        m1.metric("R²", f"{r2:.3f}", help="1.0 = perfect, 0 = la fel ca media")
        m2.metric("RMSE (EUR)", f"{rmse:.1f}", help="Eroarea medie in EUR/luna")
        m3.metric("MAE (EUR)", f"{mae:.1f}", help="Eroare absoluta medie")


# =============================================================================
# SLIDE 2 — ARBORI DE DECIZIE
# =============================================================================
elif current_name == "Arbori de Decizie":
    header("Arbori de Decizie", "Nivelul 2 — Logica prin intrebari binare: cum separam datele optim la fiecare pas", "#0891B2")

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        card("""<h3 style="color:#0891B2;">Ce face algoritmul?</h3>
        <p>La fiecare nod, alege <strong>cea mai buna intrebare</strong> (feature + prag) care separa
        datele in doua grupuri cat mai <em>pure</em> posibil — adica grupuri in care aproape toti membrii
        apartin aceleiasi clase. Repeta recursiv pana cand grupurile sunt pure sau pana la adancimea maxima.</p>""",
        "#0891B2")

        st.markdown(
            '<div class="formula">'
            'Gini impurity = 1 - sum(pi^2)\n'
            '  pi = proportia clasei i in nod\n'
            '  Gini=0   => nod pur (toti din aceeasi clasa)\n'
            '  Gini=0.5 => haos total (50/50)\n\n'
            'Information Gain = H(parinte) - sum( n_i/n * H(copil_i) )\n'
            'H(S) = -sum( pi * log2(pi) )  <- entropie Shannon'
            '</div>', unsafe_allow_html=True)

        concept("Impuritate Gini — intuitia",
                "Imagineaza-ti un sac cu bile rosii si albastre. Gini masoara cat de amestecat e sacul. "
                "90 rosii + 10 albastre: Gini = 1 - (0.9^2 + 0.1^2) = 0.18 — destul de pur. "
                "50 rosii + 50 albastre: Gini = 1 - (0.5^2 + 0.5^2) = 0.5 — maxim de impuritate. "
                "La fiecare nod, algoritmul evalueaza toate split-urile posibile si alege cel care "
                "produce copii cu Gini minim (cele mai pure grupuri).")

        concept("Overfitting in arbori — mecanismul exact",
                "Un arbore care creste fara restrictii ajunge sa aiba cate un nod pentru fiecare exemplu "
                "de antrenament — acuratete 100% pe train, dar memoreaza zgomotul. "
                "Parametrii de control: max_depth (limiteaza adancimea), min_samples_split (minim exemple "
                "pentru a face split), min_samples_leaf (minim exemple intr-o frunza). "
                "Un max_depth=5 este de obicei un punct de plecare bun.")

        case_study("Aprobarea creditelor bancare (banca romaneasca)",
                   """<ul>
                   <li><strong>Date:</strong> 10.000 cereri de credit, 12 variabile, 23% rata de default</li>
                   <li><strong>Target:</strong> credit rambursat integral (0) vs partial sau deloc (1)</li>
                   <li><strong>Primul split ales de algoritm:</strong> Scor BNR > 650? — Gini scade de la 0.35 la 0.18</li>
                   <li><strong>Al doilea split (scor mic):</strong> Venit net > 2.500 RON? separa 78% din defaulturi</li>
                   <li><strong>Al doilea split (scor mare):</strong> Vechime angajator > 12 luni?</li>
                   <li><strong>Avantaj crucial pentru banca:</strong> poate explica exact de ce a refuzat un client (cerinta GDPR Art. 22 si Basel III)</li>
                   <li><strong>Limitare observata:</strong> arbore cu depth=15 da 97% pe train si 71% pe test — overfitting sever; depth=5 da 84% pe ambele</li>
                   </ul>""")

        c_pro, c_con = st.columns(2)
        with c_pro:
            st.markdown("""<div class="pro-box"><h4>Avantaje</h4><ul>
            <li>Complet explicabil — urmaresti orice decizie</li>
            <li>Nu necesita scalare a datelor</li>
            <li>Gestioneaza variabile categorice nativ</li>
            <li>Vizualizabil grafic pentru non-tehnici</li>
            </ul></div>""", unsafe_allow_html=True)
        with c_con:
            st.markdown("""<div class="con-box"><h4>Limitari</h4><ul>
            <li>Overfitting sever fara limitare explicita</li>
            <li>Instabil — mici schimbari in date schimba arborele complet</li>
            <li>Hotare de decizie paralele cu axele, nu diagonale</li>
            </ul></div>""", unsafe_allow_html=True)

    with col2:
        fig = go.Figure()
        nodes = {
            0: (0.50, 0.88, "Scor BNR > 650?",      "#0891B2"),
            1: (0.22, 0.60, "Venit > 2500 RON?",     "#0891B2"),
            2: (0.78, 0.60, "Vechime > 12 luni?",    "#0891B2"),
            3: (0.10, 0.32, "REFUZAT\nGini=0.05",    "#EF4444"),
            4: (0.34, 0.32, "ANALIZA\nGini=0.38",    "#F59E0B"),
            5: (0.62, 0.32, "APROBAT\nGini=0.08",    "#059669"),
            6: (0.90, 0.32, "APROBAT\nGini=0.02",    "#059669"),
        }
        edges = [(0,1,"NU 35%"),(0,2,"DA 65%"),(1,3,"NU"),(1,4,"DA"),(2,5,"NU"),(2,6,"DA")]
        for (p, c, lbl) in edges:
            px_, py_ = nodes[p][0], nodes[p][1]
            cx, cy = nodes[c][0], nodes[c][1]
            col_lbl = "#EF4444" if "NU" in lbl else "#059669"
            fig.add_trace(go.Scatter(x=[px_, cx], y=[py_, cy], mode='lines',
                line=dict(color="#CBD5E1", width=2), showlegend=False, hoverinfo='none'))
            fig.add_annotation(x=(px_+cx)/2, y=(py_+cy)/2+0.03, text=f"<b>{lbl}</b>",
                showarrow=False, font=dict(size=9.5, color=col_lbl),
                bgcolor="white", borderpad=2)
        for nid, (x, y, lbl, col) in nodes.items():
            fig.add_trace(go.Scatter(x=[x], y=[y], mode='markers+text',
                marker=dict(size=64, color=col, symbol="square",
                            line=dict(color="white", width=2)),
                text=[lbl], textposition="middle center",
                textfont=dict(size=9, color="white"),
                showlegend=False, hoverinfo='none'))
        fig.update_layout(
            plot_bgcolor="white", paper_bgcolor="white",
            height=285, margin=dict(l=0, r=0, t=10, b=0),
            xaxis=dict(visible=False, range=[-0.05, 1.05]),
            yaxis=dict(visible=False, range=[0.15, 1.0]),
        )
        st.plotly_chart(fig, use_container_width=True)

        st.markdown("""<div class="warn-box">
        <p><strong>Demonstratie overfitting:</strong> un arbore nelimitat (depth=None) obtine 100% pe datele
        de antrenament si 68% pe test — a memorat zgomotul. Cu max_depth=4 obtinem 84% pe ambele seturi.
        Verifici intotdeauna comparand train accuracy cu test accuracy.</p></div>""", unsafe_allow_html=True)

        section_title("Cum verifici modelul — in detaliu")
        verify_section("""<ul>
        <li><strong>Accuracy vs AUC-ROC:</strong> pe date dezechilibrate (23% default, 77% rambursare normala),
            accuracy de 77% e obtinuta spunand mereu "rambursare normala". Metrica inutila in acest caz.
            AUC-ROC masoara capacitatea de discriminare la orice prag — foloseste asta intotdeauna pe date dezechilibrate.</li>
        <li><strong>Confusion Matrix detaliata:</strong> TP=credite rele corect refuzate, TN=credite bune corect aprobate,
            FP=credite bune refuzate gresit (cost: client pierdut), FN=credite rele aprobate gresit (cost: pierdere financiara).
            In banking, FN costa de 5-10x mai mult decat FP — ajustezi pragul de decizie explicit in functie de acest raport.</li>
        <li><strong>Precision si Recall:</strong> Precision = TP/(TP+FP) — din toti prezisi default, cati chiar sunt?
            Recall = TP/(TP+FN) — din toti defaulterii reali, cati i-ai prins?
            F1 = 2 * (P*R)/(P+R) — media armonica, utila cand vrei echilibru intre cele doua.</li>
        <li><strong>Overfitting test sistematic:</strong> traseaza train_accuracy si test_accuracy in functie de max_depth (1 la 20).
            Gaseste punctul unde test_accuracy atinge maxim — acela e max_depth-ul optim. Dupa acel punct, train creste dar test scade.</li>
        <li><strong>Cross-validation stratificat:</strong> pe date dezechilibrate, foloseste StratifiedKFold (pastreaza
            proportia claselor in fiecare fold). 5-10 fold-uri. Raporteaza media si deviatia standard a AUC-ROC.</li>
        </ul>""")

        np.random.seed(0)
        n_c = 500
        scor = np.random.normal(600, 80, n_c).clip(400, 850)
        venit = np.random.normal(3500, 1000, n_c).clip(1000, 10000)
        X_c = np.column_stack([scor, venit])
        y_c = ((scor > 640) & (venit > 2800)).astype(int)
        X_ctr, X_cte, y_ctr, y_cte = train_test_split(X_c, y_c, test_size=0.25, random_state=1)
        dt = DecisionTreeClassifier(max_depth=4, random_state=0).fit(X_ctr, y_ctr)
        dt_over = DecisionTreeClassifier(max_depth=None, random_state=0).fit(X_ctr, y_ctr)

        m1, m2, m3, m4 = st.columns(4)
        m1.metric("AUC-ROC test", f"{roc_auc_score(y_cte, dt.predict_proba(X_cte)[:,1]):.3f}")
        m2.metric("Acc test (depth=4)", f"{accuracy_score(y_cte, dt.predict(X_cte)):.1%}")
        m3.metric("Acc train (depth=4)", f"{accuracy_score(y_ctr, dt.predict(X_ctr)):.1%}")
        m4.metric("Acc train (depth=inf)", f"{accuracy_score(y_ctr, dt_over.predict(X_ctr)):.1%}",
                  delta="Overfitting!", delta_color="inverse")


# =============================================================================
# SLIDE 3 — RANDOM FOREST
# =============================================================================
elif current_name == "Random Forest":
    header("Random Forest", "Nivelul 3 — Bagging: sute de arbori independenti voteaza impreuna", "#2563EB")

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        card("""<h3 style="color:#2563EB;">Ce face algoritmul?</h3>
        <p>Construieste <strong>N arbori de decizie independenti</strong>, fiecare antrenat pe un subset
        aleator diferit de date si de features. La predictie, fiecare arbore voteaza si castigul merge
        la clasa cu cele mai multe voturi (clasificare) sau la media voturilor (regresie).</p>""", "#2563EB")

        concept("Bagging (Bootstrap Aggregating) — ideea de baza",
                "Bagging rezolva instabilitatea arborilor prin diversitate controlata: daca antrenezi 500 de "
                "arbori pe subseturi usor diferite de date, erorile lor sunt ne-corelate — unii gresesc "
                "in stanga, altii in dreapta, dar media lor converge spre raspunsul corect. "
                "Legea numerelor mari aplicata la ML. Reduce variantza modelului fara a creste bias-ul.")

        concept("Bootstrap Sampling — mecanismul",
                "Din N exemple de antrenament, extragi aleator N exemple CU REPETITIE "
                "(aproximativ 63% unice, 37% duplicate la fiecare extragere). Fiecare arbore primeste un set diferit. "
                "Exemplele care nu au fost extrase pentru un arbore specific (aproximativ 37%) "
                "formeaza setul Out-of-Bag (OOB) — un set de validare gratuit, fara sa consumi date de test separate.")

        concept("Feature Randomness — de ce e esential",
                "La fiecare nod al fiecarui arbore, algoritmul evalueaza doar un subset aleator de sqrt(p) features "
                "(clasificare) sau p/3 (regresie) — nu toate. Aceasta forteaza arborii sa fie diversi si sa nu "
                "depinda toti de aceleasi cateva features dominante (ex: toti sa intrebe 'Scor credit > 650?' ca prim split). "
                "Fara aceasta randomizare, arborii ar fi corelati si votul lor ar fi echivalent cu un singur arbore.")

        st.markdown(
            '<div class="formula">'
            'Predictie finala (clasificare):\n'
            '  y = moda( arb1(x), arb2(x), ..., arbN(x) )\n\n'
            'Predictie finala (regresie):\n'
            '  y = media( arb1(x), arb2(x), ..., arbN(x) )\n\n'
            'OOB Error = media erorilor pe exemplele nefolosite\n'
            '           la antrenamentul fiecarui arbore'
            '</div>', unsafe_allow_html=True)

        case_study("Detectia fraudei pe carduri bancare",
                   """<ul>
                   <li><strong>Date:</strong> 284.807 tranzactii, 492 fraude (0.17%) — dezechilibru extrem de clasic</li>
                   <li><strong>Features:</strong> suma tranzactie, ora, distanta fata de ultima tranzactie, frecventa zilnica, comerciant</li>
                   <li><strong>Problema cu un singur arbore:</strong> zice mereu "legitim" si obtine 99.83% accuracy — complet inutil, nu prinde nicio frauda</li>
                   <li><strong>Random Forest (500 arbori, class_weight=balanced):</strong> detecteaza 94% din fraude cu doar 0.3% alarme false</li>
                   <li><strong>Feature Importance:</strong> suma tranzactie (38%), distanta fata de ultima tranzactie (25%), frecventa zilnica (20%), ora (17%)</li>
                   <li><strong>Insight operational:</strong> o tranzactie de 1 EUR urmata la 2 ore de una de 999 EUR in alt oras = pattern de frauda confirmare</li>
                   </ul>""")

    with col2:
        np.random.seed(7)
        n_trees_viz = 9
        votes_viz = [True]*6 + [False]*3
        np.random.shuffle(votes_viz)

        fig = go.Figure()
        for i, v in enumerate(votes_viz):
            col_bar = "#2563EB" if v else "#EF4444"
            fig.add_trace(go.Bar(
                x=[f"T{i+1}"], y=[1], marker_color=col_bar, marker_line_width=0,
                text=["Frauda" if v else "Legitim"], textposition="inside",
                textfont=dict(size=11, color="white"), showlegend=False,
            ))
        fig.add_annotation(x=4, y=1.28,
            text=f"<b>Decizie finala: FRAUDA ({sum(votes_viz)}/{n_trees_viz} voturi)</b>",
            showarrow=False, font=dict(size=12, color="#2563EB"),
            bgcolor="#EFF6FF", bordercolor="#2563EB", borderwidth=1.5, borderpad=8)
        fig.update_layout(
            plot_bgcolor="white", paper_bgcolor="white",
            height=195, margin=dict(l=0, r=0, t=50, b=0),
            yaxis=dict(visible=False, range=[0, 1.5]),
            xaxis=dict(showgrid=False, tickfont=dict(size=11)),
        )
        st.plotly_chart(fig, use_container_width=True)

        section_title("Feature Importance — ce variabile conteaza?")
        features = ["Suma tranzactie", "Distanta locatie", "Frecv. zilnica", "Ora tranzactie", "Nr. tranzactii zi"]
        importances = [0.38, 0.25, 0.20, 0.10, 0.07]
        colors_fi = ["#2563EB" if i < 3 else "#93C5FD" for i in range(5)]
        fig2 = go.Figure(go.Bar(
            x=importances, y=features, orientation='h',
            marker_color=colors_fi, marker_line_width=0,
            text=[f"{v:.0%}" for v in importances], textposition="outside",
        ))
        fig2.update_layout(
            plot_bgcolor="white", paper_bgcolor="white",
            height=185, margin=dict(l=0, r=50, t=5, b=0),
            xaxis=dict(visible=False),
            yaxis=dict(tickfont=dict(size=12)),
        )
        st.plotly_chart(fig2, use_container_width=True)

        section_title("Cum verifici modelul — in detaliu")
        verify_section("""<ul>
        <li><strong>OOB Score:</strong> fiecare arbore e evaluat pe exemplele pe care nu le-a vazut la antrenament (OOB set).
            Media acestor erori este OOB Score — o estimare solida a erorii de generalizare fara sa consumi setul de test.
            Daca OOB Score = 0.91 si Test Score = 0.90, modelul generalizeaza excelent.</li>
        <li><strong>n_estimators optim:</strong> traseaza OOB Error in functie de numarul de arbori (de la 10 la 1000).
            Eroarea scade rapid la inceput si ajunge la un platou. Alegi n_estimators la "cotul" curbei (tipic 200-500).
            Dupa platou, mai multi arbori nu aduc imbunatatire — doar cost computational.</li>
        <li><strong>Cross-Validation stratificat (5-fold):</strong> imparte datele in 5 parti egale pastrand proportia claselor,
            antreneaza pe 4 si testeaza pe 1, repeta de 5 ori. Raporteaza media si deviatia standard a AUC-ROC.
            Deviatie standard mare (ex: 0.05) = model instabil pe date diferite — ai nevoie de mai multe date.</li>
        <li><strong>Precision-Recall Curve (pe date dezechilibrate):</strong> pe 0.17% frauda, AUC-ROC poate parea excelenta
            chiar si pentru un model slab. Curba Precision-Recall e mai informativa: vrei Precision mare (putine alarme false)
            sau Recall mare (prinzi mai multe fraude)? Depinde de costul de business al fiecarei erori.</li>
        <li><strong>Feature Importance stabilitate:</strong> ruleaza modelul de 5 ori cu seed diferit si compara ordinea importantelor.
            Daca se schimba dramatic, featurile sunt corelate si importanta e instabila. Foloseste permutation importance
            (sklearn.inspection.permutation_importance) — mai robusta, masoara impactul real pe performanta.</li>
        <li><strong>Calibrare probabilitati:</strong> daca modelul zice 70% probabilitate de frauda, in 70% din aceste cazuri
            trebuie sa fie frauda. Verifica cu calibration_curve din sklearn. Daca nu e calibrat, aplica CalibratedClassifierCV.</li>
        </ul>""")

        np.random.seed(0)
        n_f = 700
        X_f = np.random.randn(n_f, 4)
        y_f = (X_f[:, 0] + X_f[:, 1]*0.5 + np.random.randn(n_f)*0.3 > 0.5).astype(int)
        X_ftr, X_fte, y_ftr, y_fte = train_test_split(X_f, y_f, test_size=0.25, random_state=1)
        rf = RandomForestClassifier(n_estimators=200, oob_score=True, random_state=0).fit(X_ftr, y_ftr)
        cv_s = cross_val_score(rf, X_ftr, y_ftr, cv=5, scoring='roc_auc')

        m1, m2, m3, m4 = st.columns(4)
        m1.metric("OOB Score", f"{rf.oob_score_:.3f}")
        m2.metric("AUC-ROC test", f"{roc_auc_score(y_fte, rf.predict_proba(X_fte)[:,1]):.3f}")
        m3.metric("CV-5 AUC medie", f"{cv_s.mean():.3f}")
        m4.metric("CV Std Dev", f"{cv_s.std():.4f}", help="Sub 0.02 = model stabil")


# =============================================================================
# SLIDE 4 — GRADIENT BOOSTING
# =============================================================================
elif current_name == "Gradient Boosting":
    header("Gradient Boosting — XGBoost — LightGBM", "Nivelul 4 — Boosting: fiecare arbore nou invata din erorile celui precedent", "#D97706")

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        card("""<h3 style="color:#D97706;">Ce face algoritmul?</h3>
        <p>Construieste arbori <strong>secvential</strong>, nu paralel ca Random Forest. Fiecare arbore nou
        se antreneaza pe <em>rezidualurile</em> modelului curent — adica pe greselile ramase. Suma tuturor
        arborilor, ponderata cu learning rate, formeaza predictia finala.</p>""", "#D97706")

        concept("Boosting vs Bagging — diferenta fundamentala",
                "Bagging (Random Forest): arbori PARALELI, independenti, fiecare pe un subset diferit. "
                "Reduce varianta modelului. Nu depinde de ordinea in care sunt construiti. "
                "Boosting: arbori SECVENTIALI, fiecare corecteza erorile celui anterior. "
                "Reduce atat varianta cat si bias-ul. Ordinea conteaza — arborele 5 nu poate fi construit "
                "fara arborele 4. De aceea boosting e mai lent dar adesea mai precis.")

        concept("Rezidualuri si Gradient — de ce se numeste 'Gradient'",
                "La fiecare pas, calculam rezidualul: eroare = y_real - y_prezis. "
                "Arborele urmator se antreneaza pe aceste erori ca si cum ar fi noul target. "
                "In forma generala, rezidualul este gradientul negativ al functiei de cost — "
                "algoritmul face gradient descent in spatiul functiilor, nu in spatiul parametrilor ca regresia clasica. "
                "Aceasta permite minimizarea oricand functii de cost: MSE, MAE, Log-Loss, Huber etc.")

        concept("Early Stopping — parametrul esential",
                "Setezi un set de validare separat. La fiecare iteratie, calculezi eroarea pe el. "
                "Daca eroarea de validare nu scade dupa N iteratii consecutive (early_stopping_rounds=50), "
                "antrenamentul se opreste automat la numarul optim de arbori. "
                "Aceasta previne overfitting-ul fara sa faci grid search separat pentru n_estimators.")

        st.markdown(
            '<div class="formula">'
            'F0(x) = valoare initiala (media pentru regresie)\n'
            'Pentru t = 1 pana la T:\n'
            '  r_i = y_i - F_{t-1}(x_i)   <- rezidualuri (erori)\n'
            '  h_t = antreneaza arbore mic pe r_i\n'
            '  F_t(x) = F_{t-1}(x) + eta * h_t(x)\n\n'
            'Predictie finala: FT(x) = F0 + eta*h1 + ... + eta*hT\n'
            'eta = learning rate (0.01-0.3)'
            '</div>', unsafe_allow_html=True)

        case_study("Predictia abandonului clientilor (Churn) la o companie telecom",
                   """<ul>
                   <li><strong>Date:</strong> 50.000 clienti, 35 variabile (vechime, ARPU, nr. apeluri suport, roaming, contract tip)</li>
                   <li><strong>Target:</strong> abandon in urmatoarele 30 zile (10.5% rata de churn)</li>
                   <li><strong>De ce Gradient Boosting?</strong> relatii neliniare complexe: un client cu contract anual NU abandoneaza indiferent de ARPU, dar unul lunar cu ARPU scazut SI apeluri suport frecvente — da</li>
                   <li><strong>Hiperparametri gasiti (Bayesian Search):</strong> n_estimators=600, max_depth=5, learning_rate=0.05, subsample=0.8, colsample_bytree=0.7</li>
                   <li><strong>Rezultat:</strong> AUC-ROC 0.89 vs 0.81 Random Forest vs 0.74 Regresie Logistica</li>
                   <li><strong>SHAP insight:</strong> "Acest client are 67% probabilitate de churn pentru ca: contract lunar (+0.22), 4 apeluri suport luna trecuta (+0.18), ARPU sub 20 RON (+0.15)"</li>
                   <li><strong>Actiune retentie:</strong> echipa de retentie contacteaza clientii cu scor > 0.6 cu oferte personalizate</li>
                   </ul>""")

        c_pro, c_con = st.columns(2)
        with c_pro:
            st.markdown("""<div class="pro-box"><h4>Avantaje</h4><ul>
            <li>Cel mai bun pe date tabelate structurate</li>
            <li>Regularizare L1/L2 incorporata (XGBoost)</li>
            <li>Gestioneaza valori lipsa nativ (XGBoost)</li>
            <li>SHAP pentru explicabilitate individuala</li>
            </ul></div>""", unsafe_allow_html=True)
        with c_con:
            st.markdown("""<div class="con-box"><h4>Limitari</h4><ul>
            <li>Multi hiperparametri de tunat</li>
            <li>Antrenament secvential — mai lent</li>
            <li>Sensibil la outlieri (mai mult ca RF)</li>
            </ul></div>""", unsafe_allow_html=True)

    with col2:
        iters = list(range(1, 501, 10))
        np.random.seed(3)
        train_err = [85 * np.exp(-0.008*i) + 2 + np.random.normal(0, 0.3) for i in iters]
        test_err  = [85 * np.exp(-0.006*i) + 8 + np.random.normal(0, 0.5) for i in iters]

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=iters, y=train_err, mode='lines',
            line=dict(color="#D97706", width=2.5), name="Eroare antrenament",
            fill='tozeroy', fillcolor="rgba(217,119,6,0.08)"))
        fig.add_trace(go.Scatter(x=iters, y=test_err, mode='lines',
            line=dict(color="#7C3AED", width=2, dash='dash'), name="Eroare validare"))
        fig.add_vline(x=280, line=dict(color="#EF4444", width=1.5, dash='dot'),
                      annotation_text="Early stopping ~280", annotation_position="top right",
                      annotation_font=dict(size=9.5, color="#EF4444"))
        fig.update_layout(
            plot_bgcolor="white", paper_bgcolor="white",
            height=215, margin=dict(l=0, r=0, t=10, b=0),
            xaxis=dict(title="Nr. arbori (iteratii)", showgrid=True, gridcolor="#F1F5F9"),
            yaxis=dict(title="Eroare (%)", showgrid=True, gridcolor="#F1F5F9"),
            legend=dict(font=dict(size=11), orientation="h", y=1.08),
        )
        st.plotly_chart(fig, use_container_width=True)
        st.caption("Dupa punctul de early stopping, eroarea de validare creste — overfitting. Antrenamentul se opreste automat acolo.")

        section_title("Cum verifici modelul — in detaliu")
        verify_section("""<ul>
        <li><strong>Learning curve train vs validare per iteratie:</strong> urmaresti ambele curbe simultan in timp real.
            Train scade monoton (normal). Val scade, atinge un minim, apoi creste — acel minim e punctul optim.
            XGBoost afiseaza aceste valori la fiecare iteratie cu verbose=1. Vizualizeaza cu xgb.plot_metric(model).</li>
        <li><strong>Early stopping corect configurat:</strong> separa datele in train (70%) + validare (15%) + test (15%).
            Pasezi eval_set=[(X_val, y_val)] si early_stopping_rounds=50 la fit(). Modelul se opreste automat.
            ATENTIE: nu folosi setul de test ca set de validare pentru early stopping — ai data leakage.</li>
        <li><strong>Ordinea corecta de tuning hiperparametri:</strong>
            (1) n_estimators mare (1000) + early stopping — se determina automat numarul optim de arbori.
            (2) max_depth (3-8) si min_child_weight (1-10) — controleaza complexitatea per arbore.
            (3) subsample (0.6-0.9) si colsample_bytree (0.6-0.9) — randomizare.
            (4) Scazi learning_rate (0.01-0.05) si cresti n_estimators proportional.
            Nu tunezi toti parametrii simultan — spatiul e prea mare si rezultatele devin inexplicabile.</li>
        <li><strong>SHAP (SHapley Additive exPlanations):</strong> explica individual fiecare predictie.
            SHAP summary plot: arata importanta globala si directia efectului per feature.
            SHAP force plot: "aceasta predictie de 89% churn vine din: contract lunar +0.22, apeluri suport +0.18, ARPU scazut +0.15".
            Indispensabil in contexte unde trebuie sa explici deciziile clientilor sau regulatorilor.</li>
        <li><strong>Permutation Importance vs Built-in Importance:</strong> feature importance din XGBoost (bazata pe nr. de split-uri)
            supraevalueaza featurile cu multi valori unici (ex: ID client). Permutation importance amesteca valorile unui feature
            si masoara cat creste eroarea — mai corecta si mai robusta. Calculeaza ambele si compara.</li>
        </ul>""")

        np.random.seed(0)
        n_gb = 600
        X_gb = np.random.randn(n_gb, 5)
        y_gb = (X_gb[:,0]**2 + X_gb[:,1]*X_gb[:,2] + np.random.randn(n_gb)*0.2 > 0.5).astype(int)
        X_gbtr, X_gbte, y_gbtr, y_gbte = train_test_split(X_gb, y_gb, test_size=0.25, random_state=1)
        gb = GradientBoostingClassifier(n_estimators=200, max_depth=4, learning_rate=0.1, random_state=0).fit(X_gbtr, y_gbtr)
        rf_base = RandomForestClassifier(n_estimators=100, random_state=0).fit(X_gbtr, y_gbtr)

        m1, m2, m3, m4 = st.columns(4)
        m1.metric("GB AUC-ROC", f"{roc_auc_score(y_gbte, gb.predict_proba(X_gbte)[:,1]):.3f}")
        m2.metric("RF AUC-ROC (baseline)", f"{roc_auc_score(y_gbte, rf_base.predict_proba(X_gbte)[:,1]):.3f}")
        m3.metric("GB Accuracy", f"{accuracy_score(y_gbte, gb.predict(X_gbte)):.1%}")
        m4.metric("GB vs RF delta", f"+{(roc_auc_score(y_gbte, gb.predict_proba(X_gbte)[:,1]) - roc_auc_score(y_gbte, rf_base.predict_proba(X_gbte)[:,1])):.3f}")


# =============================================================================
# SLIDE 5 — RETELE NEURALE
# =============================================================================
elif current_name == "Retele Neurale":
    header("Retele Neurale Profunde — Deep Learning", "Nivelul 5 — Neuroni artificiali in straturi: invata reprezentari ierarhice din date brute", "#7C3AED")

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        card("""<h3 style="color:#7C3AED;">Ce face algoritmul?</h3>
        <p>Compune straturi de <strong>transformari neliniare</strong> ale datelor. Fiecare strat invata
        o reprezentare din ce in ce mai abstracta. Pe imagini: stratul 1 detecteaza muchii, stratul 3 forme,
        stratul 6 parti de obiecte, stratul final clase complete (pisica, caine, masina).</p>""", "#7C3AED")

        concept("Neuronul artificial — mecanismul exact",
                "Primeste n intrari x1..xn, fiecare ponderata cu o greutate wi. Aduna totul plus un bias b: "
                "z = w1*x1 + ... + wn*xn + b. Aplica o functie de activare nonlineara si transmite mai departe. "
                "ReLU(z) = max(0,z) este cea mai folosita: simpla, nu sufera de vanishing gradient, "
                "activeaza doar daca inputul e pozitiv, introduce sparsitate utila in retea. "
                "Sigmoid si Tanh sunt folosite doar la output layer pentru clasificare/normalizare.")

        concept("Backpropagation — cum invata reteaua",
                "Forward pass: calculeaza predictia strat cu strat, salvand activarile intermediare. "
                "Calculeaza eroarea (Loss) la final: MSE pentru regresie, Cross-Entropy pentru clasificare binara. "
                "Backward pass: propagarea erorii inapoi prin retea folosind regula lantului (chain rule) — "
                "calculeaza cat a contribuit fiecare greutate la eroarea finala (gradientul). "
                "Gradient Descent: actualizeaza fiecare greutate: w = w - lr * dLoss/dw. "
                "Adam optimizer ajusteaza learning rate-ul per parametru — mult mai eficient decat SGD simplu.")

        concept("Vanishing Gradient — problema clasica",
                "In retele adanci, gradientul se inmulteste la fiecare strat in backward pass. "
                "Daca activarile Sigmoid produc valori intre 0 si 1, gradientii se multiplica si "
                "devin exponential mici — straturile din fata aproape ca nu mai invata (dispar). "
                "Solutii moderne: ReLU in loc de Sigmoid, Batch Normalization (normalizeaza activarile "
                "intre straturi), Residual Connections (aduna inputul peste output — ResNet).")

        st.markdown(
            '<div class="formula">'
            'z = w1*x1 + w2*x2 + ... + wn*xn + b\n'
            'a = ReLU(z) = max(0, z)\n\n'
            'Loss (regresie):       MSE = (1/n)*sum((y-y_pred)^2)\n'
            'Loss (clasificare):    CrossEntropy = -sum(y*log(y_pred))\n\n'
            'Actualizare Adam:      m = beta1*m + (1-beta1)*grad\n'
            '                       v = beta2*v + (1-beta2)*grad^2\n'
            '                       w = w - lr * m / (sqrt(v) + eps)'
            '</div>', unsafe_allow_html=True)

        case_study("Clasificarea automata a radiografiilor pulmonare (spital)",
                   """<ul>
                   <li><strong>Problema:</strong> clasificarea automata a 50.000 radiografii toracice in 14 categorii de patologii</li>
                   <li><strong>Model de baza:</strong> DenseNet-121 pre-antrenat pe ImageNet (8 milioane parametri)</li>
                   <li><strong>Transfer Learning:</strong> ingheti primele 80% din straturi, fine-tunezi ultimele 20% pe radiografii</li>
                   <li><strong>Date de antrenament:</strong> 40.000 radiografii cu 14 etichete binare per imagine (multi-label)</li>
                   <li><strong>Rezultat:</strong> AUC medie 0.84 pe 14 patologii vs 0.73 cu SVM pe features HOG clasice</li>
                   <li><strong>Interpretabilitate:</strong> Grad-CAM vizualizeaza ce zone din radiografie a activat reteaua — esential pentru acceptarea clinica</li>
                   <li><strong>Deployment:</strong> model cuantizat (INT8) ruleaza in 95ms pe CPU — nu necesita GPU in productie</li>
                   </ul>""")

    with col2:
        layer_sizes = [3, 5, 5, 4, 2]
        layer_names = ["Input\n(3 features)", "Hidden 1\n(5 neuroni)", "Hidden 2\n(5 neuroni)",
                       "Hidden 3\n(4 neuroni)", "Output\n(2 clase)"]
        layer_colors = ["#0891B2", "#7C3AED", "#7C3AED", "#7C3AED", "#D97706"]
        spacing_x = 1.9

        fig = go.Figure()
        node_pos = {}
        for li, (size, col_n) in enumerate(zip(layer_sizes, layer_colors)):
            x = li * spacing_x
            ys = np.linspace(0.5, 4.5, size)
            for ni, y in enumerate(ys):
                node_pos[(li, ni)] = (x, y)
                fig.add_trace(go.Scatter(x=[x], y=[y], mode='markers',
                    marker=dict(size=28, color=col_n, line=dict(color="white", width=2)),
                    showlegend=False, hoverinfo='none'))
            fig.add_annotation(x=x, y=-0.3, text=f"<b>{layer_names[li]}</b>",
                showarrow=False, font=dict(size=9, color="#64748B"))

        np.random.seed(5)
        for li in range(len(layer_sizes)-1):
            for ni in range(layer_sizes[li]):
                for nj in range(layer_sizes[li+1]):
                    if np.random.rand() > 0.25:
                        x0, y0 = node_pos[(li, ni)]
                        x1, y1 = node_pos[(li+1, nj)]
                        w = np.random.uniform(0.3, 1.0)
                        fig.add_trace(go.Scatter(x=[x0, x1], y=[y0, y1], mode='lines',
                            line=dict(color="#CBD5E1", width=w*0.8),
                            showlegend=False, hoverinfo='none'))

        fig.add_annotation(x=0.5, y=-0.8, ax=7.1, ay=-0.8,
            text="<b>backpropagation</b>", showarrow=True, arrowhead=2,
            arrowcolor="#EF4444", font=dict(size=10, color="#EF4444"),
            axref="x", ayref="y")

        fig.update_layout(
            plot_bgcolor="white", paper_bgcolor="white",
            height=320, margin=dict(l=0, r=0, t=10, b=45),
            xaxis=dict(visible=False, range=[-0.5, 8.2]),
            yaxis=dict(visible=False, range=[-1.2, 5.2]),
        )
        st.plotly_chart(fig, use_container_width=True)

        section_title("Cum verifici modelul — in detaliu")
        verify_section("""<ul>
        <li><strong>Learning curves (Loss per epoca):</strong> traseaza train_loss si val_loss pe acelasi grafic dupa fiecare epoca.
            Ambele scad si converg impreuna = bun. Val_loss incepe sa creasca dupa N epoci = overfitting, aplica Early Stopping.
            Ambele Loss raman mari = underfitting — mareste capacitatea retelei sau antreneaza mai multe epoci.</li>
        <li><strong>Gradient flow monitoring:</strong> daca gradientii straturilor timpurii sunt aproape 0, ai vanishing gradient.
            Verifica: histogramele gradientilor per strat in TensorBoard. Solutie: schimba activarea la ReLU, adauga BatchNorm,
            sau foloseste arhitecturi cu residual connections (ResNet, DenseNet).</li>
        <li><strong>Regularizare si monitorizare gap:</strong> Dropout (dezactiveaza aleator p% din neuroni la fiecare pas —
            forteaza reteaua sa nu depinda de neuroni specifici). L2 weight decay (penalizeaza greutati mari in functia de cost).
            Monitorizeaza gap-ul train_loss vs val_loss: gap mare = prea putina regularizare, creste dropout rate sau weight decay.</li>
        <li><strong>Calibrarea probabilitatilor:</strong> o retea care produce 95% probabilitate trebuie sa aiba dreptate in 95% din cazuri.
            In practica, retelele neurale sunt adesea over-confident. Verifica cu reliability diagram (calibration_curve din sklearn).
            Aplica Temperature Scaling sau Platt Scaling post-antrenament pentru calibrare.</li>
        <li><strong>Benchmarking obligatoriu vs XGBoost:</strong> inainte de a folosi o retea neurala pe date tabelate,
            antreneaza XGBoost pe aceleasi date. Daca XGBoost da AUC 0.88 si reteaua 0.89, costul computational de 100x
            nu se justifica. Reteaua neurala aduce valoare reala cand datele sunt imagini, audio, text sau serii de timp complexe.</li>
        <li><strong>Latenta in productie:</strong> masoara inference time per exemplu pe hardware-ul tinta.
            O retea cu 100ms latenta poate procesa 10 req/sec per GPU. Daca ai nevoie de 10.000 req/sec, ai nevoie de
            optimizare: quantization INT8 (reduce memoria 4x), pruning (elimina greutati mici), sau model distillation
            (antrenezi un model mic sa imite comportamentul celui mare).</li>
        </ul>""")

        c_pro, c_con = st.columns(2)
        with c_pro:
            st.markdown("""<div class="pro-box"><h4>Avantaje</h4><ul>
            <li>Invata reprezentari automat din date brute (imagini, audio, text)</li>
            <li>Transfer learning: pornesti de la modele pre-antrenate</li>
            <li>Scalare cu date — mai multe date = mai bun</li>
            </ul></div>""", unsafe_allow_html=True)
        with c_con:
            st.markdown("""<div class="con-box"><h4>Limitari</h4><ul>
            <li>Necesita 100k+ exemple (sau transfer learning)</li>
            <li>Greu explicabil — "casuta neagra"</li>
            <li>GPU obligatoriu la scara, cost ridicat</li>
            </ul></div>""", unsafe_allow_html=True)


# =============================================================================
# SLIDE 6 — TRANSFORMERS
# =============================================================================
elif current_name == "Transformers":
    header("Transformers si Self-Attention", "Nivelul 6 — Atentia globala: fiecare element se raporteaza la toate celelalte simultan", "#0EA5E9")

    col1, col2 = st.columns([1, 1], gap="large")

    with col1:
        card("""<h3 style="color:#0891B2;">Ce face arhitectura?</h3>
        <p>Inlocuieste procesarea secventiala (RNN/LSTM) cu <strong>atentie globala paralela</strong>.
        Fiecare element dintr-o secventa se uita simultan la toate celelalte si decide cat de mult sa
        "acorde atentie" fiecaruia. Aceasta permite paralelizare masiva pe GPU si captureaza dependente
        la distante mari in secventa.</p>""", "#0891B2")

        concept("Self-Attention — mecanismul exact",
                "Fiecare token produce 3 vectori prin inmultire matriceala cu greutati invatate: "
                "Query Q (ce caut?), Key K (ce contin?), Value V (ce returnez daca sunt ales?). "
                "Scorul de atentie intre token i si token j: score(i,j) = Q_i * K_j^T / sqrt(d_k). "
                "Impartim la sqrt(d_k) pentru a stabiliza gradientii: scoruri mari duc la gradientii mici din softmax. "
                "Softmax normalizeaza scorurile in probabilitati. Outputul lui i este suma ponderata a tuturor V_j.")

        concept("Multi-Head Attention — de ce mai multe capete",
                "In loc de un singur mecanism de atentie, Transformerul ruleaza H mecanisme in paralel (H=8 sau H=16). "
                "Fiecare cap invata sa acorde atentie pentru motive diferite: "
                "capul 1 poate fi specializat pe dependente sintactice (subiect-verb), "
                "capul 2 pe co-referinte ('el' se refera la 'Ion'), capul 3 pe relatii semantice. "
                "Concatenam outputurile tuturor capetelor si aplicam o proiectie liniara finala.")

        concept("Positional Encoding — de ce e necesar",
                "Spre deosebire de RNN care proceseaza secvential si stie ordinea implicit, Transformerul "
                "proceseaza toti tokenii simultan — nu stie care e primul. "
                "Solutia: adaugam un vector de pozitie la fiecare token inainte de atentie. "
                "Encodingul original (Vaswani 2017) foloseste sin/cos cu frecvente diferite per dimensiune. "
                "Modelele moderne folosesc Rotary Position Embedding (RoPE) sau ALiBi — mai robuste la secvente lungi.")

        st.markdown(
            '<div class="formula">'
            'Attention(Q,K,V) = softmax( Q*K^T / sqrt(dk) ) * V\n\n'
            'MultiHead(Q,K,V) = Concat(head1,...,headH) * W_o\n'
            '  headi = Attention(Q*Wi_q, K*Wi_k, V*Wi_v)\n\n'
            'Transformer Block:\n'
            '  x = x + MultiHeadAttn(LayerNorm(x))   <- residual\n'
            '  x = x + FFN(LayerNorm(x))             <- feed-forward\n'
            '  FFN(x) = max(0, x*W1+b1)*W2+b2        <- 2 straturi liniare'
            '</div>', unsafe_allow_html=True)

        case_study("Fine-tuning BERT pentru analiza contractelor juridice (firma de avocatura)",
                   """<ul>
                   <li><strong>Problema:</strong> identificarea automata a clauzelor abuzive in contracte de leasing (22 tipuri de clauze)</li>
                   <li><strong>Model de baza:</strong> BERT-base-multilingual (110M parametri, pre-antrenat pe 104 limbi inclusiv romana)</li>
                   <li><strong>Strategie fine-tuning:</strong> ingheteaza primele 8 straturi, fine-tunezi ultimele 4 + capul de clasificare, 4 epoci, lr=2e-5, batch=16</li>
                   <li><strong>Date:</strong> 3.200 contracte etichetate manual de avocati (6 saptamani de munca)</li>
                   <li><strong>Rezultat:</strong> F1-macro 88.7% pe 22 tipuri de clauze vs 71.2% cu TF-IDF + SVM</li>
                   <li><strong>Vizualizare atentie:</strong> capul de atentie 5 s-a specializat pe negatii si exceptii ("nu se aplica", "cu exceptia") — avocatii au confirmat ca acestea sunt indicatori cheie de clauze abuzive</li>
                   <li><strong>ROI:</strong> analiza unui contract redusa de la 2 ore la 8 minute, cu review uman doar pe clauzele flagate cu scor > 0.7</li>
                   </ul>""")

    with col2:
        section_title("Vizualizare self-attention interactiva")
        st.caption("Apasa pe un cuvant pentru a vedea distributia atentiei sale. Galben = atentie mare, albastru = atentie medie.")

        sentence = ["Banca", "de", "pe", "malul", "raului", "era", "umbrita"]
        attn_w = np.array([
            [0.50, 0.28, 0.18, 0.90, 0.85, 0.09, 0.13],
            [0.38, 0.92, 0.62, 0.18, 0.09, 0.28, 0.18],
            [0.19, 0.48, 0.91, 0.38, 0.28, 0.19, 0.09],
            [0.82, 0.19, 0.29, 0.91, 0.72, 0.09, 0.19],
            [0.72, 0.09, 0.29, 0.82, 0.91, 0.13, 0.19],
            [0.09, 0.28, 0.19, 0.09, 0.13, 0.92, 0.72],
            [0.13, 0.19, 0.09, 0.19, 0.19, 0.72, 0.91],
        ])

        if "attn_token" not in st.session_state:
            st.session_state.attn_token = 0

        tok_cols = st.columns(len(sentence))
        for i, (ct, word) in enumerate(zip(tok_cols, sentence)):
            with ct:
                is_sel = st.session_state.attn_token == i
                if st.button(word, key=f"tok_{i}", use_container_width=True,
                             type="primary" if is_sel else "secondary"):
                    st.session_state.attn_token = i
                    st.rerun()

        idx = st.session_state.attn_token
        weights = attn_w[idx]
        colors_w = ["#FBBF24" if w > 0.65 else "#93C5FD" if w > 0.35 else "#E2E8F0" for w in weights]

        fig = go.Figure(go.Bar(
            y=sentence, x=weights, orientation='h',
            marker_color=colors_w, marker_line_width=0,
            text=[f"{w:.0%}" for w in weights], textposition="outside",
        ))
        fig.update_layout(
            plot_bgcolor="white", paper_bgcolor="white",
            height=215, margin=dict(l=0, r=55, t=5, b=0),
            xaxis=dict(visible=False, range=[0, 1.2]),
            yaxis=dict(tickfont=dict(size=13), autorange="reversed"),
            title=dict(text=f'Atentia lui "{sentence[idx]}" catre fiecare token',
                       font=dict(size=11, color="#64748B")),
        )
        st.plotly_chart(fig, use_container_width=True)
        st.caption("Observa: 'Banca' acorda atentie mare lui 'malul' si 'raului' — mecanismul de dezambiguizare a sensului.")

        section_title("Cum verifici modelul — in detaliu")
        verify_section("""<ul>
        <li><strong>Perplexitate (modele de limbaj generative):</strong> masoara cat de "surprins" este modelul de textul de test.
            Perplexitate = 2^(cross_entropy_loss_per_token). Mai mic = mai bun. GPT-4 are perplexitate sub 10 pe texte generale.
            Masura cea mai folosita pentru evaluarea LLM-urilor si compararea modelelor de limbaj.</li>
        <li><strong>BLEU / ROUGE (traducere, sumarizare):</strong> BLEU compara n-gramele din textul generat cu referinte umane.
            ROUGE masoara recall-ul n-gramelor (ce parte din referinta e acoperita de textul generat). Ambele sunt limitate —
            nu captureaza sensul semantic, ci doar suprapunerea lexicala. Foloseste BERTScore pentru evaluare semantica.</li>
        <li><strong>Fine-tuning monitoring — catastrophic forgetting:</strong> urmareste val_loss per epoca pe taskul de fine-tuning.
            Daca val_loss creste dupa 2-3 epoci, modelul incepe sa uite ce a invatat in pre-antrenament (catastrophic forgetting).
            Solutii: learning rate mic (2e-5 sau mai mic), freeze partial al straturilor timpurii, LoRA (Low-Rank Adaptation)
            care adauga parametri mici peste parametrii frozen — eficient si previne uitarea.</li>
        <li><strong>Hallucination rate — metrica critica in productie:</strong> masoara cu ce frecventa modelul produce
            fapte plauzibile dar false. Evaluare: RAG (Retrieval Augmented Generation) + compararea cu surse verificate.
            Metrica critica in aplicatii medicale, juridice sau financiare. Nu exista o metrica universala — definesti
            un set de intrebari cu raspunsuri verificabile si masori rata de raspunsuri incorecte.</li>
        <li><strong>Latenta si cost operational:</strong> modelele mari (GPT-4: ~1T parametri) cost sute de dolari per milion de tokeni.
            Masoara cost per query si latenta p50/p95/p99 (la ce latenta sunt 95% din requesturi?).
            Distillation: antrenezi un model mic (1-7B parametri) sa imite raspunsurile modelului mare — reduce costul 10-100x
            cu pierdere de 5-15% din calitate, acceptabila pentru majoritatea aplicatiilor de productie.</li>
        <li><strong>Vizualizarea atentiei pentru debugging:</strong> pentru modele open-source (LLaMA, Mistral), poti extrage
            matricele de atentie cu hooks in PyTorch. Identifica capetele de atentie specializate pe task-ul tau.
            Daca toate capetele arata acelasi pattern — redundanta, pot fi pruned pentru eficienta.</li>
        </ul>""")

        section_title("Modele celebre si aplicatii")
        models = [
            ("GPT-4 / Claude 3.5", "Generare text, cod, rationament, analiza multimodala"),
            ("BERT / RoBERTa",     "Intelegere text: clasificare, NER, Q&A, similaritate semantica"),
            ("ViT / DALL-E 3",     "Imagini: clasificare, generare, editare cu instructiuni"),
            ("AlphaFold 3",        "Biologie: predictia structurii proteinelor si interactiunilor moleculare"),
            ("Whisper / Wav2Vec",  "Audio: transcriere vorbire, identificare speaker, traducere"),
        ]
        for name, desc in models:
            st.markdown(f"""<div style="display:flex;align-items:flex-start;gap:10px;margin-bottom:6px;
            padding:9px 13px;background:#F0F9FF;border-radius:8px;border-left:3px solid #0EA5E9;">
            <strong style="font-size:12px;color:#164E63;min-width:120px;flex-shrink:0;">{name}</strong>
            <span style="font-size:12px;color:#475569;">{desc}</span></div>""", unsafe_allow_html=True)


# =============================================================================
# SLIDE 7 — COMPARATIE
# =============================================================================
elif current_name == "Comparatie":
    header("Comparatie Completa", "Cum alegi algoritmul potrivit pentru problema ta?", "#475569")

    section_title("Tabel comparativ detaliat")
    df_cmp = pd.DataFrame({
        "Algoritm":          ["Reg. Liniara", "Arbori Decizie", "Random Forest", "XGBoost", "Deep Learning", "Transformers"],
        "Complexitate":      ["Nivel 1",      "Nivel 2",        "Nivel 3",       "Nivel 4",  "Nivel 5",        "Nivel 6"],
        "Acuratete tipica":  ["Medie",        "Medie",          "Buna",          "Foarte buna","Foarte buna",  "Excelenta"],
        "Explicabil?":       ["Complet",      "Complet",        "Partial (SHAP)","Cu SHAP",  "Limitat",        "Limitat"],
        "Date minime":       ["50+",          "500+",           "1.000+",        "5.000+",   "100.000+",       "Miliarde*"],
        "Hardware":          ["CPU",          "CPU",            "CPU multi-core","CPU / GPU","GPU obligatoriu","GPU cluster"],
        "Timp antrenament":  ["Milisecunde",  "Secunde",        "Minute",        "Minute-ore","Ore-zile",      "Saptamani"],
        "Metrica cheie":     ["R², RMSE, MAE","Accuracy, AUC",  "OOB Score, AUC","Early stop, AUC, SHAP","Val Loss, AUC","Perplexitate, F1"],
        "Ideal pentru":      ["Preturi, salarii, prognoza liniara","Reguli explicite, scoring","Date tabelate generale","Kaggle, fintech, churn","Imagini, audio, semnale","NLP, multimodal, generare"],
    })
    st.dataframe(df_cmp, hide_index=True, use_container_width=True, height=295)
    st.caption("* Transformers pot fi fine-tunate pe 100-1000 exemple proprii pornind de la modele pre-antrenate pe miliarde de documente (transfer learning).")

    section_title("Ghid de alegere pe scenarii concrete")

    guide_data = [
        ("Putine date (sub 1.000 exemple)",
         "Incepe cu Regresia Liniara sau Logistica. Daca ai relatii neliniare simple, Arbore de Decizie cu max_depth=4. "
         "XGBoost sau Random Forest pe sub 500 de exemple vor face overfitting. SVM cu kernel RBF e o alternativa solida.",
         "#F0FDF4", "#166534", "#86EFAC"),
        ("Date tabelate structurate (CSV, baza de date)",
         "XGBoost sau LightGBM ca prima alegere serioasa. Random Forest ca baseline robust si verificare sanitate. "
         "Reteaua neurala nu aduce valoare pe date tabelate sub 100k exemple in 90% din cazuri.",
         "#EFF6FF", "#1E3A8A", "#93C5FD"),
        ("Imagini, video, semnale vizuale",
         "Transfer learning de la ResNet-50, EfficientNet-B4 sau ViT pre-antrenat pe ImageNet. "
         "Necesita GPU si minimum 1.000 imagini etichetate per clasa. Sub 200 imagini — data augmentation agresiva.",
         "#FDF4FF", "#581C87", "#D8B4FE"),
        ("Text natural, documente, chatboti",
         "BERT sau RoBERTa pentru intelegere si clasificare. GPT sau modele auto-regresive pentru generare de text. "
         "Fine-tuning pe date proprii cu LoRA (Low-Rank Adaptation) — eficient, nu necesita GPU puternic.",
         "#ECFEFF", "#164E63", "#67E8F9"),
        ("Serii de timp (meteo, financiar, IoT)",
         "Prophet sau ARIMA pentru serii simple cu sezonalitate clara. LSTM sau GRU pentru serii complexe, multivariate. "
         "Temporal Fusion Transformer (TFT) pentru serii multiple cu variabile externe si orizonturi lungi.",
         "#FFFBEB", "#78350F", "#FCD34D"),
        ("Explicabilitate obligatorie (medicina, finante, juridic)",
         "Regresie Liniara sau Logistica ca prima optiune — coeficientii sunt direct interpretabili. "
         "Arbore de Decizie cu max_depth limitat. Daca ai nevoie de performanta: XGBoost + SHAP pentru explicatii individuale per predictie.",
         "#FFF1F2", "#881337", "#FDA4AF"),
    ]

    all_cols = st.columns(3)
    for i, (title, body, bg, fg, border) in enumerate(guide_data):
        with all_cols[i % 3]:
            st.markdown(f"""<div style="background:{bg};border:1px solid {border};border-radius:12px;
            padding:14px 16px;margin-bottom:12px;min-height:140px;">
            <h4 style="margin:0 0 8px;font-size:13px;color:{fg};">{title}</h4>
            <p style="margin:0;font-size:12.5px;color:#374151;line-height:1.6;">{body}</p>
            </div>""", unsafe_allow_html=True)

    section_title("Cele mai comune greseli si cum sa le eviti")
    card("""<h3>Greseli frecvente in proiecte reale</h3>
    <ol>
        <li><strong>Sari direct la Deep Learning fara sa incerci XGBoost:</strong> pe date tabelate sub 100k exemple, XGBoost bate reteaua neurala in 90% din cazuri, in 10x mai putin timp si cu 100x mai putina complexitate operationala.</li>
        <li><strong>Optimizezi metrica gresita:</strong> pe 1% frauda si 99% tranzactii legitime, accuracy 99% se obtine spunand mereu "legitim". Optimizeaza AUC-ROC sau Precision-Recall pe clasa minora.</li>
        <li><strong>Data leakage la feature engineering:</strong> daca scalezi (StandardScaler) datele pe intregul dataset inainte de train/test split, ai "vazut" distributia datelor de test in procesul de antrenament. Fit scaler-ul DOAR pe train, aplica transform pe test.</li>
        <li><strong>Ignorati concept drift in productie:</strong> un model cu AUC 0.92 pe test din 2023 poate da AUC 0.65 in 2024 daca comportamentul utilizatorilor s-a schimbat. Monitorizeaza performanta lunar si re-antreneaza periodic.</li>
        <li><strong>Ignorati costul asimetric al erorilor:</strong> in detectia cancerului, un fals negativ costa infinit mai mult decat un fals pozitiv. Calibreaza pragul de decizie explicit in functie de costul real al fiecarui tip de eroare, nu lasa la valoarea default de 0.5.</li>
    </ol>""")


# =============================================================================
# SLIDE 8 — CONCLUZII
# =============================================================================
elif current_name == "Concluzii":
    header("Concluzii Cheie", "Ce ai invatat si cum aplici in practica", "#0F172A")

    conclusions = [
        ("1", "#059669",
         "Simplu functioneaza mai des decat crezi",
         "Regresia Liniara si Arborii de Decizie rezolva o proportie surprinzator de mare din problemele reale de business. "
         "Incepe intotdeauna cu modelul cel mai simplu. Daca RMSE-ul sau AUC-ROC-ul lui e acceptabil pentru costul de business, ai terminat. "
         "Complexitatea suplimentara inseamna mai greu de debugat, mai greu de explicat si mai scump de intretinut in productie."),
        ("2", "#0891B2",
         "Fiecare algoritm adauga exact o idee noua — intelege ideea, nu formula",
         "Bagging (Random Forest) = arbori independenti, votul majoritar reduce varianta. "
         "Boosting (XGBoost) = corectare secventiala a erorilor, reduce si varianta si bias-ul. "
         "Backpropagation (Retele Neurale) = gradient descent prin straturi pentru invatarea reprezentarilor. "
         "Self-Attention (Transformers) = relatii globale paralele, captureaza dependente la distante mari. "
         "Daca intelegi aceste patru idei, intelegi 90% din ML modern."),
        ("3", "#D97706",
         "XGBoost este standardul de facto pentru date tabelate — invata-l bine",
         "In competitii Kaggle si in industrie (fintech, retail, medicina), XGBoost si LightGBM domina problemele pe date structurate. "
         "Sunt robuste la valori lipsa, rapide, au regularizare incorporata si pot fi explicate cu SHAP individual per predictie. "
         "Adauga SHAP la orice model XGBoost pus in productie — vei putea explica fiecare decizie clientilor sau regulatorilor."),
        ("4", "#7C3AED",
         "Verificarea modelului este la fel de importanta ca antrenamentul",
         "Un model cu 99% accuracy pe date dezechilibrate poate fi complet inutil (spune mereu clasa majoritara). "
         "Un model cu AUC 0.92 pe test din 2023 poate da AUC 0.65 in productie in 2024 daca datele s-au schimbat (concept drift). "
         "Foloseste cross-validation, alege metrica care reflecta costul real al erorilor, calibreaza probabilitatile si monitorizeaza continuu."),
        ("5", "#EF4444",
         "Complexitate mai mare nu inseamna performanta mai buna — intotdeauna",
         "Un Transformer cu 7 miliarde de parametri pe 500 de exemple va face overfitting catastrofal. "
         "Numarul de parametri al modelului trebuie sa fie proportional cu cantitatea si complexitatea datelor. "
         "Regula practica: incepe cu modelul simplu, creste complexitatea pas cu pas si masoara cu metrici riguroase la fiecare pas. "
         "Benchmarking obligatoriu: compara intotdeauna noul model cu cel mai simplu model relevant — diferenta trebuie sa justifice costul."),
    ]

    for num, color, title, text in conclusions:
        st.markdown(f"""<div class="concl-item">
        <div class="concl-num" style="color:{color};">{num}</div>
        <div>
            <p style="font-weight:600;color:#0F172A;margin:0 0 5px;font-size:14px;">{title}</p>
            <p class="concl-text">{text}</p>
        </div></div>""", unsafe_allow_html=True)

    st.markdown("""<div class="quote-box">
    <p>"All models are wrong, but some are useful." — George Box, statistician, 1976</p>
    </div>""", unsafe_allow_html=True)

    section_title("Plan concret de invatare")
    col1, col2, col3 = st.columns(3)
    with col1:
        card("""<h3 style="color:#059669;">Saptamana 1-2</h3>
        <ul>
            <li>Instaleaza scikit-learn, pandas, plotly</li>
            <li>Aplica Regresia Liniara pe California Housing dataset</li>
            <li>Invata sa interpretezi R², RMSE, analiza rezidualuri</li>
            <li>Faci un Arbore de Decizie si vizualizezi split-urile cu plot_tree</li>
            <li>Intelegi confusion matrix si AUC-ROC pe date dezechilibrate</li>
        </ul>""", "#059669")
    with col2:
        card("""<h3 style="color:#D97706;">Luna 1</h3>
        <ul>
            <li>Random Forest cu OOB Score si Feature Importance</li>
            <li>XGBoost cu early stopping si SHAP summary plot</li>
            <li>Cross-validation stratificat si GridSearchCV</li>
            <li>Kaggle: Titanic (clasificare) si House Prices (regresie)</li>
            <li>MLflow pentru tracking experimente — habit esential</li>
        </ul>""", "#D97706")
    with col3:
        card("""<h3 style="color:#7C3AED;">Luna 2-3</h3>
        <ul>
            <li>PyTorch: prima retea neurala de la zero pe MNIST</li>
            <li>Hugging Face: fine-tuning BERT pe text propriu cu LoRA</li>
            <li>TensorBoard: monitorizare learning curves in timp real</li>
            <li>Deployment simplu: FastAPI + model serialized cu joblib</li>
            <li>Monitoring productie: data drift cu Evidently sau NannyML</li>
        </ul>""", "#7C3AED")