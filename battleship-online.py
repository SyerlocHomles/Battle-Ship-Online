import streamlit as st
import numpy as np

# Konfigurasi Halaman
st.set_page_config(page_title="Battleship Online", layout="centered")

# Inisialisasi State (Data yang tetap ada meski halaman direfresh)
if 'board' not in st.session_state:
    # 0: Air, 1: Kapal, 2: Meleset (Miss), 3: Kena (Hit)
    st.session_state.board = np.zeros((10, 10), dtype=int)
    st.session_state.turn = "Pemain 1"

def handle_click(r, c):
    # Logika sederhana: klik untuk menembak
    if st.session_state.board[r, c] == 0:
        st.session_state.board[r, c] = 2 # Anggap meleset dulu
    st.toast(f"Menembak koordinat: {chr(65+c)}{r+1}")

def draw_grid():
    # Header kolom A-J
    cols = st.columns([0.5] + [1]*10)
    for i, char in enumerate("ABCDEFGHIJ"):
        cols[i+1].markdown(f"**{char}**")

    # Baris 1-10
    for r in range(10):
        cols = st.columns([0.5] + [1]*10)
        cols[0].markdown(f"**{r+1}**")
        for c in range(10):
            val = st.session_state.board[r, c]
            
            # Warna dan label tombol berdasarkan status
            label = "🌊"
            if val == 2: label = "⚪" # Miss
            if val == 3: label = "💥" # Hit
            
            cols[c+1].button(label, key=f"btn-{r}-{c}", on_click=handle_click, args=(r, c))

st.title("🚢 Battleship Online")
st.write(f"Giliran: **{st.session_state.turn}**")

draw_grid()
