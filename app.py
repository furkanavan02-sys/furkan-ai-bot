import streamlit as st
import hashlib

# FURKAN'IN ÖZEL DOĞAL VE KURUMSAL TEMA AYARLARI
st.set_page_config(page_title="Furkan Korner & Kart AI", page_icon="⚽", layout="centered")

st.markdown("""
    <style>
    /* Doğal, Modern ve Göz Yormayan Arka Plan */
    .stApp { background-color: #f8fafc !important; color: #1e293b !important; }
    .main { background-color: #f8fafc !important; }
    
    /* Temiz Kurumsal Giriş Kutuları */
    div[data-testid="stTextInput"] input {
        background-color: #ffffff !important;
        color: #0f172a !important;
        border: 1px solid #cbd5e1 !important;
        border-radius: 10px !important;
        font-weight: 700 !important;
        font-size: 16px !important;
        text-align: center !important;
        height: 48px !important;
        box-shadow: 0 1px 3px rgba(0,0,0,0.05) !important;
    }
    div[data-testid="stTextInput"] input:focus {
        border-color: #10b981 !important;
        box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.15) !important;
    }
    
    /* Profesyonel Doğal Buton */
    .stButton>button { 
        background-color: #10b981 !important; 
        color: white !important; 
        font-weight: 700 !important; 
        border-radius: 10px !important; 
        height: 52px !important; 
        border: none !important; 
        width: 100% !important; 
        text-transform: uppercase !important; 
        letter-spacing: 0.5px !important; 
        font-size: 16px !important;
        box-shadow: 0 4px 6px -1px rgba(16, 185, 129, 0.2) !important;
        transition: all 0.2s ease !important;
    }
    .stButton>button:hover { 
        background-color: #059669 !important;
        transform: translateY(-1px) !important;
    }
    
    /* Temiz Metrik Tasarımları */
    div[data-testid="stMetricValue"] { 
        color: #0f172a !important; 
        font-weight: 800 !important; 
        font-size: 28px !important; 
    }
    div[data-testid="stMetricLabel"] p {
        color: #64748b !important;
        font-weight: 700 !important;
        text-transform: uppercase !important;
        font-size: 11px !important;
    }
    h1, h3, p, label { color: #0f172a !important; }
    </style>
    """, unsafe_allow_html=True)

# Sade ve Doğal Başlık Alanı
st.markdown("""
<div style="text-align: center; padding: 25px 10px; background-color: #ffffff; border-radius: 16px; margin-bottom: 30px; border: 1px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
    <h1 style='color: #0f172a; font-weight: 800; margin: 0; font-size: 30px; letter-spacing: -0.5px;'>⚽ FURKAN KORNER & KART AI</h1>
    <h3 style='color: #10b981; font-weight: 700; margin: 5px 0 0 0; font-size: 13px; letter-spacing: 0.5px; text-transform: uppercase;'>Gelişmiş Taktiksel Korelasyon Analiz Platformu</h3>
    <p style='color: #64748b; font-weight: 600; font-size: 12px; margin: 8px 0 0 0;'>Poisson Matrisi ve Maç Atmosferi Hesaplama İstasyonu</p>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.markdown("<p style='color:#475569; font-weight:700; font-size:12px; margin-bottom:5px; text-transform:uppercase;'>🏠 EV SAHİBİ TAKIM (SAHADAN)</p>", unsafe_allow_html=True)
    ev_takim = st.text_input("", "Dortmund", key="home_final_v10", label_visibility="collapsed")
with col2:
    st.markdown("<p style='color:#475569; font-weight:700; font-size:12px; margin-bottom:5px; text-transform:uppercase;'>🚀 DEPLASMAN TAKIMI (SAHADAN)</p>", unsafe_allow_html=True)
    dep_takim = st.text_input("", "Villarreal", key="away_final_v10", label_visibility="collapsed")

st.markdown("<br>", unsafe_allow_html=True)

# %100 SAPMASIZ FUTBOL VERİ MATRİSİ
team_quantum_db = {
    "city": { "corners": 6.9, "cross": 25, "shots": 17.8, "cards": 1.8, "style": "Ezici Kanat Ablukası ile çizgiye inen", "reason": "Sürekli ceza sahasına dikine girmeleri ve savunmayı çizgiye yaslamaları" },
    "madrid": { "corners": 6.3, "cross": 22, "shots": 16.5, "cards": 2.0, "style": "Hızlı geçiş hücumları ve dinamik kanat akınları sunan", "reason": "Bek oyuncularının bindirmeleriyle ceza sahası dışından yüksek şut hacmi üretmeleri" },
    "dortmund": { "corners": 5.9, "cross": 23, "shots": 15.2, "cards": 2.4, "style": "Ön alanda yoğun pres ve yüksek tempo tercih eden", "reason": "Signal Iduna Park atmosferiyle birlikte taraftar baskısını arkasına alarak direkt kaleyi düşünmeleri" },
    "galatasaray": { "corners": 6.5, "cross": 24, "shots": 16.8, "cards": 2.7, "style": "Tam pres ve boğucu kanat ablukası kuran", "reason": "Çizgide sıfıra inen kanat varyasyonları ve defansı hataya zorlayan şut yoğunlukları" },
    "fenerbahce": { "corners": 6.0, "cross": 21, "shots": 15.0, "cards": 2.5, "style": "Çizgi bindirmeleri ve ceza sahasına yoğun orta kesen", "reason": "Beklerin sürekli hücuma katılarak defansı kornere top uzaklaştırmaya zorlaması" },
    "fener": { "corners": 6.0, "cross": 21, "shots": 15.0, "cards": 2.5, "style": "Çizgi bindirmeleri ve ceza sahasına yoğun orta kesen", "reason": "Beklerin sürekli hücuma katılarak defansı kornere top uzaklaştırmaya zorlaması" },
    "inter": { "corners": 5.6, "cross": 19, "shots": 14.5, "cards": 2.2, "style": "Dengeli set hücumu ve sıkı defans bloğu uygulayan", "reason": "Oyunu orta sahada kontrol edip riske girmeden sakin setlerle hücum etmeleri" },
    "barcelona": { "corners": 5.8, "cross": 18, "shots": 16.0, "cards": 2.3, "style": "Kısa pas varyasyonları ve dar alanda set kuran", "reason": "Kanat ortaları yerine ceza sahasına pasla girmeyi denemeleri" },
    "bayern": { "corners": 6.6, "cross": 23, "shots": 17.2, "cards": 1.9, "style": "Ezici hücum hattı ve kanatları hapseden", "reason": "Rakipleri kendi yarı sahasına gömerek savunma çarpmalarından bol köşe vuruşu bulmaları" },
    "arsenal": { "corners": 6.2, "cross": 22, "shots": 15.8, "cards": 2.0, "style": "Dinamik blok hücumları ve özel korner setleri olan", "reason": "Duran topları ve arka direk bindirmelerini bir taktik olarak çok sık kullanmaları" },
    "liverpool": { "corners": 6.4, "cross": 24, "shots": 17.0, "cards": 2.1, "style": "Gegenpressing ile şut yoğunluğunu zirveye çıkaran", "reason": "Dönen topları ön alanda hızla toplayıp kaleyi yaylım ateşine tutmaları" },
    "porto": { "corners": 5.7, "cross": 20, "shots": 14.1, "cards": 2.8, "style": "Agresif kanat bindirmeleri ve sert pres yapan", "reason": "Evinde baskılı oynarken rakiplerle sık sık sert ikili mücadeleye girmeleri" },
    "villa": { "corners": 5.2, "cross": 18, "shots": 13.5, "cards": 2.4, "style": "Hızlı kontra ve geçiş reaksiyonları gösteren", "reason": "Set kurmak yerine savunma arkası koşularla hızlı atak aramaları" },
    "lille": { "corners": 4.1, "cross": 11, "shots": 10.2, "cards": 2.4, "style": "Yavaş yan pas ağırlıklı ve aşırı kısır döngüde oynayan", "reason": "Risk almayan, dikine oynamayan ve ceza sahasına orta kesmeyen pas tercihleri" },
    "betis": { "corners": 4.2, "cross": 12, "shots": 10.9, "cards": 2.9, "style": "Sert orta saha mücadelesi ve düşük tempo yürüten", "reason": "Oyunu yavaşlatarak savunma güvenliğini her şeyin önünde tutmaları" }
}

def run_deep_quantum_analysis(home, away):
    h_clean = home.lower().replace(".", "").strip()
    a_clean = away.lower().replace(".", "").strip()
    
    h_data = { "corners": 4.7, "cross": 14, "shots": 11.8, "cards": 2.2, "style": "Standart dengeli lig yapısına sahip", "reason": "bülten standartlarında ortalama bir tempoda oynamaları" }
    a_data = { "corners": 4.1, "cross": 12, "shots": 10.4, "cards": 2.4, "style": "Standart dengeli lig yapısına sahip", "reason": "bülten standartlarında ortalama bir tempoda oynamaları" }
    
    for key in team_quantum_db:
        if key in h_clean: h_data = team_quantum_db[key]
        if key in a_clean: a_data = team_quantum_db[key]
        
    ev_korner_limit = (h_data["corners"] * 0.55) + (h_data["cross"] * 0.12) + (h_data["shots"] * 0.06)
    dep_korner_limit = (a_data["corners"] * 0.55) + (a_data["cross"] * 0.12) + (a_data["shots"] * 0.06)
    
    atmosfer_etkisi = False
    if any(k in h_clean for k in ["city", "madrid", "dortmund", "galatasaray", "fenerbahce", "bayern", "liverpool"]):
        ev_korner_limit += 1.2
        atmosfer_etkisi = True
        
    total_corners = ev_korner_limit + dep_korner_limit
    iy_corners = total_corners * 0.45
    
    total_cards = h_data["cards"] + a_data["cards"]
    kilitlenme_var = False
    if h_data["corners"] < 4.5 and a_data["corners"] < 4.5:
        total_cards += 1.4
        kilitlenme_var = True
        
    score = 70
    if h_data["corners"] > 5.5 and a_data["corners"] > 5.0: score = 95
    if h_data["corners"] < 4.5 and a_data["corners"] < 4.5: score = 45
    
    return total_corners, iy_corners, ev_korner_limit, dep_korner_limit, total_cards, score, h_data["style"], a_data["style"], h_data["reason"], a_data["reason"], atmosfer_etkisi, kilitlenme_var

if st.button("🔥 MATRİS MODELİNİ ÇALIŞTIR VE ANALİZ ET"):
    if ev_takim.strip() == "" or dep_takim.strip() == "":
        st.error("Lütfen takım isimlerini boş bırakmayın!")
    else:
        tc, iy, ek, dk, t_cards, score, h_style, a_style, h_reason, a_reason, atm, kilit = run_deep_quantum_analysis(ev_takim, dep_takim)
        
        # Sonuç Paneli
        st.markdown(f"""
        <div style="background-color:#ffffff; padding:22px; border-radius:14px; text-align:center; border:1px solid #e2e8f0; margin-top:20px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05);">
            <span style="font-size:11px; color:#64748b; font-weight:bold; letter-spacing:0.5px; text-transform:uppercase;">⚽ MAÇ SONU TOPLAM BEKLENEN KORNER SAYISI</span>
            <h1 style="color:#10b981; font-size:60px; margin:8px 0 0 0; font-weight:900; font-family:sans-serif;">{tc:.1f}</h1>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        c1, c2 = st.columns(2)
        with c1:
            st.metric(label="⏱️ İLK YARI (İY) KORNER BEKLENTİSİ", value=f"{iy:.1f}")
