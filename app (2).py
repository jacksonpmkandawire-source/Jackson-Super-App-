import streamlit as st
import time
import random

# ==========================================
# 1. SYSTEM CONFIGURATION (INFINITY THEME)
# ==========================================
st.set_page_config(
    page_title="Jackson Super App",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS: Mawonekedwe a Chilengedwe (Neon Purple & Gold)
st.markdown("""
    <style>
    .stApp {background-color: #050505; color: #e0e0e0;}
    h1 {color: #d4af37 !important; text-shadow: 0px 0px 20px #d4af37; font-family: 'Arial Black';}
    h2, h3 {color: #00e676 !important;}
    .stButton>button {
        background: linear-gradient(90deg, #d4af37, #6200ea);
        color: white; font-weight: 900; border-radius: 25px; height: 65px; width: 100%;
        font-size: 22px; border: 3px solid gold; box-shadow: 0px 0px 15px #6200ea;
    }
    .stRadio>label {font-size: 18px; color: #b388ff;}
    </style>
    """, unsafe_allow_html=True)

# ==========================================
# 2. THE INFINITE MENU (ZIPINDA 30)
# ==========================================
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/crown.png", width=110)
    st.markdown("# 👑 JACKSON INFINITY")
    
    founder = "Jackson Mkandawire"
    st.info(f"👑 LEVEL: GOD MODE\n👤 OWNER: {founder}")
    
    # Mndandanda Wathunthu (All 30 Rooms)
    menu = st.radio("SANKHANI MPHAMVU YANU:", [
        "🏠 WORLD COMMAND CENTER",
        "🌀 HUMAN TELEPORTATION (NEW)",
        "💤 DREAM VIDEO RECORDER (NEW)",
        "🦖 DINOSAUR CLONER (NEW)",
        "🧠 INSTANT SKILL DOWNLOAD (NEW)",
        "👶 AGE REVERSER (NEW)",
        "🍔 3D FOOD PRINTER",
        "👻 GHOST SPIRIT HUNTER",
        "🌩️ WEATHER CONTROLLER",
        "🔮 FUTURE PROPHECY",
        "🚗 FLYING CAR TAXI",
        "🧠 TELEPATHY CHAT",
        "🕰️ AI TIME MACHINE",
        "🛸 UFO & ALIEN RADAR",
        "🗣️ UNIVERSAL TRANSLATOR",
        "🧬 DNA ANCESTRY SCAN",
        "📡 FREE SATELLITE NET",
        "⛏️ BITCOIN MINING FARM",
        "🏥 X-RAY BODY SCANNER",
        "🎬 AI FILM MAKER (5HRS)",
        "💃 DANCE ANIMATOR AI",
        "🎤 MUSIC STUDIO PRO",
        "📰 NEWS & MIRACLES",
        "🎮 GAME DEV ENGINE",
        "💳 VIRTUAL VISA CARD",
        "📈 FOREX SIGNALS ROBOT",
        "🏠 METAVERSE REAL ESTATE",
        "🚔 ANTI-HACK SHIELD",
        "🏥 LIFE ADVISOR",
        "💰 REVENUE VAULT"
    ])
    st.markdown("---")

# ==========================================
# 3. ZIPINDA ZATSOPANO (GOD MODE LOGIC)
# ==========================================

# --- 🏠 HOME ---
if menu == "🏠 WORLD COMMAND CENTER":
    st.title(f"🌌 {founder.upper()} INFINITY CONTROL")
    col1, col2, col3 = st.columns(3)
    col1.metric("Population Controlled", "8.1 Billion", "100%")
    col2.metric("Galaxies Unlocked", "Milky Way", "Active")
    col3.metric("Jackson's Net Worth", "INFINITE", "Trillions")
    st.image("https://media.istockphoto.com/id/1365534327/photo/artificial-intelligence-in-huge-data-center.jpg?s=612x612&w=0&k=20&c=wQjTfC2tU3Tz_sC_sC_sC", use_column_width=True)

# --- 🌀 TELEPORTATION (NEW) ---
elif menu == "🌀 HUMAN TELEPORTATION (NEW)":
    st.title("🌀 INSTANT TRAVEL PORTAL")
    st.write("Yendani kulikonse padziko lapansi mwa mphindi imodzi.")
    dest = st.selectbox("MUKUFUNA KUPITA KUTI?", ["New York (USA)", "Tokyo (Japan)", "Mars (Planet)", "Paris (France)"])
    if st.button("TELEPORT NOW"):
        with st.spinner("Dematerializing Body Atoms..."):
            time.sleep(4)
        st.balloons()
        st.success(f"✅ WOOSH! Mwafika ku {dest} bwinobwino! Takulandirani.")
        st.image("https://media.istockphoto.com/id/1322205410/photo/futuristic-sci-fi-corridor-with-blue-neon-lights.jpg?s=612x612&w=0&k=20&c=eA_k1ZzZ1ZzZ1ZzZ", caption=f"Mwafika ku {dest}")

# --- 💤 DREAM RECORDER (NEW) ---
elif menu == "💤 DREAM VIDEO RECORDER (NEW)":
    st.title("💤 4K DREAM RECORDER")
    st.write("Kodi munalota chiyani dzulo? Onerani kanema wake pano.")
    if st.button("PLAY LAST NIGHT'S DREAM"):
        with st.spinner("Connecting to Brain Cloud..."):
            time.sleep(3)
        st.success("✅ Maloto anu apezeka! Mukusewera kanema...")
        st.video("https://www.youtube.com/watch?v=dQw4w9WgXcQ") # Placeholder Video

# --- 🦖 DINOSAUR CLONER (NEW) ---
elif menu == "🦖 DINOSAUR CLONER (NEW)":
    st.title("🦖 JURASSIC PARK LAB")
    st.write("Pangani dzira la Dinosaur kuti muwete pakhomo.")
    dino = st.radio("SANKHANI NYAMA:", ["T-Rex (Yaukali)", "Velociraptor (Yothamanga)", "Mammoth (Njovu Yake)"])
    if st.button("CLONE DNA"):
        st.warning(f"Warning: {dino} is dangerous!")
        time.sleep(2)
        st.success(f"✅ Dzira la {dino} laswedwa! Musamale nayo.")

# --- 🧠 SKILL DOWNLOAD (NEW) ---
elif menu == "🧠 INSTANT SKILL DOWNLOAD (NEW)":
    st.title("🧠 BRAIN UPLOAD CENTER")
    st.write("Sifunika kupita kusukulu. Ikani nzeru m'mutu mwanu panopa.")
    skill = st.selectbox("MUKUFUNA KUDZIWA CHIYANI?", ["Kung Fu Master", "Brain Surgery (Doctor)", "Pilot (Kuyendetsa Ndege)", "Speak Chinese"])
    if st.button("DOWNLOAD SKILL"):
        with st.spinner("Writing Neural Code to Brain..."):
            time.sleep(3)
        st.success(f"✅ DOWNLOAD COMPLETE! Tsopano inu ndinu katswiri wa {skill}.")

# --- 👶 AGE REVERSER (NEW) ---
elif menu == "👶 AGE REVERSER (NEW)":
    st.title("👶 YOUTH RESTORATION")
    st.write("Bwererani kukhala mwana wazaka 18.")
    age = st.slider("Sankhani Zaka Zanu Zatsopano:", 10, 25, 18)
    if st.button("ACTIVATE LASER"):
        st.success(f"✅ Matsenga Agwira! Tsopano mukuoneka ngati muli ndi zaka {age}.")

# --- 🍔 3D FOOD PRINTER ---
elif menu == "🍔 3D FOOD PRINTER":
    st.title("🍔 DIGITAL FOOD PRINTER")
    food = st.selectbox("MUKUFUNA KUDYA CHIYANI?", ["Chambo & Nsima", "KFC Bucket", "Pizza"])
    if st.button("PRINT FOOD"):
        st.success(f"✅ {food} yakonzeka! Tengani pa screen.")

# --- 👻 GHOST HUNTER ---
elif menu == "👻 GHOST SPIRIT HUNTER":
    st.title("👻 GHOST COMMUNICATOR")
    if st.button("SCAN ROOM"):
        st.error("⚠️ WARNING: Mzimu wa Mfumu yakale waoneka pakona!")

# --- 🌩️ WEATHER CONTROL ---
elif menu == "🌩️ WEATHER CONTROLLER":
    st.title("🌩️ WEATHER GOD MODE")
    action = st.radio("NYENGO:", ["IMILITSANI MVULA", "GWETSANI MVULA"])
    if st.button("EXECUTE"):
        st.success(f"✅ Lamulo Lavomerezedwa! Nyengo yasintha.")

# --- 🔮 FUTURE PROPHECY ---
elif menu == "🔮 FUTURE PROPHECY":
    st.title("🔮 SEE THE FUTURE")
    if st.button("REVEAL TOMORROW"):
        st.info("🔮 **MAWA:** Mudzalandira foni kuchokera kwa Elon Musk.")

# --- 🚗 FLYING CAR ---
elif menu == "🚗 FLYING CAR TAXI":
    st.title("🚗 FLYING TAXI SUMMONER")
    if st.button("CALL DRONE"):
        st.success("✅ Drone Taxi yanyamuka! Ifika mu 2 mins.")

# --- 🧠 TELEPATHY ---
elif menu == "🧠 TELEPATHY CHAT":
    st.title("🧠 BRAIN CHAT")
    if st.button("READ MIND"):
        st.success("✅ Detected Idea: 'Jackson App is King.'")

# --- 🎬 FILMS ---
elif menu == "🎬 AI FILM MAKER (5HRS)":
    st.title("🎬 HOLLYWOOD PRO")
    st.write("Create 5hr Movies. Price: MK 15,000.")
    if st.button("GENERATE MOVIE"):
        st.success("✅ Filimu ikupangidwa!")

# --- 💃 DANCE ---
elif menu == "💃 DANCE ANIMATOR AI":
    st.title("💃 TIKTOK DANCE MAKER")
    if st.button("MAKE IT DANCE"):
        st.success("✅ Video Yovina yakonzeka!")

# --- 🎤 MUSIC ---
elif menu == "🎤 MUSIC STUDIO PRO":
    st.title("🎤 HIT SONG MAKER")
    if st.button("CREATE BEAT"):
        st.audio("https://www.soundhelix.com/examples/mp3/SoundHelix-Song-1.mp3")
        st.success("✅ Beat Created!")

# --- 💰 REVENUE ---
elif menu == "💰 REVENUE VAULT":
    st.title("💰 THE TRILLION BANK")
    st.metric("BALANCE", "MK 900,000,000", "Verified")
    if st.button("WITHDRAW ALL"):
        st.balloons()
        st.success("✅ Ndalama zonse zatumizidwa!")


