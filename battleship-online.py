import streamlit as st

st.set_page_config(layout="wide")

# CSS untuk memaksa tabel menjadi biru muda dengan garis hitam tebal
st.markdown("""
<style>
    .battleship-table {
        border-collapse: collapse; /* Ini yang membuat garis menyatu seperti sudoku */
        margin-left: auto;
        margin-right: auto;
        background-color: #ADD8E6; /* Biru muda */
    }
    .battleship-table td {
        border: 2px solid black; /* Garis hitam tebal */
        width: 40px;
        height: 40px;
        text-align: center;
        padding: 0px;
    }
    .grid-container {
        display: flex;
        justify-content: space-around;
        text-align: center;
    }
    .label-row { font-weight: bold; }
    .label-col { font-weight: bold; padding-right: 10px; }
</style>
""", unsafe_allow_html=True)

def create_grid_html():
    # Membuat header huruf A-J
    header = "<tr><td></td>" + "".join([f"<td class='label-row'>{c}</td>" for c in "ABCDEFGHIJ"]) + "</tr>"
    
    rows = ""
    for i in range(1, 11):
        # Membuat baris dengan angka di kiri dan 10 kotak biru
        cells = "".join([f"<td></td>" for _ in range(10)])
        rows += f"<tr><td class='label-col'>{i}</td>{cells}</tr>"
    
    return f"<table class='battleship-table'>{header}{rows}</table>"

st.title("🚢 Battleship Online")

# Menampilkan dua grid bersandingan
col1, col2 = st.columns(2)

grid_html = create_grid_html()

with col1:
    st.markdown(grid_html, unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>PLAYER 1</h3>", unsafe_allow_html=True)

with col2:
    st.markdown(grid_html, unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>PLAYER 2/ENEMY</h3>", unsafe_allow_html=True)
