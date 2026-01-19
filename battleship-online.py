import streamlit as st

st.set_page_config(layout="wide")

# Inisialisasi state untuk menyimpan koordinat yang diklik
if 'clicks' not in st.session_state:
    st.session_state.clicks = set()

# CSS ASLI KAMU (Ditambah sedikit agar tombol transparan)
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
    }
    .label-cell {
        background-color: black !important;
        color: white !important;
        font-weight: bold;
        border: 2px solid #444 !important;
    }
    /* Tombol transparan di atas sel tabel */
    .stButton button {
        background-color: transparent !important;
        border: none !important;
        width: 45px !important;
        height: 45px !important;
        padding: 0px !important;
        margin: 0px !important;
        color: black !important;
        font-size: 20px !important;
    }
    .stButton button:hover {
        background-color: rgba(255, 255, 255, 0.3) !important;
    }
</style>
""", unsafe_allow_html=True)

def draw_game_grid(player_prefix):
    # Membuat header huruf A-J
    letters = "ABCDEFGHIJ"
    
    # Kita mulai membangun tabel HTML secara manual agar rapat
    html_table = f"<table class='battleship-table'>"
    
    # 1. Baris Header (Hitam)
    html_table += "<tr><td class='label-cell'></td>"
    for char in letters:
        html_table += f"<td class='label-cell'>{char}</td>"
    html_table += "</tr>"
    
    # Menampilkan baris demi baris
    st.write(f"### {player_prefix}")
    
    # Agar tombol Streamlit bisa masuk ke dalam tabel, kita gunakan st.columns 
    # di dalam loop, tapi kita bungkus dengan container yang sangat rapat.
    
    # HEADER (A-J)
    header_cols = st.columns([0.5] + [1]*10)
    header_cols[0].markdown("<div class='label-cell' style='height:45px; line-height:45px; text-align:center;'></div>", unsafe_allow_html=True)
    for i, char in enumerate(letters):
        header_cols[i+1].markdown(f"<div class='label-cell' style='height:45px; line-height:45px; text-align:center;'>{char}</div>", unsafe_allow_html=True)

    # GRID (1-10)
    for r in range(1, 11):
        cols = st.columns([0.5] + [1]*10)
        # Angka di kiri (Hitam)
        cols[0].markdown(f"<div class='label-cell' style='height:45px; line-height:45px; text-align:center;'>{r}</div>", unsafe_allow_html=True)
        
        # Kotak Biru (Tombol)
        for c in range(10):
            key = f"{player_prefix}_{r}_{c}"
            label = "●" if key in st.session_state.clicks else ""
            
            # Setiap kolom berisi satu tombol yang diformat oleh CSS tadi
            if cols[c+1].button(label, key=key):
                if key in st.session_state.clicks:
                    st.session_state.clicks.remove(key)
                else:
                    st.session_state.clicks.add(key)
                st.rerun()

st.title("🚢 Battleship Tactical Board")

col1, col2 = st.columns(2)

with col1:
    draw_game_grid("PLAYER 1")

with col2:
    draw_game_grid("PLAYER 2")
