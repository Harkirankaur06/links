import streamlit as st

# 1. Page Settings
st.set_page_config(
    page_title="Harkiran Kaur | Interactive Hub",
    page_icon="🎮",
    layout="centered"
)

# 2. Advanced Game Engine UI, Animations & Custom SVGs
st.markdown("""
    <style>
    /* Reset Streamlit defaults */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Premium Interactive Space Background */
    [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at 50% 50%, #0d1527 0%, #040712 100%) !important;
        overflow: hidden;
    }
    
    .block-container {
        padding-top: 3rem !important;
        padding-bottom: 3rem !important;
        max-width: 550px !important;
        position: relative;
        z-index: 5;
    }

    /* === GAME CANVAS AREA === */
    .game-zone {
        background: rgba(30, 41, 59, 0.4);
        border: 2px dashed rgba(99, 102, 241, 0.4);
        border-radius: 24px;
        padding: 20px;
        text-align: center;
        margin-bottom: 2rem;
        position: relative;
        cursor: pointer;
        overflow: hidden;
        backdrop-filter: blur(8px);
    }
    .game-zone:active {
        border-color: #A855F7;
    }
    
    /* Floating target nodes */
    .game-particle {
        position: absolute;
        width: 12px;
        height: 12px;
        background: #6366F1;
        border-radius: 50%;
        box-shadow: 0 0 12px #6366F1;
        animation: floatParticle 6s infinite ease-in-out alternate;
    }
    
    @keyframes floatParticle {
        0% { transform: translate(0px, 0px) scale(1); background: #6366F1; }
        50% { transform: translate(120px, -30px) scale(1.3); background: #A855F7; }
        100% { transform: translate(40px, 50px) scale(0.9); background: #38BDF8; }
    }

    /* High-End Circular Profile Frame */
    .profile-frame {
        width: 110px;
        height: 110px;
        border-radius: 50%;
        background: linear-gradient(135deg, #6366F1, #A855F7, #38BDF8);
        background-size: 300% 300%;
        display: inline-flex;
        align-items: center;
        justify-content: center;
        padding: 4px;
        animation: gradientShift 6s ease infinite;
        box-shadow: 0 0 30px rgba(99, 102, 241, 0.4);
    }
    
    .profile-img {
        width: 100%;
        height: 100%;
        border-radius: 50%;
        object-fit: cover;
        background: #0f172a;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2.5rem;
    }

    @keyframes gradientShift {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    .profile-title {
        font-family: system-ui, sans-serif;
        font-size: 2.6rem;
        font-weight: 900;
        color: #FFFFFF !important;
        margin-top: 15px;
        margin-bottom: 4px;
        letter-spacing: -0.5px;
    }
    
    .profile-subtitle {
        font-size: 0.95rem;
        color: #94A3B8 !important;
    }

    .score-board {
        font-size: 0.8rem;
        font-weight: 700;
        color: #38BDF8;
        letter-spacing: 1px;
        margin-top: 10px;
        text-transform: uppercase;
    }

    /* Card System with Brand Colors & Dynamic Hover Lift */
    .link-card {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: rgba(15, 23, 42, 0.6);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 20px;
        padding: 16px 22px;
        margin-bottom: 12px;
        text-decoration: none !important;
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
    }
    .link-card:hover {
        transform: translateY(-4px) scale(1.01);
        background: rgba(15, 23, 42, 0.8);
        border-color: rgba(99, 102, 241, 0.4);
        box-shadow: 0 15px 30px -10px rgba(99, 102, 241, 0.3);
    }

    .link-left {
        display: flex;
        align-items: center;
        gap: 16px;
    }
    
    .logo-box {
        width: 40px;
        height: 40px;
        display: flex;
        align-items: center;
        justify-content: center;
        border-radius: 12px;
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
    }
    
    .link-title {
        color: #F8FAFC !important;
        font-weight: 600;
        font-size: 1.05rem;
    }
    .link-subtitle {
        color: #64748B !important;
        font-size: 0.8rem;
        margin-top: 1px;
    }
    
    .copy-pill {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.08);
        color: #94A3B8;
        padding: 6px 12px;
        border-radius: 10px;
        font-size: 0.75rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.2s;
    }
    .copy-pill:hover {
        background: #FFFFFF;
        color: #0F172A;
    }

    .section-tag {
        font-size: 0.75rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 2px;
        color: #6366F1;
        margin: 2rem 0 0.8rem 4px;
    }
    </style>

    <!-- Game Logic & Clipboard Operations Script -->
    <script>
    let clicks = 0;
    function triggerClickEffect() {
        clicks++;
        document.getElementById('score-value').innerText = clicks;
        
        // Dynamic Node Spawning logic
        const zone = document.getElementById('game-zone');
        const spark = document.createElement('div');
        spark.className = 'game-particle';
        spark.style.left = Math.random() * 80 + 10 + '%';
        spark.style.top = Math.random() * 60 + 20 + '%';
        zone.appendChild(spark);
        
        if(clicks % 5 === 0) {
            zone.style.boxShadow = '0 0 25px rgba(168, 85, 247, 0.6)';
            setTimeout(() => zone.style.boxShadow = 'none', 300);
        }
    }

    function copyLink(text, e) {
        if(e) { e.preventDefault(); e.stopPropagation(); }
        navigator.clipboard.writeText(text).then(() => {
            const btn = window.event.target;
            btn.innerText = 'Copied! ✓';
            btn.style.background = '#6366F1';
            btn.style.color = '#FFFFFF';
            setTimeout(() => {
                btn.innerText = 'Copy';
                btn.style.background = 'rgba(255, 255, 255, 0.04)';
                btn.style.color = '#94A3B8';
            }, 1200);
        });
        return false;
    }
    </script>
""", unsafe_allow_html=True)

# 3. Interactive Game & Profile Header Section
# Note: To use a real photo instead of the emoji, just replace the URL inside <img src="..." /> below!
st.markdown("""
    <div class="game-zone" id="game-zone" onclick="triggerClickEffect()">
        <!-- Moving nodes initialized in background -->
        <div class="game-particle" style="animation-delay: 0s;"></div>
        <div class="game-particle" style="animation-delay: -2s; left: 70%;"></div>
        
        <div class="profile-frame">
            <div class="profile-img">
                <img src="AVATAR.jpg" style="width:100%; height:100%; border-radius:50%; object-fit:cover;" alt="Harkiran"/>
            </div>
        </div>
        
        <div class="profile-title">HARKIRAN KAUR</div>
        <div class="profile-subtitle">📍 Delhi, India &nbsp;•&nbsp; Software Engineer</div>
        <div class="score-board">👾 System Overload Score: <span id="score-value">0</span></div>
    </div>
""", unsafe_allow_html=True)

# 4. Inline SVG Icon Renderer Function
def render_row(svg_path, title, subtitle, target_url, viewbox="0 0 24 24"):
    card_html = f"""
    <a class="link-card" href="{target_url}" target="_blank">
        <div class="link-left">
            <div class="logo-box">
                <svg width="20" height="20" viewBox="{viewbox}" fill="currentColor" style="color: #a5b4fc;">
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

# SVG Raw Path Assets
GITHUB_PATH = "M12 .297c-6.63 0-12 5.373-12 12 0 5.303 3.438 9.8 8.205 11.385.6.113.82-.258.82-.577 0-.285-.01-1.04-.015-2.04-3.338.724-4.042-1.61-4.042-1.61C4.422 18.07 3.633 17.7 3.633 17.7c-1.087-.744.084-.729.084-.729 1.205.084 1.838 1.236 1.838 1.236 1.07 1.835 2.809 1.305 3.495.998.108-.776.417-1.305.76-1.605-2.665-.3-5.466-1.332-5.466-5.93 0-1.31.465-2.38 1.235-3.22-.135-.303-.54-1.523.105-3.176 0 0 1.005-.322 3.3 1.23.96-.267 1.98-.399 3-.405 1.02.006 2.04.138 3 .405 2.28-1.552 3.285-1.23 3.285-1.23.645 1.653.24 2.873.12 3.176.765.84 1.23 1.91 1.23 3.22 0 4.61-2.805 5.625-5.475 5.92.42.36.81 1.096.81 2.22 0 1.606-.015 2.896-.015 3.286 0 .315.21.69.825.57C20.565 22.092 24 17.592 24 12.297c0-6.627-5.373-12-12-12"
LINKEDIN_PATH = "M19 0h-14c-2.761 0-5 2.239-5 5v14c0 2.761 2.239 5 5 5h14c2.762 0 5-2.239 5-5v-14c0-2.761-2.238-5-5-5zm-11 19h-3v-11h3v11zm-1.5-12.268c-.966 0-1.75-.79-1.75-1.764s.784-1.764 1.75-1.764 1.75.79 1.75 1.764-.783 1.764-1.75 1.764zm13.5 12.268h-3v-5.604c0-3.368-4-3.113-4 0v5.604h-3v-11h3v1.765c1.396-2.586 7-2.777 7 2.476v6.759z"
YOUTUBE_PATH = "M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z"
GLOBE_PATH = "M12 2C6.48 2 2 6.48 2 12s4.48 10 10 10 10-4.48 10-10S17.52 2 12 2zm-1 17.93c-3.95-.49-7-3.85-7-7.93 0-.62.08-1.21.21-1.79L9 15v1c0 1.1.9 2 2 2v1.93zm6.9-2.54c-.26-.81-1-1.39-1.9-1.39h-1v-3c0-.55-.45-1-1-1H8v-2h2c.55 0 1-.45 1-1V7h2c1.1 0 2-.9 2-2v-.41c2.93 1.19 5 4.06 5 7.41 0 2.08-.8 3.97-2.1 5.39z"
CODE_PATH = "M9.4 16.6L4.8 12l4.6-4.6L8 6l-6 6 6 6 1.4-1.4zm5.2 0l4.6-4.6-4.6-4.6L16 6l6 6-6 6-1.4-1.4z"

# 5. Core Content Sections
st.markdown('<div class="section-tag">Profiles & Hubs</div>', unsafe_allow_html=True)
render_row(GLOBE_PATH, "Main Portfolio Website", "harkirankaur06.github.io/Portfolio", "https://harkirankaur06.github.io/Portfolio")
render_row(GITHUB_PATH, "GitHub Workspace", "github.com/harkirankaur06", "https://github.com/harkirankaur06")
render_row(LINKEDIN_PATH, "LinkedIn Connection", "linkedin.com/in/harkiran-kaur-", "https://linkedin.com/in/harkiran-kaur-")
render_row(YOUTUBE_PATH, "Video Project Demos", "youtube.com/@harkirankaur-h5g", "https://youtube.com/@harkirankaur-h5g")

st.markdown('<div class="section-tag">Live Deployments</div>', unsafe_allow_html=True)
render_row(CODE_PATH, "LEGEND Financial Digital Twin", "psb-steel.vercel.app", "https://psb-steel.vercel.app/")
render_row(CODE_PATH, "Low-Q App", "low-q.vercel.app", "https://low-q.vercel.app")
render_row(CODE_PATH, "Unreal App", "unreal.streamlit.app", "https://unreal.streamlit.app")