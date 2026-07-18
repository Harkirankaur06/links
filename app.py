import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Harkiran Kaur | Hub",
    page_icon="✨",
    layout="centered"
)

# 2. Bulletproof UI Styling (Applied directly to native Streamlit classes)
st.markdown("""
    <style>
    /* Hide default Streamlit frames */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Apply the animated gradient directly to Streamlit's app wrapper */
    [data-testid="stAppViewContainer"] {
        background: radial-gradient(circle at 20% 20%, rgba(99, 102, 241, 0.15) 0%, transparent 40%),
                    radial-gradient(circle at 80% 80%, rgba(168, 85, 247, 0.15) 0%, transparent 50%),
                    #070a13 !important;
        background-attachment: fixed !important;
    }
    
    /* Content wrapper constraints */
    .block-container {
        padding-top: 4rem !important;
        padding-bottom: 4rem !important;
        max-width: 540px !important;
    }
    
    /* Typography & Profile Header */
    .profile-container {
        text-align: center;
        margin-bottom: 2rem;
    }
    
    .avatar-placeholder {
        width: 96px;
        height: 96px;
        border-radius: 50%;
        background: linear-gradient(135deg, #6366F1, #A855F7);
        display: inline-flex;
        align-items: center;
        justify-content: center;
        font-size: 2.2rem;
        box-shadow: 0 0 30px rgba(99, 102, 241, 0.4);
        border: 2px solid rgba(255, 255, 255, 0.2);
        margin-bottom: 15px;
        animation: pulseGlow 3s infinite alternate ease-in-out;
    }
    
    @keyframes pulseGlow {
        0% { transform: scale(1); box-shadow: 0 0 25px rgba(99, 102, 241, 0.4); }
        100% { transform: scale(1.04); box-shadow: 0 0 40px rgba(168, 85, 247, 0.6); }
    }
    
    .profile-title {
        font-family: system-ui, -apple-system, sans-serif;
        font-size: 2.6rem;
        font-weight: 900;
        letter-spacing: -1px;
        color: #FFFFFF !important;
        margin-bottom: 6px;
    }
    
    .profile-subtitle {
        font-size: 0.95rem;
        color: #94A3B8 !important;
        letter-spacing: 0.5px;
    }

    /* Grid layout for Action Links */
    .action-grid {
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 12px;
        margin-bottom: 2rem;
    }
    .action-button {
        display: flex;
        align-items: center;
        justify-content: center;
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 14px;
        padding: 12px;
        color: #F1F5F9 !important;
        font-weight: 600;
        font-size: 0.9rem;
        text-decoration: none !important;
        transition: all 0.2s ease;
    }
    .action-button:hover {
        background: rgba(255, 255, 255, 0.08);
        border-color: rgba(255, 255, 255, 0.2);
        transform: translateY(-2px);
    }
    
    /* Section Separation Labels */
    .section-label {
        font-size: 0.75rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 2px;
        color: #818CF8;
        margin-top: 2rem;
        margin-bottom: 0.8rem;
        padding-left: 2px;
    }
    
    /* Interactive Glassmorphic Custom Cards */
    .link-card {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: rgba(15, 23, 42, 0.45);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.06);
        border-radius: 18px;
        padding: 16px 20px;
        margin-bottom: 12px;
        text-decoration: none !important;
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }
    
    .link-card:hover {
        transform: translateY(-3px) scale(1.01);
        background: rgba(15, 23, 42, 0.65);
        border-color: rgba(99, 102, 241, 0.4);
        box-shadow: 0 16px 32px -10px rgba(99, 102, 241, 0.3);
    }
    
    .link-content {
        display: flex;
        align-items: center;
        gap: 14px;
    }
    
    .icon-wrapper {
        width: 42px;
        height: 42px;
        background: rgba(99, 102, 241, 0.1);
        border: 1px solid rgba(99, 102, 241, 0.2);
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        transition: all 0.3s ease;
    }
    
    .link-card:hover .icon-wrapper {
        background: linear-gradient(135deg, #6366F1, #A855F7);
        border-color: transparent;
        transform: rotate(5deg) scale(1.05);
    }
    
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
        font-size: 1.05rem;
    }
    
    .link-subtitle {
        color: #64748B !important;
        font-size: 0.8rem;
        margin-top: 2px;
    }
    
    .link-card:hover .link-subtitle {
        color: #CBD5E1 !important;
    }
    
    /* Interactive Clipboard Action Button */
    .copy-btn {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.08);
        color: #94A3B8;
        padding: 6px 12px;
        border-radius: 10px;
        font-size: 0.75rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.2s ease;
    }
    
    .copy-btn:hover {
        background: #FFFFFF;
        color: #0F172A;
        border-color: #FFFFFF;
    }
    </style>
    
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
                btn.style.borderColor = 'rgba(255, 255, 255, 0.08)';
                btn.style.color = '#94A3B8';
            }, 1200);
        });
        return false;
    }
    </script>
""", unsafe_allow_html=True)

# 3. Import Vector Icons Library Engine
st.markdown('<script src="https://unpkg.com/lucide@latest"></script>', unsafe_allow_html=True)

# 4. Profile Presentational UI Header
st.markdown("""
    <div class="profile-container">
        <div class="avatar-placeholder">👩‍💻</div>
        <div class="profile-title">HARKIRAN KAUR</div>
        <div class="profile-subtitle">📍 Delhi, India &nbsp;•&nbsp; Software Engineer</div>
    </div>
""", unsafe_allow_html=True)

# Call/Email Grid
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
                <i data-lucide="{icon_name}" style="color: #818CF8; width: 18px; height: 18px;"></i>
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

# 6. Content Section - Profiles & Digital Networks
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

# Injects the execution handler to activate icons
st.markdown('<script>lucide.createIcons();</script>', unsafe_allow_html=True)