import streamlit as st

st.set_page_config(layout="wide")

# CSS untuk Header Hitam, Teks Putih, dan Grid Biru
st.markdown("""
<style>
    .battleship-table {
        border-collapse: collapse;
        margin-left: auto;
        margin-right: auto;
        background-color: #ADD8E6; /* Grid tetap Biru Muda */
    }
    
    /* Style untuk kotak grid permainan */
    .battleship-table td {
        border: 2px solid black; /* Garis hitam tebal */
        width: 45px;
        height: 45px;
        text-align: center;
        padding: 0px;
    }

    /* Style khusus untuk KOORDINAT (Hitam, Teks Putih) */
    .label-cell {
        background-color: black !important;
        color: white !important;
        font-weight: bold;
        border: 2px solid #444 !important; /* Garis abu gelap agar terlihat antar label */
    }

    .grid-container {
        display: flex;
        justify-content: space-around;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

def create_grid_html(player_name):
    # Membuat header huruf A-J (Hitam, Teks Putih)
    header = "<tr><td class='label-cell'></td>" + "".join([f"<td class='label-cell'>{c}</td>" for c in "ABCDEFGHIJ"]) + "</tr>"
    
    rows = ""
    for i in range(1, 11):
        # Membuat baris dengan angka di kiri (Hitam, Teks Putih) dan 10 kotak biru
        cells = "".join([f"<td></td>" for _ in range(10)])
        rows += f"<tr><td class='label-cell'>{i}</td>{cells}</tr>"
    
    return f"<div><h3>{player_name}</h3><table class='battleship-table'>{header}{rows}</table></div>"

st.title("🚢 Battleship Tactical Board")

# Menampilkan dua grid bersandingan
col1, col2 = st.columns(2)

with col1:
    st.markdown(create_grid_html("PLAYER 1"), unsafe_allow_html=True)

with col2:
    st.markdown(create_grid_html("PLAYER 2 / ENEMY"), unsafe_allow_html=True)
