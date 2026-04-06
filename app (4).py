
import streamlit as st

st.set_page_config(page_title="Jackson Super App", page_icon="👑", layout="wide")

# THE NEURAL SIDEBAR (Menu ya Mabiliyoni kumanzere)
st.sidebar.title("👑 JACKSON MENU")
room = st.sidebar.radio("SANKHANI CHIPINDA:", ["🏠 HOME SCREEN", "🎬 CINEMA ROOM", "🎤 MUSIC STUDIO", "💰 REVENUE VAULT"])

# --- CHIPINDA CHA HOME ---
if room == "🏠 HOME SCREEN":
    st.markdown("<h1 style='text-align: center; color: gold;'>👑 JACKSON SUPER APP 👑</h1>", unsafe_allow_html=True)
    st.success("VAULT STATUS: 300,000,000,000 SYNCED ✅")
    st.info("Founder: Jackson Mkandawire - Universal Discovery Master")

# --- CHIPINDA CHA CINEMA ---
elif room == "🎬 CINEMA ROOM":
    st.title("🎬 JACKSON CINEMA ROOM")
    st.video("https://youtube.com") # Chitsanzo cha Film
    st.success("Cinema Neural Hub Active! ✅ Ready for Production.")

# --- CHIPINDA CHA REVENUE ---
elif room == "💰 REVENUE VAULT":
    st.title("💰 PRIVATE REVENUE VAULT")
    st.metric(label="CURRENT REVENUE", value="K3,300,000", delta="Ready for Payout")
    if st.button("WITHDRAW TO MOBILE MONEY"):
        st.balloons()
        st.success("Chuma cha suti yatsopano tsopano chikutuluka mwaukhondo!")
