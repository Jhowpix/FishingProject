import psycopg
import pandas as pd
import matplotlib.pyplot as plt

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
        "equipment"]
)

df["equipment"] = df["equipment"].str.replace("\xa0", " ", regex=False)
df["equipment"] = df["equipment"].replace(
    "Vara B sica",
    "Vara Básica"
)

print("\n=== DADOS DAS PESCARIAS ===")
print(df)

total_value = df["value"].sum()
print(f"Valor total dos peixes: ${total_value}")

print("\n=== PEIXES PESCADOS ===")
fish_count = df["fish"].value_counts()
print(fish_count)

fish_count.plot(kind="bar")

plt.title("Peixes Pescados")
plt.xlabel("Peixes")
plt.ylabel("Quantidades")

plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig("graphs/fish_count.png")
plt.show()

print("\n=== VALOR POR PEIXE ===")
fish_value = df.groupby("fish")["value"].sum()
print(fish_value)

fish_value.plot(kind="bar")

plt.title("Valor por Peixe")
plt.xlabel("Peixe")
plt.ylabel("Valor")

plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig("graphs/fish_value.png")
plt.show()

print("\n=== VALOR POR RARIDADE ===")
rarity_value = df.groupby("rarity")["value"].sum()
print(rarity_value)

rarity_value.plot(kind="bar")

plt.title("Valor por Raridade")
plt.xlabel("Raridade")
plt.ylabel("Valor")

plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig("graphs/rarity_value.png")
plt.show()

print("\n=== XP POR RARIDADE ===")
rarity_xp = df.groupby("rarity")["xp"].sum()
print(rarity_xp)

rarity_xp.plot(kind="bar")

plt.title("XP por Raridade")
plt.xlabel("Raridade")
plt.ylabel("XP")

plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig("graphs/rarity_xp.png")
plt.show()

area_count = df["area"].value_counts()
print(area_count)

player_count = df["player"].value_counts()
print(player_count)

print("\n=== PESCARIAS POR EQUIPAMENTO ===")
equipment_count = df["equipment"].value_counts()
print(equipment_count)

print("\n=== VALOR POR EQUIPAMENTO ===")
equipment_value = df.groupby("equipment")["value"].sum()
print(equipment_value)

print("\n=== VALOR MÉDIO POR EQUIPAMENTO ===")
equipment_average = df.groupby("equipment")["value"].mean().round(2)
print(equipment_average)

equipment_average.plot(kind="bar")

plt.title("Valor Médio por Equipamento")
plt.xlabel("Equipamento")
plt.ylabel("Valor Médio")

plt.xticks(rotation=30)
plt.tight_layout()

plt.savefig("graphs/equipment_average.png")
plt.show()

print(df["player"].unique())

#print(f"Quantidade de registros: {len(records)}")
print("Conexão com PostgreSQL realizada!")


