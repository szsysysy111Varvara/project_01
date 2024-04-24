import mysql.connector
from db import Database
from popular_commands import popular_commands

def search_popular_commands():
    try:
        history_db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'Varvara00!',
            'database': 'history_database'
        }

        history_connection = mysql.connector.connect(**history_db_config)
        db = Database(**history_db_config)
        db.connect()

        popular_queries = popular_commands(history_connection)
        print("Самые популярные запросы:")
        for query, count in popular_queries:
            print(f"Запрос: {query}, Количество: {count}")

    except mysql.connector.Error as e:
        print("Произошла ошибка при подключении к базе данных:", e)

    finally:
        if history_connection:
            history_connection.close()

    print("Конец работы программы!")


search_popular_commands()

