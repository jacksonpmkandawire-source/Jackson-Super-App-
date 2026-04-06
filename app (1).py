
import streamlit as st

st.set_page_config(page_title="Jackson Super App", page_icon="👑", layout="centered")

st.markdown("<h1 style='text-align: center; color: gold;'>👑 JACKSON SUPER APP 👑</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: white;'>SUPREME FOUNDER 300B EDITION</p>", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    st.button("🎬 CINEMA")
    st.button("🎤 STUDIO")
with col2:
    st.button("💬 SOCIAL")
    st.button("💰 REVENUE")

st.success("VAULT STATUS: 300,000,000,000 SYNCED ✅")
st.info("Founder: Jackson Mkandawire - Universal Discovery Master")
