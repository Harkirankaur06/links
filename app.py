import streamlit as st
import base64

# 1. Page Configuration
st.set_page_config(
    page_title="Harkiran's Pop Hub! ✨",
    page_icon="🌈",
    layout="centered"
)

# 2. Hyper-Colorful, Bubbly & Light-Mode Locked CSS Engine
st.markdown("""
    <style>
    /* Absolute Force Light Mode Overrides */
    [data-testid="stAppViewContainer"], .stApp, html, body {
        background: linear-gradient(135deg, #FFDEE9 0%, #B5FFFC 100%) !important;
        background-attachment: fixed !important;
        color: #000000 !important;
    }
    
    /* Reset Streamlit defaults */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 3rem !important;
        max-width: 520px !important;
        position: relative;
        z-index: 10;
    }

    /* === SCREEN-WIDE FLOATING BACKGROUND CANVAS === */
    .bubble-bg {
        position: fixed;
        width: 100vw; height: 100vh;
        top: 0; left: 0;
        z-index: 0; /* Keeps bubbles completely in the background */
        pointer-events: none; /* Prevents bubbles from blocking clicks on buttons */
    }
    .bubble {
        position: absolute;
        bottom: -60px;
        background: rgba(255, 255, 255, 0.45);
        border: 2px solid rgba(255, 255, 255, 0.75);
        border-radius: 50%;
        animation: floatUp 7s infinite linear;
        pointer-events: none;
    }
    @keyframes floatUp {
        0% { transform: translateY(0) translateX(0) scale(1); opacity: 0; }
        10% { opacity: 0.8; }
        90% { opacity: 0.8; }
        100% { transform: translateY(-120vh) translateX(70px) scale(1.2); opacity: 0; }
    }

    /* === INTERACTIVE BUBBLY PROFILE CARD === */
    .game-zone {
        background: rgba(255, 255, 255, 0.88);
        border: 4px solid #000000;
        box-shadow: 8px 8px 0px #000000;
        border-radius: 30px;
        padding: 25px;
        text-align: center;
        margin-bottom: 2rem;
        cursor: pointer;
        transition: all 0.2s ease;
    }
    .game-zone:hover {
        transform: translate(-2px, -2px);
        box-shadow: 10px 10px 0px #000000;
    }
    .game-zone:active {
        transform: translate(4px, 4px);
        box-shadow: 2px 2px 0px #000000;
    }
    
    /* Playful Wobbling Image Frame and Content Moving Together */
    .profile-frame {
        width: 120px;
        height: 120px;
        border-radius: 30% 70% 70% 30% / 30% 30% 70% 70%;
        background: linear-gradient(45deg, #FF007F, #7B2CBF, #00F5D4);
        display: inline-flex;
        align-items: center;
        justify-content: center;
        padding: 5px;
        animation: blobMorph 6s ease-in-out infinite alternate;
        box-shadow: 4px 4px 0px #000000;
        overflow: hidden;
    }
    
    .profile-img {
        width: 100%; height: 100%;
        border-radius: 30% 70% 70% 30% / 30% 30% 70% 70%;
        object-fit: cover;
        background: #fff;
        animation: blobMorph 6s ease-in-out infinite alternate;
    }

    @keyframes blobMorph {
        0% { border-radius: 30% 70% 70% 30% / 30% 30% 70% 70%; }
        50% { border-radius: 70% 30% 30% 70% / 70% 70% 30% 30%; }
        100% { border-radius: 50% 50% 50% 50% / 40% 60% 40% 60%; }
    }
    
    .profile-title {
        font-family: 'Arial Black', Gadget, sans-serif;
        font-size: 2.5rem;
        font-weight: 900;
        color: #000000 !important;
        margin-top: 15px;
        text-transform: uppercase;
        letter-spacing: -1px;
        text-shadow: 2px 2px 0px #00F5D4, -2px -2px 0px #FF007F;
    }
    
    .profile-subtitle {
        font-size: 1.05rem;
        font-weight: 700;
        color: #334155 !important;
        margin-top: 5px;
    }

    .score-board {
        background: #FFFF00;
        border: 2px solid #000000;
        padding: 6px 16px;
        border-radius: 20px;
        display: inline-block;
        font-weight: 800;
        color: #000000;
        margin-top: 10px;
        font-size: 0.9rem;
        box-shadow: 3px 3px 0px #000000;
    }

    /* === NEON CARTOON CARD LAYOUT === */
    .section-tag {
        font-family: 'Arial Black', Gadget, sans-serif;
        font-size: 0.9rem;
        font-weight: 900;
        text-transform: uppercase;
        color: #000000;
        margin: 2rem 0 0.8rem 8px;
        display: inline-block;
        background: #FFB703;
        padding: 2px 8px;
        border: 2px solid #000000;
        transform: rotate(-1deg);
        box-shadow: 2px 2px 0px #000000;
    }
    
    .link-card {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: #FFFFFF;
        border: 3px solid #000000;
        border-radius: 20px;
        padding: 16px 20px;
        margin-bottom: 14px;
        text-decoration: none !important;
        box-shadow: 5px 5px 0px #000000;
        transition: all 0.2s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        transform: scale(1.03) translate(-2px, -2px) !important;
    }
    
    .link-card:hover {
        transform: scale(1.03) translate(-2px, -2px);
        box-shadow: 8px 8px 0px #000000;
    }
    
    .link-card.hub-card:hover { border-color: #FF007F; background: #FFF0F5; }
    .link-card.dev-card:hover { border-color: #00F5D4; background: #E6FFFA; }

    .link-left {
        display: flex;
        align-items: center;
        gap: 14px;
    }
    
    .logo-box {
        width: 44px;
        height: 44px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 12px;
        background: #F1F5F9;
        border: 2px solid #000000;
        color: #000000;
    }
    
    .link-title {
        color: #000000 !important;
        font-weight: 800;
        font-size: 1.1rem;
    }
    .link-subtitle {
        color: #475569 !important;
        font-size: 0.8rem;
        font-weight: 600;
        margin-top: 1px;
    }
    
    .copy-pill {
        background: #E2E8F0;
        border: 2px solid #000000;
        color: #000000;
        padding: 6px 14px;
        border-radius: 12px;
        font-size: 0.75rem;
        font-weight: 800;
        cursor: pointer;
        box-shadow: 2px 2px 0px #000000;
    }
    </style>

    <!-- JavaScript Interactive Score and Copy Controls -->
    <script>
    let popCount = 0;
    function popBubbleEffect(event) {
        popCount++;
        document.getElementById('score-value').innerText = popCount;
        
        // Quick visual pop background flash
        const zone = document.getElementById('game-zone');
        const colors = ['#FF007F', '#00F5D4', '#FFFF00', '#A855F7', '#FF9F1C'];
        zone.style.backgroundColor = colors[popCount % colors.length] + '15';
        setTimeout(() => zone.style.backgroundColor = 'rgba(255, 255, 255, 0.88)', 150);
    }

    function copyLink(text, e) {
        if(e) { e.preventDefault(); e.stopPropagation(); }
        navigator.clipboard.writeText(text).then(() => {
            const btn = window.event.target;
            btn.innerText = 'POPPED! 🎉';
            btn.style.background = '#00F5D4';
            setTimeout(() => {
                btn.innerText = 'Copy';
                btn.style.background = '#E2E8F0';
            }, 1200);
        });
        return false;
    }
    </script>

    <!-- Continuous Screen-Wide Background Bubble Framework -->
    <div class="bubble-bg">
        <div class="bubble" style="left: 8%; width: 45px; height: 45px; animation-delay: 0s; animation-duration: 6s;"></div>
        <div class="bubble" style="left: 25%; width: 25px; height: 25px; animation-delay: 1.5s; animation-duration: 8s;"></div>
        <div class="bubble" style="left: 45%; width: 55px; height: 55px; animation-delay: 0.5s; animation-duration: 5s;"></div>
        <div class="bubble" style="left: 68%; width: 35px; height: 35px; animation-delay: 3s; animation-duration: 7s;"></div>
        <div class="bubble" style="left: 88%; width: 40px; height: 40px; animation-delay: 1s; animation-duration: 6.5s;"></div>
    </div>
""", unsafe_allow_html=True)

# 3. Base64 Image Parser for Local Directory File
try:
    with open("AVATAR.jpg", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    MY_PHOTO_URL = f"data:image/jpeg;base64,{encoded_string}"
except FileNotFoundError:
    MY_PHOTO_URL = "https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=200&q=80"

# Main Interactive Header
st.markdown(f"""
    <div class="game-zone" id="game-zone" onclick="popBubbleEffect(event)">
        <div class="profile-frame">
            <img class="profile-img" src="{MY_PHOTO_URL}" alt="Harkiran Kaur"/>
        </div>
        <div class="profile-title">HARKIRAN KAUR</div>
        <div class="profile-subtitle">🍭 Bubbly Software Engineer & Developer</div>
        <div><div class="score-board">🎈 Bubbles Popped: <span id="score-value">0</span></div></div>
    </div>
""", unsafe_allow_html=True)

# 4. Card Builder Function
def render_row(svg_path, title, subtitle, target_url, card_type="hub-card", viewbox="0 0 24 24"):
    card_html = f"""
    <a class="link-card {card_type}" href="{target_url}" target="_blank">
        <div class="link-left">
            <div class="logo-box">
                <svg width="22" height="22" viewBox="{viewbox}" fill="currentColor">
                    <path d="{svg_path}"/>
                </svg>
            </div>
            <div class="link-text-container">
                <span class="link-title">{title}</span>
                <span class="link-subtitle">{subtitle}</span>
            </div>
        </div>
        <button class="copy-pill" onclick="copyLink('{target_url}', event); return false;">Copy</button>
    </a>
    """
    st.markdown(card_html, unsafe_allow_html=True)

# SVG Icons
GLOBE_PATH = "M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"
GITHUB_PATH = "M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"
LINKEDIN_PATH = "M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"
YOUTUBE_PATH = "M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"
CODE_PATH = "M9.4 16.6L4.8 12l4.6-4.6L8 6l-6 6 6 6 1.4-1.4zm5.2 0l4.6-4.6-4.6-4.6L16 6l6 6-6 6-1.4-1.4z"

# Sections
st.markdown('<div class="section-tag">⭐ Profiles & Hubs ⭐</div>', unsafe_allow_html=True)
render_row(GLOBE_PATH, "Main Portfolio Website", "harkirankaur06.github.io/Portfolio", "https://harkirankaur06.github.io/Portfolio", "hub-card")
render_row(GITHUB_PATH, "GitHub Workspace", "github.com/harkirankaur06", "https://github.com/harkirankaur06", "hub-card")
render_row(LINKEDIN_PATH, "LinkedIn Connection", "linkedin.com/in/harkiran-kaur-", "https://linkedin.com/in/harkiran-kaur-", "hub-card")
render_row(YOUTUBE_PATH, "Video Project Demos", "youtube.com/@harkirankaur-h5g", "https://youtube.com/@harkirankaur-h5g", "hub-card")

st.markdown('<div class="section-tag">🚀 Live Deployments 🚀</div>', unsafe_allow_html=True)
render_row(CODE_PATH, "LEGEND Financial Digital Twin", "psb-steel.vercel.app", "https://psb-steel.vercel.app/", "dev-card")
render_row(CODE_PATH, "Low-Q App", "low-q.vercel.app", "https://low-q.vercel.app", "dev-card")
render_row(CODE_PATH, "Unreal App", "unreal.streamlit.app", "https://unreal.streamlit.app", "dev-card")

st.markdown("<p style='text-align: center; font-size: 13px; font-weight: 800; color: #000000; margin-top: 3rem;'>Made with 💖, Python & Magic!</p>", unsafe_allow_html=True)