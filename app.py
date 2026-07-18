import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Harkiran Kaur | Hub",
    page_icon="⚡",
    layout="centered"
)

# 2. Complete UI Overhaul (Modern Dark Glassmorphism Design)
st.markdown("""
    <style>
    /* Hide default Streamlit visual noise */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Main body container adjustments */
    .block-container {
        padding-top: 3rem !important;
        padding-bottom: 3rem !important;
        max-width: 580px !important;
    }
    
    /* Typography & Core Styles */
    body {
        color: #F7FAFC;
    }
    
    .profile-title {
        font-family: system-ui, -apple-system, sans-serif;
        font-size: 2.2rem;
        font-weight: 800;
        letter-spacing: -0.5px;
        text-align: center;
        background: linear-gradient(135deg, #6366F1 0%, #A855F7 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 2px;
    }
    
    .profile-subtitle {
        font-size: 1rem;
        color: #94A3B8;
        text-align: center;
        margin-bottom: 20px;
        font-weight: 500;
    }
    
    /* Section Headings */
    .section-label {
        font-size: 0.8rem;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 1.5px;
        color: #6366F1;
        margin-top: 2rem;
        margin-bottom: 0.8rem;
        padding-left: 4px;
    }
    
    /* Custom Modern Link Cards */
    .link-card {
        display: flex;
        justify-content: space-between;
        align-items: center;
        background: rgba(30, 41, 59, 0.7);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 16px;
        padding: 16px 20px;
        margin-bottom: 12px;
        transition: all 0.25s cubic-bezier(0.4, 0, 0.2, 1);
        text-decoration: none !important;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    }
    
    .link-card:hover {
        transform: translateY(-2px);
        background: rgba(30, 41, 59, 0.9);
        border-color: rgba(99, 102, 241, 0.4);
        box-shadow: 0 10px 15px -3px rgba(99, 102, 241, 0.1), 0 4px 6px -2px rgba(99, 102, 241, 0.05);
    }
    
    .link-content {
        display: flex;
        align-items: center;
        gap: 14px;
    }
    
    .link-icon {
        font-size: 1.3rem;
    }
    
    .link-text-container {
        display: flex;
        flex-direction: column;
    }
    
    .link-title {
        color: #F8FAFC !important;
        font-weight: 600;
        font-size: 1rem;
    }
    
    .link-subtitle {
        color: #64748B !important;
        font-size: 0.8rem;
        margin-top: 1px;
    }
    
    /* Copy Action Button Styling */
    .copy-btn {
        background: rgba(255, 255, 255, 0.05);
        border: none;
        color: #94A3B8;
        padding: 6px 10px;
        border-radius: 8px;
        font-size: 0.75rem;
        font-weight: 600;
        cursor: pointer;
        transition: all 0.2s;
    }
    
    .copy-btn:hover {
        background: rgba(99, 102, 241, 0.2);
        color: #F8FAFC;
    }
    </style>
    
    <!-- JavaScript Functionality for Quick Copy -->
    <script>
    function copyToClipboard(text, e) {
        if(e) { e.preventDefault(); e.stopPropagation(); }
        navigator.clipboard.writeText(text).then(() => {
            const btn = window.event.target;
            const originalText = btn.innerText;
            btn.innerText = 'Copied! ✓';
            btn.style.background = '#22C55E';
            btn.style.color = '#FFFFFF';
            setTimeout(() => {
                btn.innerText = originalText;
                btn.style.background = 'rgba(255, 255, 255, 0.05)';
                btn.style.color = '#94A3B8';
            }, 1500);
        });
        return false;
    }
    </script>
""", unsafe_allow_html=True)

# 3. Header Profile Layout
st.markdown('<div class="profile-title">HARKIRAN KAUR</div>', unsafe_allow_html=True)
st.markdown('<div class="profile-subtitle">💻 Software Engineer & Student | 📍 Delhi, India</div>', unsafe_allow_html=True)

# Clean, modern layout grid for basic direct actions
col1, col2 = st.columns(2)
with col1:
    st.link_button("📞 Call Direct", "tel:8585976065", use_container_width=True)
with col2:
    st.link_button("✉️ Email Direct", "mailto:harkirankaur.0606@gmail.com", use_container_width=True)

# 4. Helper Function to Generate Custom Embedded Cards
def render_link_card(icon, title, subtitle, target_url):
    card_html = f"""
    <a class="link-card" href="{target_url}" target="_blank">
        <div class="link-content">
            <span class="link-icon">{icon}</span>
            <div class="link-text-container">
                <span class="link-title">{title}</span>
                <span class="link-subtitle">{subtitle}</span>
            </div>
        </div>
        <button class="copy-btn" onclick="copyToClipboard('{target_url}', event); return false;">Copy Link</button>
    </a>
    """
    st.markdown(card_html, unsafe_allow_html=True)

# 5. Core Portfolios & Networks Section
st.markdown('<div class="section-label">Profiles & Hubs</div>', unsafe_allow_html=True)

render_link_card("🌐", "Main Portfolio Website", "harkirankaur06.github.io/Portfolio", "https://harkirankaur06.github.io/Portfolio")
render_link_card("🐙", "GitHub Workspace", "github.com/harkirankaur06", "https://github.com/harkirankaur06")
render_link_card("💼", "LinkedIn Connection", "linkedin.com/in/harkiran-kaur-", "https://linkedin.com/in/harkiran-kaur-")
render_link_card("📺", "Video Project Demos", "youtube.com/@harkirankaur-h5g", "https://youtube.com/@harkirankaur-h5g")

# 6. Live Project Implementations Section
st.markdown('<div class="section-label">Live Deployments</div>', unsafe_allow_html=True)

render_link_card("🏗️", "PSB Steel Platform", "psb-steel.vercel.app", "https://psb-steel.vercel.app/")
render_link_card("⚡", "Low-Q App", "low-q.vercel.app", "https://low-q.vercel.app")
render_link_card("🎮", "Unreal App", "unreal.streamlit.app", "https://unreal.streamlit.app")

# 7. Mini Footer
st.markdown("<p style='text-align: center; font-size: 11px; color: #475569; margin-top: 3rem;'>Custom Engine • Built using Python & Streamlit</p>", unsafe_allow_html=True)