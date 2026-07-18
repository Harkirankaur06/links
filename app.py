import streamlit as st
import base64

# 1. Page Configuration
st.set_page_config(
    page_title="Harkiran's Pop Hub! ✨",
    page_icon="🌈",
    layout="centered"
)

# 2. Hyper-Colorful, Bubbly & Lively CSS Engine
st.markdown("""
    <style>
    /* Reset Streamlit defaults */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Dynamic Candy Gradient Background */
    [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #FFDEE9 0%, #B5FFFC 100%) !important;
        background-attachment: fixed !important;
        overflow-x: hidden;
    }
    
    .block-container {
        padding-top: 2rem !important;
        padding-bottom: 3rem !important;
        max-width: 520px !important;
        position: relative;
        z-index: 10;
    }

    /* === INTERACTIVE GAME ZONE === */
    .game-zone {
        background: rgba(255, 255, 255, 0.9);
        border: 4px solid #000000;
        box-shadow: 8px 8px 0px #000000;
        border-radius: 30px;
        padding: 25px;
        text-align: center;
        margin-bottom: 2rem;
        position: relative;
        z-index: 20;
        user-select: none;
    }
    
    /* Interactive Canvas for click/pop tracking */
    #bubbleCanvas {
        background: transparent;
        display: block;
        margin: 15px auto 0 auto;
        border-radius: 20px;
        border: 2px dashed #000000;
        cursor: pointer;
    }
    
    /* Playful Wobbling Image Frame */
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
    }
    
    .profile-img {
        width: 100%; height: 100%;
        border-radius: 30% 70% 70% 30% / 30% 30% 70% 70%;
        object-fit: cover;
        background: #fff;
        overflow: hidden;
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

    <!-- HTML5 Canvas Active Game Engine Script -->
    <script>
    let score = 0;
    let bubbles = [];
    let canvas, ctx;

    function initGame() {
        canvas = document.getElementById('bubbleCanvas');
        if (!canvas) return;
        ctx = canvas.getContext('2d');
        
        // Handle window scaling context safely
        canvas.width = canvas.parentElement.clientWidth - 40;
        canvas.height = 180;

        // Spawn starter bubbles setup loop
        for(let i=0; i<6; i++) { spawnBubble(); }
        
        // Standard loop tick
        setInterval(updateGame, 30);
        
        canvas.addEventListener('click', checkPop);
    }

    function spawnBubble() {
        bubbles.push({
            x: Math.random() * (canvas.width - 40) + 20,
            y: canvas.height + Math.random() * 50,
            radius: Math.random() * 15 + 15,
            speed: Math.random() * 1 + 0.8,
            wobble: Math.random() * 2,
            wobbleSpeed: Math.random() * 0.05
        });
    }

    function updateGame() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        
        bubbles.forEach((b, index) => {
            b.y -= b.speed;
            b.wobble += b.wobbleSpeed;
            let currentX = b.x + Math.sin(b.wobble) * 10;
            
            // Draw gradient shiny bubble layout
            ctx.beginPath();
            let grad = ctx.createRadialGradient(currentX - b.radius/3, b.y - b.radius/3, 2, currentX, b.y, b.radius);
            grad.addColorStop(0, 'rgba(255, 255, 255, 0.9)');
            grad.addColorStop(0.4, 'rgba(0, 245, 212, 0.4)');
            grad.addColorStop(1, 'rgba(255, 0, 127, 0.3)');
            
            ctx.fillStyle = grad;
            ctx.strokeStyle = '#000000';
            ctx.lineWidth = 2;
            ctx.arc(currentX, b.y, b.radius, 0, Math.PI * 2);
            ctx.fill();
            ctx.stroke();
            
            // Recycle bubble if it floats off top canvas edge
            if (b.y + b.radius < 0) {
                bubbles.splice(index, 1);
                spawnBubble();
            }
        });
    }

    function checkPop(e) {
        const rect = canvas.getBoundingClientRect();
        const mouseX = e.clientX - rect.left;
        const mouseY = e.clientY - rect.top;
        
        bubbles.forEach((b, index) => {
            let currentX = b.x + Math.sin(b.wobble) * 10;
            let dist = Math.hypot(mouseX - currentX, mouseY - b.y);
            
            // Collision detection hit!
            if (dist < b.radius) {
                bubbles.splice(index, 1);
                score++;
                document.getElementById('score-value').innerText = score;
                spawnBubble();
                
                // Flash boundary layout border temporarily for game response loop
                const zone = document.getElementById('game-zone');
                zone.style.borderColor = '#00F5D4';
                setTimeout(() => zone.style.borderColor = '#000000', 100);
            }
        });
    }

    // Dynamic document check loop hook
    document.addEventListener("DOMContentLoaded", function() {
        setTimeout(initGame, 500);
    });
    // Fallback for direct loads
    if (document.readyState === "complete" || document.readyState === "interactive") {
        setTimeout(initGame, 500);
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
""", unsafe_allow_html=True)

# 3. Base64 Image Parser for Local Directory File
try:
    with open("AVATAR.jpg", "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    MY_PHOTO_URL = f"data:image/jpeg;base64,{encoded_string}"
except FileNotFoundError:
    MY_PHOTO_URL = "https://images.unsplash.com/photo-1494790108377-be9c29b29330?auto=format&fit=crop&w=200&q=80"

# Main Interactive UI Composition Block
st.markdown(f"""
    <div class="game-zone" id="game-zone">
        <div class="profile-frame">
            <img class="profile-img" src="{MY_PHOTO_URL}" alt="Harkiran Kaur"/>
        </div>
        <div class="profile-title">HARKIRAN KAUR</div>
        <div class="profile-subtitle">🍭 Bubbly Software Engineer & Developer</div>
        <div><div class="score-board">🎈 Bubbles Popped: <span id="score-value">0</span></div></div>
        
        <!-- Live HTML5 Game Node Area -->
        <canvas id="bubbleCanvas"></canvas>
    </div>
""", unsafe_allow_html=True)

# 4. Row Card Component Template
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