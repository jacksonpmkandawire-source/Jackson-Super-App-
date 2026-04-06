
import streamlit as st

st.set_page_config(page_title="Jackson Super App", page_icon="👑", layout="wide")

# NAVIGATION (Mabatani a Zipinda)
st.sidebar.title("👑 JACKSON MENU")
room = st.sidebar.radio("SANKHANI CHIPINDA:", ["HOME SCREEN", "🎬 CINEMA ROOM", "🎤 MUSIC STUDIO", "💰 REVENUE VAULT"])

# --- CHIPINDA CHA HOME ---
if room == "HOME SCREEN":
    st.markdown("<h1 style='text-align: center; color: gold;'>👑 JACKSON SUPER APP 👑</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; color: white;'>SUPREME FOUNDER EDITION</p>", unsafe_allow_html=True)
    st.image("https://icons8.com", use_column_width=False)
    st.success("VAULT STATUS: 300,000,000,000 SYNCED ✅")

# --- CHIPINDA CHA CINEMA (FILMS) ---
elif room == "🎬 CINEMA ROOM":
    st.title("🎬 JACKSON CINEMA ROOM")
    st.markdown("### ZIPINDA ZA MAFILIMU (FILM PRODUCTION)")
    st.video("https://youtube.com") # Ichi ndi chitsanzo
    st.info("Jackson, apa ndipo uzikweza mafilimu ako a mabiliyoni!")

# --- CHIPINDA CHA STUDIO (MUSIC) ---
elif room == "🎤 MUSIC STUDIO":
    st.title("🎤 JACK AMAPIANO STUDIO")
    st.markdown("### CHIPINDA CHA NYIMBO (AUDIO ENGINE)")
    st.audio("https://soundhelix.com")
    st.success("Neural Synth Active: Ready to record hits!")

# --- CHIPINDA CHA REVENUE (MONEY) ---
elif room == "💰 REVENUE VAULT":
    st.title("💰 PRIVATE REVENUE VAULT")
    st.metric(label="TOTAL EARNINGS", value="K2,000,000", delta="Ready for Payout")
    st.write("Founder: Jackson Mkandawire - Universal Discovery Master")
    if st.button("WITHDRAW FUNDS"):
        st.balloons()
        st.success("Malipiro a suti yatsopano akutuluka panopa!")
