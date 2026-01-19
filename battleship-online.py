import streamlit as st
import numpy as np

# 1. CSS Custom untuk membuat grid rapat dan kotak (Square)
st.markdown("""
    <style>
    /* Menghilangkan padding antar kolom */
    [data-testid="column"] {
        padding: 0px 1px !important;
        margin: 0px !important;
    }
    /* Memaksa tombol menjadi kotak sempurna */
    .stButton > button {
        width: 100%;
        height: 40px;
        padding: 0px !important;
        border-radius: 0px;
        border: 1px solid #d1d1d1;
        background-color: white;
        color: black;
        font-size: 10px;
    }
    /* Warna saat kursor di atas kotak (hover) */
    .stButton > button:hover {
        background-color: #f0f2f6;
        border-color: #ff4b4b;
    }
    </style>
    """, unsafe_allow_html=True)

def draw_sudoku_grid(prefix):
    # Header Huruf A-J
    cols = st.columns([0.5] + [1]*10)
    for i, char in enumerate("ABCDEFGHIJ"):
        cols[i+1].markdown(f"<p style='text-align:center; font-weight:bold;'>{char}</p>", unsafe_allow_html=True)

    # Grid 10x10
    for r in range(10):
        cols = st.columns([0.5] + [1]*10)
        cols[0].markdown(f"<p style='line-height:40px; font-weight:bold;'>{r+1}</p>", unsafe_allow_html=True)
        for c in range(10):
            # Key harus unik antara grid atas dan bawah, maka pakai prefix
            if cols[c+1].button(" ", key=f"{prefix}-{r}-{c}"):
                st.toast(f"Koordinat: {chr(65+c)}{r+1}")

# --- TAMPILAN UTAMA ---
st.title("⚓ Battleship Online")

st.write("### 🎯 Target Grid")
draw_sudoku_grid("top")

st.markdown("<br>", unsafe_allow_html=True) # Jarak antar grid

st.write("### 🚢 Your Fleet")
draw_sudoku_grid("bottom")
