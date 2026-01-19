import streamlit as st
import numpy as np

st.set_page_config(layout="wide")

# CSS AGRESIF: Memaksa Streamlit menghilangkan semua gap/jarak
st.markdown("""
<style>
    /* 1. Menghilangkan gap horizontal antar kolom */
    [data-testid="column"] {
        padding: 0px !important;
        margin: 0px !important;
        gap: 0px !important;
    }
    
    /* 2. Menghilangkan gap antar baris */
    [data-testid="stVerticalBlock"] > div {
        padding-top: 0px !important;
        padding-bottom: 0px !important;
    }

    /* 3. Style Tombol: Biru Muda, Garis Hitam Tebal, Tanpa Jarak */
    .stButton > button {
        width: 100% !important;
        height: 45px !important;
        border-radius: 0px !important;
        border: 2px solid black !important; /* Garis hitam tebal */
        background-color: #ADD8E6 !important; /* Biru muda */
        color: black !important;
        font-size: 20px !important;
        padding: 0px !important;
        margin: 0px !important;
        display: block !important;
    }

    /* 4. Label Koordinat: Hitam, Teks Putih */
    .coord-label {
        background-color: black;
        color: white;
        text-align: center;
        line-height: 45px;
        font-weight: bold;
        border: 2px solid black;
        height: 45px;
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

if 'my_board' not in st.session_state:
    st.session_state.my_board = np.zeros((10, 10), dtype=int)

def place_ship(r, c):
    if st.session_state.my_board[r, c] == 0:
        st.session_state.my_board[r, c] = 1
    else:
        st.session_state.my_board[r, c] = 0

def draw_sudoku_grid(board_data, key_prefix):
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
            is_ship = board_data[r, c] == 1
            label = "●" if is_ship else ""
            cols[c+1].button(label, key=f"{key_prefix}-{r}-{c}", on_click=place_ship, args=(r, c))

# --- TAMPILAN UTAMA ---
st.title("⚓ Battleship Sudoku Mode")

col1, col2 = st.columns(2)

with col1:
    st.subheader("PLAYER 1")
    draw_sudoku_grid(st.session_state.my_board, "p1")

with col2:
    st.subheader("PLAYER 2/ENEMY")
    draw_sudoku_grid(np.zeros((10,10)), "p2")
