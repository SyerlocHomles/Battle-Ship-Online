import streamlit as st

# Mengatur agar halaman melebar agar cukup untuk 2 grid bersandingan
st.set_page_config(layout="wide")

# CSS untuk meniru persis gaya di gambar (Warna biru muda, garis hitam tebal)
st.markdown("""
    <style>
    /* Menghilangkan padding antar kolom Streamlit */
    [data-testid="column"] {
        padding: 0px !important;
        margin: 0px !important;
    }
    
    /* Style tombol agar berbentuk kotak, biru muda, dan garis hitam tebal */
    .stButton > button {
        width: 100%;
        height: 40px;
        border-radius: 0px;
        border: 2px solid black !important; /* Garis hitam tebal */
        background-color: #ADD8E6 !important; /* Biru muda sesuai gambar */
        color: black;
        font-weight: bold;
    }

    /* Efek saat tombol ditekan */
    .stButton > button:active, .stButton > button:focus {
        background-color: #87CEEB !important;
        border: 2px solid black !important;
    }

    /* Label header (A-J dan 1-10) */
    .grid-label {
        text-align: center;
        font-weight: bold;
        font-family: sans-serif;
    }
    </style>
    """, unsafe_allow_html=True)

def draw_battleship_grid(key_prefix):
    # Membuat Header Huruf A-J
    header_cols = st.columns([0.5] + [1]*10)
    letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    for i, l in enumerate(letters):
        header_cols[i+1].markdown(f'<p class="grid-label">{l}</p>', unsafe_allow_html=True)

    # Membuat 10 Baris
    for r in range(10):
        cols = st.columns([0.5] + [1]*10)
        # Label Angka di samping kiri
        cols[0].markdown(f'<p class="grid-label" style="line-height:40px;">{r+1}</p>', unsafe_allow_html=True)
        for c in range(10):
            if cols[c+1].button("", key=f"{key_prefix}-{r}-{c}"):
                st.toast(f"{key_prefix.upper()}: {letters[c]}{r+1}")

# --- TAMPILAN UTAMA (2 Kolom Besar) ---
main_col1, main_col2 = st.columns(2)

with main_col1:
    draw_battleship_grid("player1")
    st.markdown("<h2 style='text-align: center;'>PLAYER 1</h2>", unsafe_allow_html=True)

with main_col2:
    draw_battleship_grid("player2")
    st.markdown("<h2 style='text-align: center;'>PLAYER 2/ENEMY</h2>", unsafe_allow_html=True)
