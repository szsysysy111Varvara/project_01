import mysql.connector

def search_movies(connection, genre, year):
    try:
        cursor = connection.cursor()
        query = """
            SELECT title, genres, year
            FROM movies
            WHERE genres = %s AND year = %s
            LIMIT 10;
        """
        cursor.execute(query, (genre, year))
        results = cursor.fetchall()
        cursor.close()
        return results
    except mysql.connector.Error as e:
        print("Ошибка при выполнении запроса:", e)
        return []
