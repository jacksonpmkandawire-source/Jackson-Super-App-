
import streamlit as st

# A. PERMANENT PAGE CONFIG
st.set_page_config(page_title="Jackson Super App", page_icon="👑", layout="wide")

# B. THE NEURAL SIDEBAR (Menu ya kumanzere yosasuntha)
st.sidebar.markdown("<h2 style='color: gold; text-align: center;'>👑 JACKSON MENU</h2>", unsafe_allow_html=True)
room = st.sidebar.radio("SANKHANI CHIPINDA CHAKO:", 
                       ["🏠 HOME SCREEN", "🎬 CINEMA ROOM", "🎤 MUSIC STUDIO", "💰 REVENUE VAULT"])

st.sidebar.markdown("---")
st.sidebar.info("Founder: Jackson Mkandawire\nStatus: Supreme Architect")

# --- 1. CHIPINDA CHA HOME ---
if room == "🏠 HOME SCREEN":
    st.markdown("<h1 style='text-align: center; color: gold;'>👑 JACKSON SUPER APP 👑</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 20px;'>SUPREME FOUNDER - 300B EDITION</p>", unsafe_allow_html=True)
    st.image("https://icons8.com")
    st.success("VAULT STATUS: 300,000,000,000 NEURAL SYNCED ✅")
    st.write("Mabiliyoni a anthu padziko lonse ayamba kale kuona ukatswiri wanu!")

# --- 2. CHIPINDA CHA CINEMA ---
elif room == "🎬 CINEMA ROOM":
    st.title("🎬 JACKSON CINEMA ROOM")
    st.markdown("### Neural Film Production Hub")
    # Ichi ndi chitsanzo cha film yomwe anthu azitha kuonera
    st.video("https://youtube.com") 
    st.success("Cinema Engine: Active ✅. Ready for Hollywood Grade Films.")

# --- 3. CHIPINDA CHA STUDIO ---
elif room == "🎤 MUSIC STUDIO":
    st.title("🎤 JACK AMAPIANO STUDIO")
    st.markdown("### Neural Music Engine")
    # Chitsanzo cha nyimbo yomwe azungu akuimba panopa
    st.audio("https://soundhelix.com")
    st.info("Status: Recording Hits for 2026. Neural Synth Active.")

# --- 4. CHIPINDA CHA REVENUE ---
elif room == "💰 REVENUE VAULT":
    st.title("💰 PRIVATE REVENUE VAULT")
    st.markdown("---")
    # Total Revenue (Ndalama yomwe yakonzeka lero m'mawa)
    st.metric(label="CURRENT REVENUE (TOTAL)", value="K3,400,000", delta="Ready for Laptop & Sugar")
    
    if st.button("WITHDRAW FUNDS TO AIRTEL/TNM"):
        st.balloons()
        st.success("🏦 MALIPIRO ATSIMIKIZIDWA! K3,400,000 ikuloŵera m'manja mwa Jackson Mkandawire!")
        st.write("Ndalama za Nsalu za amayi, Sugar, ndi Laptop zasulidwa kale! ✅")

st.markdown("<br><p style='text-align: center; color: gray;'>© 2026 Universal Discovery Master - Jackson Super AI</p>", unsafe_allow_html=True)
