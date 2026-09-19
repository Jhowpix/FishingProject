import streamlit as st
import psycopg
import pandas as pd

connection = psycopg.connect(
    host="localhost",
    dbname="fishing_game",
    user="postgres",
    password="Sua Senha Aqui"
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

st.title("🎣 Fishing Analytics")
st.write("Dashboard do projeto de pesca")

st.metric("🎣 Total de pescarias", len(df))
st.dataframe(df)

st.metric(
    label="💰 Total do valor gerado em todas as pescas.",
    value=f"R$ {df['value'].sum():,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
)
# st.dataframe(df)

st.metric(
    label="🔝 Total de Xp ganhos.",
    value=f"{df['xp'].sum():,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
)
# st.dataframe(df)