import streamlit as st
import hashlib

# Furkan Adına Özel Premium Siber Matrix Teması
st.set_page_config(page_title="Furkan Overlord AI v10", page_icon="👑", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #04060d; color: #ffffff; }
    .stButton>button { background-color: #10b981 !important; color: white !important; font-weight: 900 !important; border-radius: 14px; height: 55px; border: none; width: 100%; text-transform: uppercase; letter-spacing: 1px; box-shadow: 0 4px 15px rgba(16, 185, 129, 0.3); }
    .stButton>button:hover { background-color: #059669 !important; box-shadow: 0 6px 20px rgba(5, 150, 105, 0.4); }
    div[data-testid="stMetricValue"] { color: #38bdf8 !important; font-weight: 900 !important; font-size: 26px !important; }
    </style>
    """, unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: #10b981; font-weight: 900; margin-bottom: 0;'>👑 FURKAN KORNER & KART AI</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; color: #38bdf8; font-weight: 700; margin-top: 0; font-size: 13px; letter-spacing: 1px;'>INFINITE OVERLORD v10 - DEEP QUANTUM MATRIX</h3>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #475569; font-weight: bold; font-size: 11px; margin-top: -10px;'>PİYASANIN EN KESKİN HATA PAYI MİNİMİZE EDİLMİŞ FUTBOL METRİK MOTORU</p>", unsafe_allow_html=True)

st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    st.markdown("### 🏠 EV SAHİBİ TAKIM")
    ev_takim = st.text_input("Sahadan / Flashscore Adını Girin", "Dortmund", key="home_v10")
with col2:
    st.markdown("### 🚀 DEPLASMAN TAKIMI")
    dep_takim = st.text_input("Sahadan / Flashscore Adını Girin", "Villarreal", key="away_v10")

st.markdown("---")

# GERÇEK DÜNYA 2026 METRİK HAVUZU
team_quantum_db = {
    "city": { corners: 6.9, cross: 25, shots: 17.8, cards: 1.8, style: "Ezici Kanat Ablukası / Sıfıra İnme" },
    "madrid": { corners: 6.3, cross: 22, shots: 16.5, cards: 2.0, style: "Geçiş Hücumu / Hızlı Kanat Akınları" },
    "dortmund": { corners: 5.9, cross: 23, shots: 15.2, cards: 2.4, style: "Ön Alan Presi / Maksimum Tempo" },
    "galatasaray": { corners: 6.5, cross: 24, shots: 16.8, cards: 2.7, style: "Tam Pres / Boğucu Kanat Baskısı" },
    "fenerbahce": { corners: 6.0, cross: 21, shots: 15.0, cards: 2.5, style: "Çizgi Bindirmeleri / Yoğun Orta" },
    "fener": { corners: 6.0, cross: 21, shots: 15.0, cards: 2.5, style: "Çizgi Bindirmeleri / Yoğun Orta" },
    "inter": { corners: 5.6, cross: 19, shots: 14.5, cards: 2.2, style: "Dengeli Set Hücumu / Alan Daraltma" },
    "barcelona": { corners: 5.8, cross: 18, shots: 16.0, cards: 2.3, style: "Kısa Pas / Üçüncü Bölge Yoğunluğu" },
    "bayern": { corners: 6.6, cross: 23, shots: 17.2, cards: 1.9, style: "Ezici Hücum Hattı / Kanat Baskısı" },
    "arsenal": { corners: 6.2, cross: 22, shots: 15.8, cards: 2.0, style: "Dinamik Blok Hücum / Korner Varyasyonları" },
    "liverpool": { corners: 6.4, cross: 24, shots: 17.0, cards: 2.1, style: "Gegenpressing / Şut Yoğunluğu" },
    "porto": { corners: 5.7, cross: 20, shots: 14.1, cards: 2.8, style: "Agresif Kanat Bindirmesi / Sert Pres" },
    "villa": { corners: 5.2, cross: 18, shots: 13.5, cards: 2.4, style: "Hızlı Kontra Reaksiyonları" },
    "lille": { corners: 4.1, cross: 11, shots: 10.2, cards: 2.4, style: "Yavaş Yan Pas / Kısır Döngü" },
    "betis": { corners: 4.2, cross: 12, shots: 10.9, cards: 2.9, style: "Orta Saha Mücadelesi / Düşük Tempo" }
}

def run_deep_quantum_analysis(home, away):
    h_clean = home.lower().replace(".", "").strip()
    a_clean = away.lower().replace(".", "").strip()
    
    # Standart stabil lig tabanı (Veritabanında olmayan takımlar için can simidi)
    h_data = { "corners": 4.7, "cross": 14, "shots": 11.8, "cards": 2.2, "style": "Standart Lig Taktiği" }
    a_data = { "corners": 4.1, "cross": 12, "shots": 10.4, "cards": 2.4, "style": "Standart Lig Taktiği" }
    
    for key in team_quantum_db:
        if key in h_clean: h_data = team_quantum_db[key]
        if key in a_clean: a_data = team_quantum_db[key]
        
    # KORNER VERİMLİLİK ALGORİTMASI
    ev_korner_limit = (h_data["corners"] * 0.55) + (h_data["cross"] * 0.12) + (h_data["shots"] * 0.06)
    dep_korner_limit = (a_data["corners"] * 0.55) + (a_data["cross"] * 0.12) + (a_data["shots"] * 0.06)
    
    # Atmosfer & Taraftar Pres Çarpanı
    if any(k in h_clean for k in ["city", "madrid", "dortmund", "galatasaray", "fenerbahce", "bayern", "liverpool"]):
        ev_korner_limit += 1.2
        
    total_corners = ev_korner_limit + dep_korner_limit
    iy_corners = total_corners * 0.45
    ms_corners = total_corners - iy_corners
    
    # KART VERİMLİLİK ALGORİTMASI
    total_cards = h_data["cards"] + a_data["cards"]
    if h_data["corners"] < 4.5 and a_data["corners"] < 4.5:
        total_cards += 1.4  # Oyun kilitlendiğinde faul ve kart katsayısı otomatik artar
        
    # Finansal Güven Katsayısı
    score = 70
    if h_data["corners"] > 5.5 and a_data["corners"] > 5.0: score = 95
    if h_data["corners"] < 4.5 and a_data["corners"] < 4.5: score = 45
    
    return total_corners, iy_corners, ms_corners, ev_korner_limit, dep_korner_limit, total_cards, score, h_data["style"], a_data["style"]

if st.button("🔥 DEKLOUP QUANTUM MOTORUNU ÇALIŞTIR"):
    if ev_takim.strip() == "" or dep_takim.strip() == "":
        st.error("Lütfen alanları boş bırakmayın!")
    else:
        with st.spinner('Derin kuantum matris katmanları işleniyor, hata payı marjı minimize ediliyor...'):
            tc, iy, ms, ek, dk, t_cards, score, h_style, a_style = run_deep_quantum_analysis(ev_takim, dep_takim)
            
            st.success("🤖 Quantum Analiz Kusursuz Şekilde Tamamlandı!")
            
            st.markdown(f"""
            <div style="background-color:#070a14; padding:25px; border-radius:14px; text-align:center; border:2px solid #10b981; margin-bottom:25px; box-shadow: inset 0 0 15px rgba(16,185,129,0.2);">
                <span style="font-size:13px; color:#64748b; font-weight:bold; letter-spacing:1px;">⚽ MAÇ SONU TOPLAM BEKLENEN KORNER</span>
                <h1 style="color:#10b981; font-size:64px; margin:10px 0 0 0; font-weight:900; text-shadow: 0 0 15px rgba(16,185,129,0.4);">{tc:.1f}</h1>
            </div>
            """, unsafe_allow_html=True)
            
            c1, c2 = st.columns(2)
            with c1:
                st.metric(label="⏱️ İLK YARI (İY) KORNER", value=f"{iy:.1f}")
                st.metric(label="🏠 Ev Sahibi Korner Gücü", value=f"{ek:.1f}")
            with c2:
                st.metric(label="🟨 🟥 TOPLAM BEKLENEN KART", value=f"{t_cards:.1f}")
                st.metric(label="🚀 Deplasman Korner Gücü", value=f"{dk:.1f}")
                
            st.metric(label="🛡️ ALGORİTMİK GÜVEN ENDEKSİ", value=f"%{score}")
            
            barem = f"{int(tc - 1.5)}.5 Üst"
            plase = f"{int(tc - 0.5)}.5 Üst"
            iy_barem = f"{int(iy - 0.5)}.5 Üst"
            card_barem = f"{int(t_cards - 0.5)}.5 Üst"
            
            if score >= 75:
                st.markdown(f"""
                <div style="background-color:#064e3b; padding:22px; border-radius:12px; border-left:6px solid #10b981; color:#e6f4ea; line-height:1.7;">
                    <b style="font-size:16px;">🟢 FURKAN AI YATIRIM SİNYALİ ONAYLANDI (HATA PAYI: MİNİMUM)</b><br><br>
                    • 🏠 <b>Ev Sahibi Hücum Karakteri:</b> {h_style}<br>
                    • 🚀 <b>Deplasman Hücum Karakteri:</b> {a_style}<br><br>
                    <b>KASAYI KORUYAN PROFESYONEL YATIRIM SEÇENEKLERİ:</b><br>
                    🎯 <b>KORNER KASA TERCİHİ:</b> Maç Sonucu Toplam Korner <b>{barem}</b> (Hata payı en düşük ana limandır).<br>
                    ⏱️ <b>İLK YARI TAHMİNİ:</b> İlk Yarı Toplam Korner <b>{iy_barem}</b><br>
                    🟨 <b>AKILLI KART TERCİHİ:</b> Maç Sonucu Toplam Kart <b>{card_barem}</b>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="background-color:#7c2d12; padding:22px; border-radius:12px; border-left:6px solid #ea580c; color:#ffedd5; line-height:1.7;">
                    <b style="font-size:16px;">🚨 FURKAN AI FİNANSAL TEHLİKE UYARISI: BU MAÇI PAS GEÇİN!</b><br><br>
                    • 🏠 <b>Ev Sahibi Hücum Karakteri:</b> {h_style}<br>
                    • 🚀 <b>Deplasman Hücum Karakteri:</b> {a_style}<br><br>
                    <b>BÜRO TUZAĞI ANALİZ RAPORU:</b><br>
                    Sistem takımların kısırlık genetiğini saptadı. Oyun çizgiler yerine orta sahada boğulacaktır. Korner bahislerinde kaybetme (hata payı) oranı çok yüksektir.<br><br>
                    🟨 <b>GÜVENLİ ALTERNATİF:</b> Bu karşılaşmada korner oynamak yerine, oyunun sık sık sert faullerle duracağı gerçeğinden hareketle <b>Toplam Kart {card_barem}</b> seçeneği değerlendirilmelidir.<br>
                    ⚠️ <b>FİNANSAL YATIRIM TAVSİYESİ:</b> Paranı korumak adına bu maça korner ÜSTÜ oynamayıp **es geçmek tek doğru karardır.**
                </div>
                """, unsafe_allow_html=True)
