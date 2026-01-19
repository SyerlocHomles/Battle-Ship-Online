import streamlit as st
import numpy as np

# Fungsi untuk membuat grid (seperti kotak sudoku)
def render_battleship_grid(grid_data, title, interactive=False):
    st.subheader(title)
    
    # Header kolom A-J
    cols = st.columns([0.7] + [1]*10)
    for i, char in enumerate("ABCDEFGHIJ"):
        cols[i+1].write(f"**{char}**")

    for r in range(10):
        cols = st.columns([0.7] + [1]*10)
        cols[0].write(f"**{r+1}**") # Nomor baris
        for c in range(10):
            val = grid_data[r, c]
            
            # Logika Warna/Simbol
            # 0: Kosong, 1: Kapal, 2: Miss (Putih), 3: Hit (Merah)
            label = "🌊"
            if val == 2: label = "⚪"
            if val == 3: label = "💥"
            if val == 1 and not interactive: label = "🚢" # Kapal hanya terlihat di grid sendiri

            if interactive:
                # Grid atas (tempat nembak)
                if cols[c+1].button(label, key=f"target-{r}-{c}"):
                    st.session_state.last_shot = (r, c)
                    st.write(f"Menembak ke {chr(65+c)}{r+1}!")
            else:
                # Grid bawah (hanya tampilan posisi kita)
                cols[c+1].markdown(f"<div style='text-align:center'>{label}</div>", unsafe_allow_html=True)

# --- TAMPILAN UTAMA ---
st.title("🚢 Battleship Tactical Console")

# Inisialisasi data contoh jika belum ada
if 'my_ships' not in st.session_state:
    st.session_state.my_ships = np.zeros((10,10))
    st.session_state.enemy_shots = np.zeros((10,10))

# 1. GRID ATAS (Target: Klik untuk nembak lawan)
with st.container():
    render_battleship_grid(st.session_state.enemy_shots, "🎯 TARGET GRID (Tembak Lawan di Sini)", interactive=True)

st.divider() # Garis pemisah

# 2. GRID BAWAH (Ocean: Lihat posisi kapal sendiri)
with st.container():
    render_battleship_grid(st.session_state.my_ships, "⚓ OCEAN GRID (Kapal Milikmu)")
