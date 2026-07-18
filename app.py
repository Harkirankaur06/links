import streamlit as st

# 1. Initialize Page Profile & Global Config
st.set_page_config(
    page_title="Harkiran Kaur | Identity Hub",
    page_icon="✨",
    layout="centered"
)

# 2. Premium Engineering UI Overhaul (Neon Glassmorphism + Background Particles)
st.markdown("""
    <style>
    /* Absolute reset of Streamlit styling defaults */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stApp { background: #090D16 !important; }
    
    /* Layout Framework Constraints */
    .block-container {
        padding-top: 4rem !important;
        padding-bottom: 4rem !important;
        max-width: 540px !important;
        position: relative;
        z-index: 2;
    }
    
    /* Dynamic Moving Canvas Layer (Pure CSS Particles background) */
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
        background: radial-gradient(circle, rgba(99, 102, 241, 0.15) 0%, rgba(0,0,0,0) 70%);
        border-radius: 50%;
        animation: floatOrb 20s infinite alternate ease-in-out;
    }
    .orb-2 {
        position: absolute;
        bottom: 10%, right: 10%;
        width: 400px; height: 400px;
        background: radial-gradient(circle, rgba(168, 85, 247, 0.12) 0%, rgba(0,0,0,0) 70%);
        border-radius: 50%;
        animation: floatOrb 25s infinite alternate-reverse ease-in-out;
    }
    @keyframes floatOrb {
        0% { transform: translate(0px, 0px) scale(1); }
        100% { transform: translate(60px, 40px) scale(1.2); }
    }

    /* User Presentation Branding Card */
    .avatar-wrapper {
        display: flex;
        justify-content: center;
        margin-bottom: 18px;
    }
    .avatar-placeholder {
        width: 90px;
        height: 90px;
        border-radius: 50%;
        background: linear-gradient(135deg, #6366F1, #A855F7);
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 2rem;
        box-shadow: 0 0 25px rgba(99, 102, 241, 0.4);
        border: 2px solid rgba(255, 255, 255, 0.1);
    }
    
    .profile-title {
        font-family: system-ui, -apple-system, sans-serif;
        font-size: 2.6rem;
        font-weight: 900;
        letter-spacing: -1px;
        text-align: center;
        background: linear-gradient(to right, #FFFFFF, #CBD5E1);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 4px;
    }
    
    .profile-subtitle {
        font-size: 0.95rem;
        color: #94A3B8;
        text-align: center;
        margin-bottom: 24px;
        letter-spacing: 0.5px;
    }

    /* Core Action Links Setup */
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
        gap: 8px;
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 14px;
        padding: 12px;
        color: #E2E8F0 !important;
        font-weight: 600;
        font-size: 0.9rem;
        text-decoration: none !important;
        transition: all 0.2s;
    }
    .action-button:hover {
        background: rgba(255, 255, 255, 0.07);
        border-color: rgba(255, 255, 255, 0.2);
    }
    
    /* Section Headings Styling */
    .section-label {
        font-size: 0.75rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 2px;
        color: #818CF8;
        margin-top: 2rem;
        margin-bottom: 0.75rem;
        padding-left: 4px;
    }
    
    /* Interactive Cards Grid System */
    .link-card {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: rgba(15, 23, 42, 0.4);
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.05);
        border-radius: 18px;
        padding: 18px 22px;
        margin-bottom: 12px;
        text-decoration: none !important;
        transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
    }
    
    /* Dynamic Hover/Neon Border Glow Effects */
    .link-card:hover {
        transform: translateY(-3px) scale(1.01);
        background: rgba(15, 23, 42, 0.6);
        border-color: rgba(99, 102, 241, 0.3);
        box-shadow: 0 15px 30px -10px rgba(99, 102, 241, 0.2);
    }
    
    .link-content {
        display: flex;
        align-items: center;
        gap: 16px;
    }
    
    .icon-wrapper {
        width: 44px;
        height: 44px;
        background: linear-gradient(135deg, rgba(99, 102, 241, 0.1), rgba(168, 85, 247, 0.1));
        border: 1px solid rgba(99, 102, 241, 0.2);
        border-radius: 14px;
        display: flex;
        align-items: center;
        justify-content: center;
        transition: all 0.3s;
    }
    
    .link-card:hover .icon-wrapper {
        background: linear-gradient(135deg, #6366F1, #A855F7);
        border-color: transparent;
        transform: rotate(4deg);
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
        letter-spacing: -0.2px;
    }
    
    .link-subtitle {
        color: #475569 !important;
        font-size: 0.8rem;
        margin-top: 2px;
        transition: color 0.2s;
    }
    .link-card:hover .link-subtitle {
        color: #94A3B8 !important;
    }
    
    /* Copy Action Pill Button */
    .copy-btn {
        background: rgba(255, 255, 255, 0.03);
        border: 1px solid rgba(255, 255, 255, 0.05);
        color: #64748B;
        padding: 6px 12px;
        border-radius: 10px;
        font-size: 0.75rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.2s;
    }
    
    .copy-btn:hover {
        background: #FFFFFF;
        color: #0F172A;
        border-color: #FFFFFF;
        transform: scale(1.05);
    }
    </style>
    
    <!-- Custom Moving Asset Background Nodes -->
    <div class="bg-animation">
        <div class="orb" style="top: 10%; left: -10%;"></div>
        <div class="orb-2" style="bottom: 5%; right: -5%;"></div>
    </div>
    
    <!-- Inline Copy Handling Interactivity Script -->
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
                btn.style.background = 'rgba(255, 255, 255, 0.03)';
                btn.style.borderColor = 'rgba(255, 255, 255, 0.05)';
                btn.style.color = '#64748B';
            }, 1200);
        });
        return false;
    }
    </script>
""", unsafe_allow_html=True)

# 3. Import Vector Icons Library Engine
st.markdown('<script src="https://unpkg.com/lucide@latest"></script>', unsafe_allow_html=True)

# 4. Profile Header Branding
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

# Execute Lucide script to process inline rendering tags accurately
st.markdown('<script>lucide.createIcons();</script>', unsafe_allow_html=True)

# 8. Clean Micro-Footer
st.markdown("<p style='text-align: center; font-size: 11px; color: #334155; margin-top: 4rem; letter-spacing: 0.5px;'>Portfolio Links Engine • Generated via Streamlit</p>", unsafe_allow_html=True)