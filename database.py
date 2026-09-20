import psycopg

def save_fishing_record(player, area, fish, rarity, value, xp, equipment):

    connection = psycopg.connect(
        host="localhost",
        dbname = "fishing_game",
        user = "postgres",
        password = "senha",
    )

    cursor = connection.cursor()

    cursor.execute(
        '''
        INSERT INTO fishing_records
        (player, area, fish, rarity, value, xp, equipment)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        ''',
        (player, area, fish, rarity, value, xp, equipment)
    )

    connection.commit()

#    print("Pescaria salva no PostgreSQL")

    cursor.close()
    connection.close()

#    print("\nConexão encerrada.")

