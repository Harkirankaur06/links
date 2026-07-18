import streamlit as st
import time

# 1. Initialize Page Profile & Global Config
st.set_page_config(
    page_title="Harkiran Kaur | Identity Hub",
    page_icon="✨",
    layout="centered"
)

# 2. Complete UI Engineering Overhaul (Neon Glassmorphism + Background Particles)
st.markdown("""
    <style>
    /* Absolute reset of Streamlit styling defaults to allow custom composition */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp { background: #030712 !important; }
    
    /* Layout Framework Constraints */
    .block-container {
        padding-top: 5rem !important;
        padding-bottom: 5rem !important;
        max-width: 550px !important;
        position: relative;
        z-index: 10;
    }
    
    /* === DYNAMIC CSS PARTICLE BACKGROUND (Always Visible) === */
    .bg-animation {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background: radial-gradient(circle at 50% 50%, #111827, #030712);
        z-index: 1;
        overflow: hidden;
    }
    .orb {
        position: absolute;
        width: 350px; height: 350px;
        background: radial-gradient(circle, rgba(99, 102, 241, 0.2) 0%, rgba(0,0,0,0) 70%);
        border-radius: 50%;
        animation: floatOrb 25s infinite alternate ease-in-out;
    }
    .orb-2 {
        position: absolute;
        bottom: 5%; right: -5%;
        width: 400px; height: 400px;
        background: radial-gradient(circle, rgba(168, 85, 247, 0.15) 0%, rgba(0,0,0,0) 70%);
        border-radius: 50%;
        animation: floatOrb 30s infinite alternate-reverse ease-in-out;
    }
    @keyframes floatOrb {
        0% { transform: translate(0px, 0px) scale(1); }
        100% { transform: translate(80px, 60px) scale(1.1); }
    }

    /* === PREMIUM PROFILE HEAD (Moving Images) === */
    .avatar-wrapper {
        display: flex;
        justify-content: center;
        margin-bottom: 20px;
        position: relative;
    }
    /* Animated Gradient Border that spins */
    .avatar-placeholder {
        width: 100px;
        height: 100px;
        border-radius: 50%;
        background: linear-gradient(135deg, #6366F1, #A855F7);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2.2rem;
        box-shadow: 0 0 35px rgba(99, 102, 241, 0.5);
        border: 2px solid rgba(255, 255, 255, 0.1);
        position: relative;
        overflow: hidden;
        animation: spin-gradient 4s linear infinite;
    }
    @keyframes spin-gradient {
        0% { border-color: rgba(99, 102, 241, 0.8); }
        50% { border-color: rgba(168, 85, 247, 0.8); }
        100% { border-color: rgba(99, 102, 241, 0.8); }
    }
    
    .profile-title {
        font-family: system-ui, -apple-system, sans-serif;
        font-size: 2.8rem;
        font-weight: 900;
        letter-spacing: -1.5px;
        text-align: center;
        background: linear-gradient(to right, #FFFFFF, #94A3B8);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
    }
    
    .profile-subtitle {
        font-size: 1rem;
        color: #94A3B8;
        text-align: center;
        margin-bottom: 28px;
        letter-spacing: 0.5px;
        font-weight: 500;
    }

    /* === DIRECT CONNECT GRID === */
    .action-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 14px;
        margin-bottom: 2.5rem;
    }
    .action-button {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 10px;
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 16px;
        padding: 14px;
        color: #F8FAFC !important;
        font-weight: 600;
        font-size: 0.9rem;
        text-decoration: none !important;
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    }
    .action-button:hover {
        background: rgba(255, 255, 255, 0.08);
        border-color: rgba(255, 255, 255, 0.2);
        transform: translateY(-2px);
    }
    
    /* Section Headings */
    .section-label {
        font-size: 0.75rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 2.5px;
        color: #818CF8;
        margin-top: 2.5rem;
        margin-bottom: 1rem;
        padding-left: 4px;
    }
    
    /* === INTERACTIVE GLASSMORPHIC LINK CARDS === */
    .link-card {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: rgba(15, 23, 42, 0.5);
        backdrop-filter: blur(15px);
        -webkit-backdrop-filter: blur(15px);
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 20px;
        padding: 20px 24px;
        margin-bottom: 14px;
        text-decoration: none !important;
        transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1); /* Advanced timing for physics */
    }
    
    /* Dynamic Hover: Neon Border Glow + Rotation */
    .link-card:hover {
        transform: translateY(-4px) scale(1.015) rotate(0.2deg);
        background: rgba(15, 23, 42, 0.7);
        border-color: rgba(99, 102, 241, 0.4);
        box-shadow: 0 20px 40px -15px rgba(99, 102, 241, 0.25), 0 0 15px rgba(99, 102, 241, 0.1);
    }
    
    .link-content {
        display: flex;
        align-items: center;
        gap: 18px;
    }
    
    /* Animated Icon Wrapper */
    .icon-wrapper {
        width: 46px;
        height: 46px;
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.1), rgba(168, 85, 247, 0.1));
        border: 1px solid rgba(99, 102, 241, 0.3);
        border-radius: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .link-card:hover .icon-wrapper {
        background: linear-gradient(135deg, #6366F1, #A855F7);
        border-color: transparent;
        transform: rotate(5deg) scale(1.1);
    }

    /* Target direct SVGs inside the wrapper on hover */
    .link-card:hover i {
        color: #FFFFFF !important;
    }
    
    .link-text-container {
        display: flex;
        flex-direction: column;
    }
    
    .link-title {
        color: #F8FAFC !important;
        font-weight: 600;
        font-size: 1.1rem;
        letter-spacing: -0.2px;
    }
    
    .link-subtitle {
        color: #64748B !important;
        font-size: 0.8rem;
        margin-top: 3px;
        transition: color 0.2s;
    }
    .link-card:hover .link-subtitle {
        color: #CBD5E1 !important;
    }
    
    /* Copy Action Pill Button */
    .copy-btn {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.07);
        color: #94A3B8;
        padding: 8px 14px;
        border-radius: 12px;
        font-size: 0.75rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.2s cubic-bezier(0.4, 0, 0.2, 1);
    }
    
    .copy-btn:hover {
        background: #FFFFFF;
        color: #0F172A;
        border-color: #FFFFFF;
        transform: scale(1.08);
    }
    </style>
    
    <!-- Custom Moving Asset Background Nodes (CSS Driven Animations) -->
    <div class="bg-animation">
        <div class="orb" style="top: 15%; left: -8%;"></div>
        <div class="orb-2" style="bottom: 8%; right: -6%;"></div>
    </div>
    
    <!-- Inline Copy Handling Interactivity Script (Must keep for copy button to work) -->
    <script>
    function copyToClipboard(text, e) {
        if(e) { e.preventDefault(); e.stopPropagation(); }
        navigator.clipboard.writeText(text).then(() => {
            const btn = window.event.target;
            const originalText = btn.innerText;
            btn.innerText = 'Copied! ✓';
            btn.style.background = '#6366F1';
            btn.style.borderColor = '#6366F1';
            btn.style.color = '#FFFFFF';
            setTimeout(() => {
                btn.innerText = originalText;
                btn.style.background = 'rgba(255, 255, 255, 0.04)';
                btn.style.borderColor = 'rgba(255, 255, 255, 0.07)';
                btn.style.color = '#94A3B8';
            }, 1200);
        });
        return false;
    }
    </script>
""", unsafe_allow_html=True)

# 3. Import Vector Icons Library Engine (Required Internet for full visual)
st.markdown('<script src="https://unpkg.com/lucide@latest"></script>', unsafe_allow_html=True)

# 4. Profile Header Branding & Animations
st.markdown("""
    <div class="avatar-wrapper">
        <div class="avatar-placeholder">👩‍💻</div>
    </div>
""", unsafe_allow_html=True)
st.markdown('<div class="profile-title">HARKIRAN KAUR</div>', unsafe_allow_html=True)
st.markdown('<div class="profile-subtitle">📍 Delhi, India &nbsp;•&nbsp; Software Engineer</div>', unsafe_allow_html=True)

# Direct Connect Action Grid
st.markdown("""
    <div class="action-grid">
        <a class="action-button" href="tel:8585976065">📞 Call Direct</a>
        <a class="action-button" href="mailto:harkirankaur.0606@gmail.com">✉️ Drop Email</a>
    </div>
""", unsafe_allow_html=True)

# 5. Core Interface Card Component Definition
def render_link_card(icon_name, title, subtitle, target_url):
    card_html = f"""
    <a class="link-card" href="{target_url}" target="_blank">
        <div class="link-content">
            <div class="icon-wrapper">
                <i data-lucide="{icon_name}" style="color: #A78BFA; width: 20px; height: 20px;"></i>
            </div>
            <div class="link-text-container">
                <span class="link-title">{title}</span>
                <span class="link-subtitle">{subtitle}</span>
            </div>
        </div>
        <button class="copy-btn" onclick="copyToClipboard('{target_url}', event); return false;">Copy</button>
    </a>
    """
    st.markdown(card_html, unsafe_allow_html=True)

# 6. Content Section - Portfolios & Digital Networks
st.markdown('<div class="section-label">Profiles & Hubs</div>', unsafe_allow_html=True)

render_link_card("globe", "Main Portfolio Website", "harkirankaur06.github.io/Portfolio", "https://harkirankaur06.github.io/Portfolio")
render_link_card("github", "GitHub Workspace", "github.com/harkirankaur06", "https://github.com/harkirankaur06")
render_link_card("linkedin", "LinkedIn Connection", "linkedin.com/in/harkiran-kaur-", "https://linkedin.com/in/harkiran-kaur-")
render_link_card("youtube", "Video Project Demos", "youtube.com/@harkirankaur-h5g", "https://youtube.com/@harkirankaur-h5g")

# 7. Content Section - Live Engine Deployments
st.markdown('<div class="section-label">Live Deployments</div>', unsafe_allow_html=True)

render_link_card("layers", "LEGEND Financial Digital Twin", "psb-steel.vercel.app", "https://psb-steel.vercel.app/")
render_link_card("activity", "Low-Q App", "low-q.vercel.app", "https://low-q.vercel.app")
render_link_card("terminal", "Unreal App", "unreal.streamlit.app", "https://unreal.streamlit.app")

# Execute Lucide script to process inline rendering tags accurately (MUST KEEP AT END)
st.markdown('<script>lucide.createIcons();</script>', unsafe_allow_html=True)

# 8. Clean Micro-Footer
st.markdown("<p style='text-align: center; font-size: 11px; color: #334155; margin-top: 5rem; letter-spacing: 0.5px; z-index: 10; position: relative;'>Personal Hub &copy; Harkiran Kaur</p>", unsafe_allow_html=True)