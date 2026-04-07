import streamlit as st

st.set_page_config(page_title="Jackson Super App", page_icon="👑", layout="wide")

st.sidebar.markdown("<h2 style='color: gold;'>👑 JACKSON MENU</h2>", unsafe_allow_html=True)
room = st.sidebar.radio("SANKHANI CHIPINDA:", ["🏠 HOME SCREEN", "🎬 CINEMA & BETTING", "🎤 MUSIC STUDIO", "💰 REVENUE VAULT"])

if room == "🏠 HOME SCREEN":
    st.markdown("<h1 style='text-align: center; color: gold;'>👑 JACKSON SUPER APP 👑</h1>", unsafe_allow_html=True)
    st.success("VAULT STATUS: 300,000,000,000 SYNCED ✅")

elif room == "🎬 CINEMA & BETTING":
    st.title("🎬 CINEMA & ⚽ BET PREDICTIONS")
    st.markdown("### Today's Top Predictions (April 7, 2026)")
    st.info("🚀 Prediction 1: Real Madrid vs Man City - Home Win (2.10)")
    st.info("🚀 Prediction 2: Arsenal vs Bayern - Over 2.5 Goals (1.85)")
    st.success("Cinema Hub: Watch Live Football & Dance Challenges Active ✅")

elif room == "🎤 MUSIC STUDIO":
    st.title("🎤 JACK AMAPIANO STUDIO")
    st.audio("https://soundhelix.com")

elif room == "💰 REVENUE VAULT":
    st.title("💰 PRIVATE REVENUE VAULT")
    st.metric(label="CURRENT REVENUE", value="K3,650,000", delta="Ready for Ufa & Clothing")
    if st.button("WITHDRAW FUNDS FOR FOOD"):
        st.balloons()
        st.success("MALIPIRO ATSIMIKIZIDWA! K3,650,000 ikuloŵera kwa Jackson Mkandawire! ✅")
    
