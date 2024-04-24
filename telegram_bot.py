import mysql.connector
from telegram import Bot

history_db_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Varvara00!',
    database='history_database'
)

dbconfig = {
    'host': 'ich-db.ccegls0svc9m.eu-central-1.rds.amazonaws.com',
    'user': 'ich1',
    'password': 'password',
    'database': 'movies'
}


BOT_TOKKEN = '7074786769:AAEiy3KQFb3KLhwHIF9dXm9e0h06LTDfZrA'
CHAT_ID = '5365908056'
bot = telegram.Bot(token=BOT_TOKKEN)

