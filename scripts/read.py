import mysql.connector
import os


DB_USER = os.getenv("MYSQL_USER")
DB_PASS = os.getenv("MYSQL_PASSWORD","6equj5_db_user" )
DB_NAME = os.getenv("MYSQL_DATABASE", "home_db")

conn = mysql.connector.connect(
    host="mysql_ctn",  # localhost or 127.0.0.1
    port=3306,  # 3306 if not remapped
    user="db_user",
    password=DB_PASS,
    database=DB_NAME
)

cursor = conn.cursor()

with open('schema.sql', 'r') as f:
    sql_commands = f.read()

for command in sql_commands.split(';'):
    cmd = command.strip()
    if cmd:
        try:
            cursor.execute(cmd)
        except mysql.connector.Error as err:
            print(f"⚠️ Error running command: {cmd}\n{err}")

conn.commit()
cursor.close()
conn.close()
