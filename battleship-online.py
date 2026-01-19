import streamlit as st

st.set_page_config(layout="wide")

# Inisialisasi state untuk menyimpan posisi kapal/klik
if 'clicks' not in st.session_state:
    st.session_state.clicks = set()

# CSS kamu tetap sama (Hanya ditambah sedikit untuk button di dalam tabel)
st.markdown("""
<style>
    .battleship-table {
        border-collapse: collapse;
        margin-left: auto;
        margin-right: auto;
        background-color: #ADD8E6;
    }
    
    .battleship-table td {
        border: 2px solid black;
        width: 45px;
        height: 45px;
        text-align: center;
        padding: 0px;
        position: relative; /* Penting untuk posisi tombol */
    }

    .label-cell {
        background-color: black !important;
        color: white !important;
        font-weight: bold;
        border: 2px solid #444 !important;
        width: 45px;
        height: 45px;
    }

    /* CSS Tambahan agar tombol Streamlit masuk ke dalam kotak tabel tanpa merusak garis */
    .stButton button {
        background-color: transparent !important;
        border: none !important;
        width: 100% !important;
        height: 45px !important;
        border-radius: 0px !important;
        padding: 0px !important;
        color: black !important;
        font-size: 20px !important;
    }
    
    .stButton button:hover {
        background-color: rgba(0,0,0,0.1) !important;
    }
</style>
""", unsafe_allow_html=True)

def create_grid_with_buttons(player_name, key_suffix):
    st.markdown(f"<h3 style='text-align: center;'>{player_name}</h3>", unsafe_allow_html=True)
    
    # 1. Header Huruf (Tetap HTML murni)
    cols_header = st.columns([1] + [1]*10)
    cols_header[0].markdown("<div class='label-cell' style='display: flex; align-items: center; justify-content: center;'></div>", unsafe_allow_html=True)
    letters = "ABCDEFGHIJ"
    for i, char in enumerate(letters):
        cols_header[i+1].markdown(f"<div class='label-cell' style='display: flex; align-items: center; justify-content: center;'>{char}</div>", unsafe_allow_html=True)

    # 2. Baris Angka + Tombol
    for i in range(1, 11):
        cols = st.columns([1] + [1]*10)
        # Angka di kiri
        cols[0].markdown(f"<div class='label-cell' style='display: flex; align-items: center; justify-content: center;'>{i}</div>", unsafe_allow_html=True)
        
        # Grid interaktif
        for j in range(10):
            key = f"{key_suffix}_{i}_{j}"
            # Cek apakah koordinat ini sudah diklik (ada kapal)
            label = "●" if key in st.session_state.clicks else ""
            
            if cols[j+1].button(label, key=key):
                if key in st.session_state.clicks:
                    st.session_state.clicks.remove(key)
                else:
                    st.session_state.clicks.add(key)
                st.rerun()

st.title("🚢 Battleship Tactical Board")

# Menampilkan dua grid bersandingan
col_p1, col_p2 = st.columns(2)

with col_p1:
    create_grid_with_buttons("PLAYER 1", "p1")

with col_p2:
    create_grid_with_buttons("PLAYER 2 / ENEMY", "p2")
