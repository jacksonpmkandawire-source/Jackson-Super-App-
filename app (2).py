
import streamlit as st

st.set_page_config(page_title="Jackson Super App", page_icon="👑", layout="centered")

st.markdown("<h1 style='text-align: center; color: gold;'>👑 JACKSON SUPER APP 👑</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white;'>SUPREME FOUNDER 300B EDITION</p>", unsafe_allow_html=True)

# THE INTERACTIVE BUTTONS LOGIC
if st.button("🎬 CINEMA"):
    st.balloons()
    st.info("🚀 Jackson Cinema ikukonza mavidiyo a mabiliyoni...")

if st.button("🎤 STUDIO"):
    st.balloons()
    st.info("🎤 Jack Amapiano Studio yadzuka panthawi yomweyo!")

if st.button("💬 SOCIAL"):
    st.balloons()
    st.info("🌍 Jackson Social ikulumikiza dziko lonse lero!")

if st.button("💰 REVENUE"):
    st.balloons()
    st.success("🏦 REVENUE STATUS: K2,000,000 READY FOR PAYOUT! ✅")
    st.write("Jackson, ndalama za suti yatsopano zayamba kuloŵera mu Vault!")

st.markdown("<br><div style='background-color: #1b5e20; padding: 15px; border-radius: 10px; text-align: center; color: white;'>VAULT STATUS: 300,000,000,000 SYNCED ✅</div>", unsafe_allow_html=True)
st.markdown("<br><p style='text-align: center; color: #90caf9;'>Founder: Jackson Mkandawire - Universal Discovery Master</p>", unsafe_allow_html=True)
