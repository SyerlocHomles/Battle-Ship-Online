import streamlit as st

# 1. CSS Kustom untuk membuat Grid Polos ala Sudoku
st.markdown("""
    <style>
    /* Menghilangkan padding utama agar grid rapat */
    [data-testid="column"] {
        padding: 0px !important;
        margin: 0px !important;
    }
    
    /* Desain tombol menjadi kotak polos */
    .stButton > button {
        width: 100%;
        height: 45px; /* Sesuaikan tinggi kotak */
        border-radius: 0px;
        border: 0.5px solid #bdc3c7; /* Garis tipis antar kotak */
        background-color: white;
        transition: 0.2s;
    }

    /* Efek hover (saat kursor di atas kotak) */
    .stButton > button:hover {
        background-color: #f1f2f6;
        border-color: #3498db;
    }

    /* Logika Garis Tebal ala Sudoku (opsional, tiap 5 kotak untuk grid 10x10) */
    /* Jika ingin kotak benar-benar polos tanpa garis tebal, bagian ini bisa dihapus */
    </style>
    """, unsafe_allow_html=True)

def draw_clean_grid(key_prefix):
    # Membuat 10 baris
    for r in range(10):
        # Membuat 10 kolom
        cols = st.columns(10)
        for c in range(10):
            # Tombol kosong tanpa teks
            if cols[c].button("", key=f"{key_prefix}-{r}-{c}"):
                # Ini tempat kita menaruh logika klik nanti
                st.toast(f"Klik koordinat: Baris {r+1}, Kolom {c+1}")

# --- TAMPILAN UTAMA ---
st.title("🚢 Battleship Sudoku Style")

st.write("### 🎯 Target Grid")
draw_clean_grid("target")

st.markdown("<br><br>", unsafe_allow_html=True)

st.write("### ⚓ Your Fleet")
draw_clean_grid("home")
