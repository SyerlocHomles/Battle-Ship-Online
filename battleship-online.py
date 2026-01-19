import streamlit as st
import numpy as np

st.set_page_config(layout="wide")

# CSS untuk Grid Sudoku Rapat dengan Header Hitam
st.markdown("""
<style>
    /* Menghilangkan gap antar kolom */
    [data-testid="column"] {
        padding: 0px !important;
        margin: 0px !important;
        gap: 0px !important;
    }
    
    /* Tombol Grid Biru Muda dengan Garis Hitam Tebal */
    .stButton > button {
        width: 100% !important;
        height: 45px !important;
        border-radius: 0px !important;
        border: 2px solid black !important;
        background-color: #ADD8E6 !important; /* Biru Muda */
        color: black !important;
        font-size: 20px !important;
        padding: 0px !important;
    }

    /* Label Koordinat Hitam Teks Putih */
    .coord-label {
        background-color: black;
        color: white;
        text-align: center;
        line-height: 45px;
        font-weight: bold;
        border: 1px solid #444;
        height: 45px;
    }
</style>
""", unsafe_allow_html=True)

# Inisialisasi State Papan (10x10) jika belum ada
if 'my_board' not in st.session_state:
    st.session_state.my_board = np.zeros((10, 10), dtype=int)

def place_ship(r, c):
    # Toggle: klik untuk pasang (1), klik lagi untuk hapus (0)
    if st.session_state.my_board[r, c] == 0:
        st.session_state.my_board[r, c] = 1
    else:
        st.session_state.my_board[r, c] = 0

def draw_clickable_grid(board_data, key_prefix):
    # Header A-J
    cols = st.columns([0.5] + [1]*10)
    cols[0].markdown('<div class="coord-label"></div>', unsafe_allow_html=True)
    for i, char in enumerate("ABCDEFGHIJ"):
        cols[i+1].markdown(f'<div class="coord-label">{char}</div>', unsafe_allow_html=True)

    # Baris 1-10
    for r in range(10):
        cols = st.columns([0.5] + [1]*10)
        cols[0].markdown(f'<div class="coord-label">{r+1}</div>', unsafe_allow_html=True)
        for c in range(10):
            # Cek apakah ada kapal di koordinat ini
            is_ship = board_data[r, c] == 1
            label = "●" if is_ship else "" # Titik hitam jika ada kapal
            
            # Gambar tombol
            cols[c+1].button(label, key=f"{key_prefix}-{r}-{c}", on_click=place_ship, args=(r, c))

# --- TAMPILAN UTAMA ---
st.title("🚢 Battleship Tactical Setup")
st.write("Klik pada kotak biru untuk menyusun siluet kapalmu (titik hitam).")

col1, col2 = st.columns(2)

with col1:
    st.subheader("PLAYER 1 (Your Board)")
    draw_clickable_grid(st.session_state.my_board, "p1")

with col2:
    st.subheader("ENEMY PREVIEW")
    # Grid musuh sementara statis
    draw_clickable_grid(np.zeros((10,10)), "p2")
