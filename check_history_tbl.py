import mysql.connector


history_db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Varvara00!",
    database="history_database"
)


history_cursor = history_db_connection.cursor()

try:
    history_cursor.execute("SELECT * FROM history_of_data")

    results = history_cursor.fetchall()

    if results:
        print("Найдены следующие записи в таблице истории:")
        for row in results:
            print(row)
    else:
        print("Нет записей в таблице истории.")

except mysql.connector.Error as e:
    print("Ошибка при выполнении запроса:", e)

finally:
    history_cursor.close()
    history_db_connection.close()
