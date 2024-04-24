import mysql.connector

def get_all_from_movies():
    movies_db_config = {
        'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
        'user': 'ich1',
        'password': 'password',
        'database': 'movies'
    }

    try:
        connection = mysql.connector.connect(**movies_db_config)
        cursor = connection.cursor()
        query = """
            SELECT * FROM movies;
        """
        cursor.execute(query)
        results = cursor.fetchall()
        cursor.close()
        connection.close()
        return results
    except mysql.connector.Error as error:
        print("Ошбка с подклучением к MySQL", error)
        return None

get_all_from_movies()
