import streamlit as st

# 1. Page Configuration
st.set_page_config(
    page_title="Harkiran Kaur | Links",
    page_icon="💻",
    layout="centered"
)

# Custom Styling to mimic a premium link aggregator
st.markdown("""
    <style>
    /* Center the container and set a clean mobile-friendly width */
    .block-container {
        padding-top: 2rem;
        max-width: 520px;
    }
    /* Style the main links */
    div.stButton > button {
        width: 100%;
        border-radius: 12px;
        padding: 14px 20px;
        font-size: 16px;
        font-weight: 500;
        background-color: transparent;
        border: 1px solid #4A5568;
        text-align: left;
        display: flex;
        align-items: center;
        transition: all 0.2s ease-in-out;
    }
    div.stButton > button:hover {
        border-color: #6366F1;
        color: #6366F1;
        background-color: rgba(99, 102, 241, 0.05);
        transform: translateY(-2px);
    }
    /* Subheader spacing */
    .section-header {
        margin-top: 1.5rem;
        margin-bottom: 0.8rem;
        font-size: 14px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 1px;
        color: #A0AEC0;
    }
    </style>
""", unsafe_allow_html=True)

# 2. Profile Header Section
st.markdown("<h1 style='text-align: center; margin-bottom: 5px;'>HARKIRAN KAUR</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #718096; margin-bottom: 15px;'>📍 Delhi, India</p>", unsafe_allow_html=True)

# Contact Shortcuts (Quick icons right below the header)
col1, col2 = st.columns(2)
with col1:
    st.link_button("📞 +91 8585976065", "tel:8585976065")
with col2:
    st.link_button("✉️ Email Me", "mailto:harkirankaur.0606@gmail.com")

st.markdown("---")

# 3. Professional Networks & Profiles
st.markdown("<div class='section-header'>Profiles & Portfolios</div>", unsafe_allow_html=True)

st.link_button("🌐 Main Portfolio Website", "https://harkirankaur06.github.io/Portfolio")
st.link_button("🐙 GitHub Profile", "https://github.com/harkirankaur06")
st.link_button("💼 LinkedIn Network", "https://linkedin.com/in/harkiran-kaur-")
st.link_button("📺 Video Project Demos", "https://youtube.com/@harkirankaur-h5g")

# 4. Live Projects Section
st.markdown("<div class='section-header'>Live Deployments</div>", unsafe_allow_html=True)

st.link_button("🏗️ PSB Steel Platform", "https://psb-steel.vercel.app/")
st.link_button("⚡ Low-Q App", "https://low-q.vercel.app")
st.link_button("🎮 Unreal App", "https://unreal.streamlit.app")

st.markdown("---")

# 5. Footer
st.markdown("<p style='text-align: center; font-size: 12px; color: #A0AEC0;'>Built with Python & Streamlit</p>", unsafe_allow_html=True)