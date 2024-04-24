import mysql.connector

dbconfig = {'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
            'user': 'ich1',
            'password': 'password',
            'database': 'movies'}

def show_table_fields(table_name):
    connection = mysql.connector.connect(**dbconfig)
    cursor = connection.cursor()
    try:
        cursor.execute(f"DESCRIBE {table_name}")
        fields = cursor.fetchall()
        with open("data.txt", "wb") as file:
            file.write("Поля и их описания:\n".encode('utf-8'))
            for field in fields:
                line = f"Поле: {field[0]},\nОписание: {field[1]}\n\n"
                file.write(line.encode('utf-8'))
        print("Результат записан в файл data.txt")
    except mysql.connector.Error as e:
        print(f'Ошибка при получении полей таблицы: {e}')
    finally:
        cursor.close()
        connection.close()

show_table_fields("movies")


