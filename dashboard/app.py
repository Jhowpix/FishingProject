import streamlit as st
import psycopg
import pandas as pd
from streamlit_autorefresh import st_autorefresh

connection = psycopg.connect(
    host="localhost",
    dbname="fishing_game",
    user="postgres",
    password="senha"
)

cursor = connection.cursor()

cursor.execute("""
    SELECT player, area, fish, rarity, value, xp, equipment
    FROM fishing_records
""")

records = cursor.fetchall()

df = pd.DataFrame(
    records,
    columns=[
        "player",
        "area",
        "fish",
        "rarity",
        "value",
        "xp",
        "equipment"
    ]
)

st_autorefresh(
    interval=10000,
    key="fishing_dashboard"
)

st.title("🎣 Fishing Analytics")
#st.write("Dashboard do projeto de pesca")

st.metric("   TOTAL DE PEIXES.", len(df))
st.dataframe(df)

st.metric(
    label="💰  VALOR TOTAL DOS PEIXES.",
    value=f"R$ {df['value'].sum():,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
)
st.metric(
    label="🔝 TOTAL XP! GANHOS.",
    value=f"{df['xp'].sum():,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
)

