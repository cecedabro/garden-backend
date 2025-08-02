import sqlite3

# Connects (or creates) the database
# The variable 'conn' is the active connection that we 
# Use to send commands to the database
conn = sqlite3.connect('practice.db')

# Creates a cursor tool to run SQL commands
# (Think of the cursor as a pen to write or read data in the database)
cursor = conn.cursor()

# Define an SQL command to create a table
# We specify the structure of our data
sql_command = """
CREATE TABLE IF NOT EXISTS weather_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    temperature REAL,
    humidity REAL,
    timestamp TEXT
)
"""

# ** PRACICING SQL NOTES **
# SQL formatting logic in a nutshell:
# 
# CREATE TABLE table_name (
#   column_name data_type constraints,
#   column_name data_type constraints,
#   ...
#)

# Execute the SQL command
cursor.execute(sql_command)


# Commits changes so it actually saces them to the database file
conn.commit()
# Closes the connection
conn.close()

print("Database and table created (or already existed)")