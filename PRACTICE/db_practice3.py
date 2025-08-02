import sqlite3

conn = sqlite3.connect('practice.db')
cursor = conn.cursor()

sql_command = """
SELECT * FROM weather_data;"""
# Select -> you want to retrieve data
# * -> means 'all columns'
# FROM weather_data -> Which table to read from
# SQLite looks inside its stored data and matches rows
cursor.execute(sql_command)
# ^The cursor only sends the command, it does not immediatly return results

rows = cursor.fetchall()
# This tells SQLite:
# "Give me all rows from the result set as a list of tuples"
# Alternatively:
# - fetchone() -> gives just the first row
# - fetchmany(5) -> gives the first 5 rows


for i in rows:
    print(i)

conn.commit()
conn.close()
print("Sucessfully ran to the end of the script!")