import mysql.connector

class Database:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            print("Подключение к базе данных успешно.")
        except mysql.connector.Error as e:
            print("Ошибка при подключении к базе данных:", e)

    def disconnect(self):
        if self.connection:
            self.connection.close()
            print("Отключение от базы данных.")

    def create_history_table(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS history_of_data (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    commands_text TEXT,
                    commands_datetime DATETIME
                );
            """)
            print("Таблица истории запросов создана успешно.")
            cursor.close()
        except mysql.connector.Error as e:
            print("Ошибка при создании таблицы истории запросов:", e)

    def comm_history(self, command):
        try:
            cursor = self.connection.cursor()
            query = """
                INSERT INTO history_of_data (commands_text, commands_datetime)
                VALUES (%s, NOW());
            """
            cursor.execute(query, (command,))
            self.connection.commit()
            cursor.close()
            print("Запись в историю запросов выполнена успешно.")
        except mysql.connector.Error as e:
            print("Ошибка при записи в историю запросов:", e)





