import mysql.connector

def search_by_director(connection, director):
    try:
        cursor = connection.cursor()
        query = """
            SELECT title, year, genres
            FROM movies 
            WHERE JSON_CONTAINS(directors, %s) 
            LIMIT 10;
        """
        cursor.execute(query, (director,))
        results = cursor.fetchall()
        cursor.close()
        return results
    except mysql.connector.Error as e:
        print("Ошибка при выполнении запроса:", e)
        return []




