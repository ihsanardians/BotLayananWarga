import streamlit as st

st.set_page_config(
    page_title="LayananWarga AI",
    page_icon="🏛️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}


.stApp {
    background: #f8f9fc;
    color: #1e2235;
}

.block-container {
    max-width: 1100px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

header[data-testid="stHeader"] {
    background: transparent;
}

.brand {
    font-size: 1.25rem;
    font-weight: 800;
    color: #262344;
    letter-spacing: -0.5px;
}

.brand span {
    color: #7357e8;
}

.eyebrow {
    color: #7357e8;
    font-weight: 700;
    font-size: 0.82rem;
    letter-spacing: 1.5px;
    text-transform: uppercase;
}

.hero-title {
    font-size: clamp(2.3rem, 5vw, 3.6rem);
    line-height: 1.12;
    font-weight: 800;
    letter-spacing: -2px;
    color: #20213a;
    margin: 0.6rem 0 1rem 0;
}

.hero-title span {
    color: #7357e8;
}

.hero-desc {
    font-size: 1.05rem;
    line-height: 1.8;
    color: #72758a;
    max-width: 650px;
}

.section-title {
    font-size: 1.35rem;
    font-weight: 750;
    color: #252640;
    margin-bottom: 0.3rem;
}

.section-desc {
    color: #85879a;
    font-size: 0.92rem;
    margin-bottom: 1.2rem;
}

.service-card {
    background: white;
    border: 1px solid #ececf4;
    border-radius: 18px;
    padding: 1.3rem;
    min-height: 170px;
    box-shadow: 0 5px 20px rgba(38, 35, 68, 0.035);
}

.service-icon {
    font-size: 1.8rem;
    margin-bottom: 0.8rem;
}

.service-title {
    color: #282942;
    font-size: 1rem;
    font-weight: 700;
    margin-bottom: 0.45rem;
}

.service-desc {
    color: #85879a;
    font-size: 0.86rem;
    line-height: 1.6;
}

div.stButton > button {
    border-radius: 10px;
    border: 1px solid #e5e1fb;
    background: white;
    color: #5f49c8;
    font-weight: 600;
    min-height: 2.7rem;
    transition: all 0.2s ease;
}

div.stButton > button:hover {
    background: #f0edff;
    border-color: #7357e8;
    color: #5038bd;
}

div.stChatInput {
    border-radius: 14px;
}

/* Area pesan chat */
div[data-testid="stChatMessage"] {
    background: #ffffff !important;
    color: #20213a !important;
    border: 1px solid #dedff0;
    border-radius: 15px;
    padding: 0.7rem 1rem;
}

/* Pastikan teks dalam pesan terbaca */
div[data-testid="stChatMessage"] p,
div[data-testid="stChatMessage"] li {
    color: #20213a !important;
}

/* Kolom input chat */
div[data-testid="stChatInput"] {
    background: #ffffff !important;
}

div[data-testid="stChatInput"] textarea {
    color: #20213a !important;
    -webkit-text-fill-color: #20213a !important;
    background: #ffffff !important;
    caret-color: #7357e8 !important;
}

div[data-testid="stChatInput"] textarea::placeholder {
    color: #85879a !important;
    -webkit-text-fill-color: #85879a !important;
    opacity: 1;
}

div[data-testid="stChatInput"] > div {
    background: #ffffff !important;
    border: 1px solid #dedff0 !important;
    border-radius: 14px;
}

.footer {
    text-align: center;
    color: #a0a1b0;
    font-size: 0.8rem;
    padding-top: 2rem;
}
</style>
""", unsafe_allow_html=True)

# Header
left, right = st.columns([3, 1])

with left:
    st.markdown(
        '<div class="brand">✦ LayananWarga <span>AI</span></div>',
        unsafe_allow_html=True
    )

with right:
    st.markdown(
        '<div style="text-align:right;color:#85879a;font-size:0.85rem;'
        'padding-top:5px;">Asisten Pelayanan Publik</div>',
        unsafe_allow_html=True
    )

st.divider()

# Hero
st.markdown(
    '<div class="eyebrow">PELAYANAN PUBLIK INDONESIA</div>'
    '<div class="hero-title">Urusan publik,<br>'
    '<span>lebih mudah dipahami.</span></div>'
    '<div class="hero-desc">Bingung mengurus dokumen atau layanan pemerintah? '
    'Tanyakan kebutuhanmu dan dapatkan panduan langkah demi langkah, '
    'persyaratan, serta rujukan informasi resmi.</div>',
    unsafe_allow_html=True
)

st.write("")
st.write("")

# Service cards
st.markdown(
    '<div class="section-title">Mau mengurus apa hari ini?</div>'
    '<div class="section-desc">Pilih topik untuk memulai percakapan.</div>',
    unsafe_allow_html=True
)

services = [
    ("🪪", "KTP & Kartu Keluarga", "Informasi pembuatan dan perubahan data kependudukan.",
     "Bagaimana cara membuat KTP elektronik untuk pertama kali?"),
    ("🛵", "SIM & Kendaraan", "Panduan perpanjangan SIM dan administrasi kendaraan.",
     "Apa saja syarat perpanjangan SIM C?"),
    ("💰", "Pajak", "Panduan umum pajak kendaraan dan pajak pribadi.",
     "Bagaimana cara membayar pajak kendaraan tahunan?"),
    ("📄", "Dokumen Lainnya", "Cari tahu prosedur berbagai layanan administrasi.",
     "Bagaimana cara mengurus surat pindah domisili?")
]

cols = st.columns(4)

for col, (icon, title, desc, question) in zip(cols, services):
    with col:
        st.markdown(
            f'<div class="service-card">'
            f'<div class="service-icon">{icon}</div>'
            f'<div class="service-title">{title}</div>'
            f'<div class="service-desc">{desc}</div>'
            f'</div>',
            unsafe_allow_html=True
        )
        if st.button("Tanyakan →", key=title, use_container_width=True):
            st.session_state["suggested_question"] = question

st.write("")
st.write("")

# Chat area
st.markdown(
    '<div class="section-title">Tanya LayananWarga AI</div>'
    '<div class="section-desc">Mulai dengan pertanyaan yang ingin kamu ketahui.</div>',
    unsafe_allow_html=True
)

import os
from google import genai

# Mengambil API key dari environment variable
api_key = os.environ.get("GEMINI_API_KEY")

if not api_key:
    st.warning("API key Gemini belum dikonfigurasi.")
    st.stop()

client = genai.Client(api_key=api_key)

SYSTEM_PROMPT = """
Kamu adalah LayananWarga AI, asisten informasi pelayanan publik Indonesia.

Tugasmu:
- Membantu masyarakat memahami prosedur layanan publik dengan bahasa Indonesia
  yang jelas, ramah, dan mudah dipahami.
- Berikan langkah-langkah, persyaratan, dan perkiraan biaya hanya jika
  informasinya dapat dipastikan.
- Ketentuan dapat berbeda menurut daerah dan instansi. Tanyakan lokasi pengguna
  jika diperlukan.
- Jangan mengarang persyaratan, biaya, alamat, jadwal, atau tautan resmi.
- Jika tidak yakin atau informasi terbaru diperlukan, katakan dengan jujur
  dan sarankan pengguna memeriksa situs resmi instansi terkait.
- Kamu adalah asisten informasi independen, bukan layanan resmi pemerintah.
"""

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

prompt = st.chat_input("Contoh: Apa syarat membuat KTP baru?")

if prompt:
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    history = [
        {
            "role": "user" if m["role"] == "user" else "model",
            "parts": [{"text": m["content"]}]
        }
        for m in st.session_state.messages[:-1]
    ]

    with st.chat_message("assistant"):
        with st.spinner("LayananWarga AI sedang menyiapkan jawaban..."):
            try:
                response = client.models.generate_content(
                    model="gemini-3.5-flash-lite",
                    contents=history + [{
                        "role": "user",
                        "parts": [{"text": SYSTEM_PROMPT + "\n\nPertanyaan: " + prompt}]
                    }]
                )
                answer = response.text or (
                    "Maaf, saya belum bisa memberikan jawaban. "
                    "Silakan coba lagi."
                )
            except Exception:
                answer = (
                    # "Maaf, terjadi kendala saat menghubungi AI. "
                    # "Silakan coba kembali beberapa saat lagi."
                    f"Terjadi kendala saat menghubungi Gemini.\n\n"
                    f"**Jenis error:** `{type(e).__name__}`\n\n"
                    f"**Detail:** `{str(e)}`"
                )

        st.markdown(answer)

    st.session_state.messages.append({
        "role": "assistant",
        "content": answer
    })
