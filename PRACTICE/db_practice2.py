import sqlite3

conn = sqlite3.connect('practice.db')
cursor = conn.cursor()

sql_command = """
INSERT INTO weather_data (temperature, humidity, timestamp)
VALUES (23.5, 60, '2025-08-02 12:00')
"""

cursor.execute(sql_command)

conn.commit()
conn.close()
print("Sucessfully added a row of data to the database!")

