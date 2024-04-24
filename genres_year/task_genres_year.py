import mysql.connector
from db import Database
from search_movies_genres_year import search_movies

def is_valid_genre(genre):
    return not any(char.isdigit() for char in genre)

def is_valid_year(year):
    return year.isdigit()

def genres_year():
    try:
        history_db_connection = mysql.connector.connect(
            host='localhost',
            user='root',
            password='Varvara00!',
            database='history_database'
        )

        history_cursor = history_db_connection.cursor()

        dbconfig = {
            'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
            'user': 'ich1',
            'password': 'password',
            'database': 'movies'
        }

        db = Database(**dbconfig)
        db.connect()
        db.create_history_table()

        while True:
            genre = input("Введите жанр фильма: ")
            if not is_valid_genre(genre):
                print("Ошибка: Жанр должен быть текстом.")
                continue

            year = input("Введите год выпуска фильма: ")
            if not is_valid_year(year):
                print("Ошибка: Год выпуска должен быть числом.")
                continue

            if db.connection:
                movies = search_movies(db.connection, genre, year)
                if movies:
                    print("Результаты по жанру и году:")
                    for title, genre, year in movies:
                        print(f"Название фильма: {title}, Жанр: {genre}, Год выпуска: {year}")
                else:
                    print("Нет данных для введенных параметров.")

                command = "INSERT INTO history_of_data (commands_text, commands_datetime) VALUES (%s, NOW())"
                history_cursor.execute(command, (f"{genre}, {year}",))
                history_db_connection.commit()
            else:
                print("Ошибка: Соединение с базой данных movies не установлено.")

            choice = input("Хотите ли вы получить еще 10 фильмов? (Y/N): ").lower()
            if choice not in ('y', 'yes'):
                break

    except Exception as e:
        print("Произошла ошибка:", e)

    finally:
        if history_cursor:
            history_cursor.close()
        if history_db_connection:
            history_db_connection.close()

        if db:
            db.disconnect()

    print("Конец работы программы!")

genres_year()






