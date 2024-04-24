import mysql.connector
from db import Database
from users_keyword import search_by_director

def search_keyword_director():
    try:
        movies_db_config = {
            'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
            'user': 'ich1',
            'password': 'password',
            'database': 'movies'
        }
        movies_connection = mysql.connector.connect(**movies_db_config)

        history_db_config = {
            'host': 'localhost',
            'user': 'root',
            'password': 'Varvara00!',
            'database': 'history_database'
        }

        history_connection = mysql.connector.connect(**history_db_config)

        db = Database(**movies_db_config)
        db.connect()

        while True:
            keyword = input("Введите имя и фамилию режессера( [\" \"] ): ")

            movies = search_by_director(movies_connection, keyword)

            if movies:
                print("Фильмы режессера:")
                for title, year, genres in movies:
                    print(f"Название: {title}, Год: {year}, Жанр: {genres}")
            else:
                print("Фильмы режессера не найдены.")

            command = f"INSERT INTO history_of_data (commands_text, commands_datetime) VALUES (%s, NOW());"
            history_cursor = history_connection.cursor()
            history_cursor.execute(command, (keyword,))
            history_connection.commit()
            history_cursor.close()

            choice = input("Хотите ещё раз выполнить поиск? (Y/N): ").lower()
            if choice not in ('y', 'yes'):
                break

    except mysql.connector.Error as e:
        print("Произошла ошибка при подключении к базе данных:", e)

    finally:
        if movies_connection:
            movies_connection.close()
        if history_connection:
            history_connection.close()

        if db.disconnect:
            db.disconnect()

    print("Конец работы программы!")

search_keyword_director()



