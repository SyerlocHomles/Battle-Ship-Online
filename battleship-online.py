import streamlit as st

# 1. CSS Kustom dengan logika Garis Tebal (nth-child)
st.markdown("""
    <style>
    [data-testid="column"] {
        padding: 0px !important;
        margin: 0px !important;
    }
    
    .stButton > button {
        width: 100%;
        height: 45px;
        border-radius: 0px;
        border: 0.5px solid #bdc3c7;
        background-color: white;
    }

    /* Garis tebal vertikal setelah kolom ke-5 */
    [data-testid="column"]:nth-child(5) {
        border-right: 3px solid black !important;
    }

    /* Garis tebal horizontal setelah baris ke-5 */
    .thick-row {
        border-bottom: 3px solid black !important;
    }
    
    .stButton > button:hover {
        background-color: #f1f2f6;
        border-color: #3498db;
    }
    </style>
    """, unsafe_allow_html=True)

def draw_sudoku_style_grid(key_prefix):
    for r in range(10):
        # Tambahkan div khusus untuk memberi garis bawah tebal pada baris ke-5
        is_thick = "thick-row" if r == 4 else ""
        
        st.markdown(f'<div class="{is_thick}">', unsafe_allow_html=True)
        cols = st.columns(10)
        for c in range(10):
            if cols[c].button("", key=f"{key_prefix}-{r}-{c}"):
                st.toast(f"Baris {r+1}, Kolom {c+1}")
        st.markdown('</div>', unsafe_allow_html=True)

# --- TAMPILAN UTAMA ---
st.title("⚓ Battleship Sudoku Grid")

st.write("### 🎯 Target Grid")
draw_sudoku_style_grid("target")

st.write("### 🚢 Your Fleet")
draw_sudoku_style_grid("home")
