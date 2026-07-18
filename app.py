import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Harkiran Kaur | Hub",
    page_icon="⚡",
    layout="centered"
)

# 2. Advanced CSS Layout with Animations, Motion Mechanics & Custom Icons
st.markdown("""
    <style>
    /* Hide default Streamlit frames */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Document Container & Dynamic Sizing */
    .block-container {
        padding-top: 3rem !important;
        padding-bottom: 4rem !important;
        max-width: 600px !important;
    }
    
    /* Gradient Profile Header Layout */
    .profile-title {
        font-family: system-ui, -apple-system, sans-serif;
        font-size: 2.5rem;
        font-weight: 800;
        letter-spacing: -0.5px;
        text-align: center;
        background: linear-gradient(135deg, #818CF8 0%, #C084FC 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 4px;
        animation: smoothFloat 4s ease-in-out infinite alternate;
    }
    
    .profile-subtitle {
        font-size: 1rem;
        color: #94A3B8;
        text-align: center;
        margin-bottom: 24px;
        font-weight: 500;
    }

    /* Soft floating effect for branding elements */
    @keyframes smoothFloat {
        0% { transform: translateY(0px); }
        100% { transform: translateY(-4px); }
    }
    
    /* Section Headings */
    .section-label {
        font-size: 0.8rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 2px;
        color: #818CF8;
        margin-top: 2.5rem;
        margin-bottom: 1rem;
        padding-left: 4px;
    }
    
    /* Premium Interactive Link Cards */
    .link-card {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: rgba(30, 41, 59, 0.5);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 18px 24px;
        margin-bottom: 14px;
        text-decoration: none !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        
        /* Smooth state transitions for interactive movement */
        transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1);
        position: relative;
        overflow: hidden;
    }
    
    /* Dynamic Movement & Glow on Hover */
    .link-card:hover {
        transform: translateY(-4px) scale(1.01);
        background: rgba(30, 41, 59, 0.8);
        border-color: rgba(129, 140, 248, 0.4);
        box-shadow: 0 12px 20px -3px rgba(129, 140, 248, 0.15), 0 4px 6px -2px rgba(129, 140, 248, 0.05);
    }
    
    .link-content {
        display: flex;
        align-items: center;
        gap: 16px;
    }
    
    /* Icon Formatting (Circular background badge) */
    .icon-wrapper {
        width: 42px;
        height: 42px;
        background: rgba(255, 255, 255, 0.05);
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        transition: all 0.3s;
    }
    
    .link-card:hover .icon-wrapper {
        background: rgba(129, 140, 248, 0.2);
        transform: rotate(6deg);
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
    
    /* Interactive Copy Button Bubble */
    .copy-btn {
        background: rgba(255, 255, 255, 0.04);
        border: 1px solid rgba(255, 255, 255, 0.05);
        color: #94A3B8;
        padding: 8px 14px;
        border-radius: 10px;
        font-size: 0.75rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.2s;
        z-index: 10;
    }
    
    .copy-btn:hover {
        background: #818CF8;
        color: #FFFFFF;
        border-color: #818CF8;
    }
    </style>
    
    <!-- Injection of JavaScript Clipboard Operations -->
    <script>
    function copyToClipboard(text, e) {
        if(e) { e.preventDefault(); e.stopPropagation(); }
        navigator.clipboard.writeText(text).then(() => {
            const btn = window.event.target;
            const originalText = btn.innerText;
            btn.innerText = 'Copied! ✓';
            btn.style.background = '#10B981';
            btn.style.borderColor = '#10B981';
            btn.style.color = '#FFFFFF';
            setTimeout(() => {
                btn.innerText = originalText;
                btn.style.background = 'rgba(255, 255, 255, 0.04)';
                btn.style.borderColor = 'rgba(255, 255, 255, 0.05)';
                btn.style.color = '#94A3B8';
            }, 1500);
        });
        return false;
    }
    </script>
""", unsafe_allow_html=True)

# 3. Injecting Vector Icon Library (Lucide CDN)
st.markdown('<script src="https://unpkg.com/lucide@latest"></script>', unsafe_allow_html=True)

# 4. Profile Presentational Identity
st.markdown('<div class="profile-title">HARKIRAN KAUR</div>', unsafe_allow_html=True)
st.markdown('<div class="profile-subtitle">💻 Software Engineer & Student | 📍 Delhi, India</div>', unsafe_allow_html=True)

# Call/Email Quick Action Buttons
col1, col2 = st.columns(2)
with col1:
    st.link_button("📞 Quick Call", "tel:8585976065", use_container_width=True)
with col2:
    st.link_button("✉️ Drop Email", "mailto:harkirankaur.0606@gmail.com", use_container_width=True)

# 5. Core Interface Rendering Function (Combines SVG Vector Layouts + Data Structure)
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

# 6. Primary Directory Mapping
st.markdown('<div class="section-label">Profiles & Hubs</div>', unsafe_allow_html=True)

render_link_card("globe", "Main Portfolio Website", "harkirankaur06.github.io/Portfolio", "https://harkirankaur06.github.io/Portfolio")
render_link_card("github", "GitHub Workspace", "github.com/harkirankaur06", "https://github.com/harkirankaur06")
render_link_card("linkedin", "LinkedIn Connection", "linkedin.com/in/harkiran-kaur-", "https://linkedin.com/in/harkiran-kaur-")
render_link_card("youtube", "Video Project Demos", "youtube.com/@harkirankaur-h5g", "https://youtube.com/@harkirankaur-h5g")

# 7. Production Implementations Mapping (Featuring Updated Title)
st.markdown('<div class="section-label">Live Deployments</div>', unsafe_allow_html=True)

render_link_card("cpu", "LEGEND Financial Digital Twin", "psb-steel.vercel.app", "https://psb-steel.vercel.app/")
render_link_card("zap", "Low-Q Scientific Digital Twin", "low-q.vercel.app", "https://low-q.vercel.app")
render_link_card("gamepad-2", "Unreal App", "unreal.streamlit.app", "https://unreal.streamlit.app")

# Injects the execution handler ensuring vector shapes accurately draw inside standard layouts
st.markdown('<script>lucide.createIcons();</script>', unsafe_allow_html=True)

# 8. Mini Footer
st.markdown("<p style='text-align: center; font-size: 11px; color: #475569; margin-top: 4rem;'>Custom Engine • Built using Python & Streamlit</p>", unsafe_allow_html=True)