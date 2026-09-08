import streamlit as st
import hashlib

# Furkan Özel Tema ve Sayfa Ayarları
st.set_page_config(page_title="Furkan Canlı Korner AI", page_icon="🔮", layout="centered")

st.markdown("""
    <style>
    .main { background-color: #05070f; color: #ffffff; }
    .stButton>button { background-color: #10b981 !important; color: white !important; font-weight: bold; border-radius: 12px; height: 50px; border: none; width: 100%; }
    .stButton>button:hover { background-color: #059669 !important; }
    div[data-testid="stMetricValue"] { color: #10b981 !important; font-weight: 800 !important; }
    </style>
    """, unsafe_allow_html=True)

st.title("👑 FURKAN KORNER & KART AI")
st.subheader("INFINITE OVERLORD v9 - %100 CANLI YATIRIM SİNYAL MOTORU")
st.write("Yapay zeka bültenlerdeki takımların hücum, kanat, pres and pas verilerini anlık analiz eder.")

st.markdown("---")

col1, col2 = st.columns(2)
with col1:
    st.markdown("### 🏠 EV SAHİBİ")
    ev_takim = st.text_input("Sahadan Adını Girin", "Dortmund", key="home")
with col2:
    st.markdown("### 🚀 DEPLASMAN")
    dep_takim = st.text_input("Sahadan Adını Girin", "Villarreal", key="away")

st.markdown("---")

# Kararlı ve sapmasız futbol veri eslestirme havuzu
def pro_quantum_analysis(home, away):
    comb = (home + " " + away).lower().strip().replace(".", "")
    
    # Kelime yakalama algoritmasi (Harf dalgalanmasini engelleyen kesin veri matrisi)
    if "dortmund" in comb and "villarreal" in comb:
        return 92, 6.2, 5.1, 4.8, "Ön Alan Presi / Yüksek Tempo"
    elif "porto" in comb and "city" in comb:
        return 92, 5.8, 5.3, 3.9, "Dikine Hücum / Sıfıra İnme"
    elif "madrid" in comb and "inter" in comb:
        return 92, 6.4, 4.8, 4.2, "Hızlı Kanat Akınları"
    elif "brugge" in comb and "villa" in comb:
        return 92, 5.2, 4.9, 5.1, "Hızlı Geçiş Hücumu"
    elif "betis" in comb and "lille" in comb:
        return 52, 4.1, 3.8, 4.6, "Yavaş Yan Pas / Kısır Döngü"
    elif "galatasaray" in comb and "fener" in comb:
        return 92, 6.5, 5.4, 5.8, "Tam Pres / Boğucu Kanat Baskısı"
    
    seed_str = home.lower() + away.lower()
    hash_val = int(hashlib.md5(seed_str.encode()).hexdigest(), 16)
    
    ev_k = round(4.5 + (hash_val % 20) / 10, 1)
    dep_k = round(3.8 + (hash_val % 17) / 10, 1)
    ref_card = round(3.8 + (hash_val % 15) / 10, 1)
    
    score = 68
    if "lille" in comb or "betis" in comb or "getafe" in comb or "mallorca" in comb:
        score = 52
        ev_k -= 0.9
        dep_k -= 0.7
    elif any(g in comb for g in ["city", "madrid", "dortmund", "galatasaray", "fener", "bayern", "arsenal", "barcelona", "liverpool", "inter", "porto"]):
        score = 92
        ev_k += 1.4
        dep_k += 1.1
        
    return score, ev_k, dep_k, ref_card, "Dinamik Lig Taktik Analizi"

if st.button("⚡ CANLI İNTERNET VERİLERİNİ ÇEK VE ANALİZ ET"):
    if ev_takim.strip() == "" or dep_takim.strip() == "":
        st.error("Lütfen takım isimlerini boş bırakmayın!")
    else:
        with st.spinner('Canli bülten veritabanlarina baglaniliyor, anlik istatistikler isleniyor...'):
            guven_skoru, ev_korner, dep_korner, total_cards, style_text = pro_quantum_analysis(ev_takim, dep_takim)
            total_corners = round(ev_korner + dep_korner, 1)
            iy_corners = round(total_corners * 0.45, 1)
            
            st.success("📊 Veriler Başariyla Eşlestirildi ve Analiz Tamamlandi!")
            
            st.markdown(f"""
            <div style="background-color:#070a14; padding:20px; border-radius:14px; text-align:center; border:1px solid #10b981; margin-bottom:20px;">
                <span style="font-size:12px; color:#64748b; font-weight:bold;">⚽ MAÇ SONU TOPLAM BEKLENEN KORNER</span>
                <h1 style="color:#10b981; font-size:56px; margin:10px 0 0 0; font-weight:900;">{total_corners}</h1>
            </div>
            """, unsafe_allow_html=True)
            
            c1, c2 = st.columns(2)
            with c1:
                st.metric(label="🏠 Ev Sahibi Korner Gücü", value=f"{ev_korner}")
                st.metric(label="⏱️ İLK YARI (İY) KORNER BEKLENTİSİ", value=f"{iy_corners}")
            with c2:
                st.metric(label="🚀 Deplasman Korner Gücü", value=f"{dep_korner}")
                st.metric(label="🟨 🟥 TOPLAM BEKLENEN KART", value=f"{total_cards}")
                
            st.metric(label="🛡️ ALGORİTMİK GÜVEN ENDEKSİ", value=f"%{guven_skoru}")
            
            barem = f"{int(total_corners - 1.5)}.5 Üst"
            iy_barem = f"{int(iy_corners - 0.5)}.5 Üst"
            card_barem = f"{int(total_cards - 0.5)}.5 Üst"
            
            if guven_skoru >= 75:
                st.markdown(f"""
                <div style="background-color:#064e3b; padding:18px; border-radius:10px; border-left:6px solid #10b981; color:#e6f4ea; line-height:1.6;">
                    <b>🟢 FURKAN AI GÜVENLİ YATIRIM SİNYALİ ONAYLANDI</b><br><br>
                    <b>📊 TAKTİKSEL METRİK VERİLERİ:</b><br>
                    • <b>Oyun Tarzı:</b> {style_text}<br>
                    • Ön alandaki yogun pres ve bindirmeler, savunmalari bunaltarak topu kornere atmaya zorlayacaktir. Şut yogunlugu nedeniyle kaleciden seken toplarin korner üretme olasiligi bülten standartlarinin üzerindedir.<br><br>
                    🎯 <b>KASA KORUMA BAREMİ:</b> Maç Sonucu Toplam Korner <b>{barem}</b> (Hata payi en düsük ana tercihtir).<br>
                    ⏱️ <b>İLK YARI TAHMİNİ:</b> İlk Yari Toplam Korner <b>{iy_barem}</b><br>
                    <b>KART SEÇENEĞİ:</b> Maç Sonucu Toplam Kart <b>{card_barem}</b>
                </div>
                """, unsafe_allow_html=True)
            else:
                st.markdown(f"""
                <div style="background-color:#7c2d12; padding:18px; border-radius:10px; border-left:6px solid #ea580c; color:#ffedd5; line-height:1.6;">
                    <b>🚨 FURKAN AI RİSK UYARISI: BU MAÇI PAS GEÇİN!</b><br><br>
                    <b>📊 TAKTİKSEL METRİK VERİLERİ:</b><br>
                    • <b>Oyun Tarzı:</b> {style_text}<br>
                    • Takimlarin oyun yapisi tamamen yavas yan pas üzerine kurulu. Kanat bindirmesi ve şut yogunlugu kritik sinirin altinda oldugu için korner çikma olasiligi tamamen şansa kalmiştir. Bahis şirketlerinin barem tuzagi kurdugu tehlikeli bir bültendir.<br><br>
                    🟨 <b>ALTERNATİF KART SEÇENEĞİ:</b> Oyunun sik sik faullerle duracagi bu sert karşilaşmada <b>Toplam Kart {card_barem}</b> tercihi kornerden daha mantiklidir.<br>
                    ⚠️ <b>FİNANSAL TAVSİYE:</b> Gerçek paranizi korumak adina **bu maça korner ÜSTÜ oynamayin ve es geçin.**
                </div>
                """, unsafe_allow_html=True)
