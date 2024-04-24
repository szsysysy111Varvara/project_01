import mysql.connector

def popular_commands(connection):
    try:
        cursor = connection.cursor()
        query = """
            SELECT commands_text, COUNT(*)
            FROM history_of_data
            GROUP BY commands_text
            ORDER BY COUNT(*) DESC;
        """
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        return results
    except mysql.connector.Error as e:
        print("Ошибка при выполнении запроса:", e)
        return []
