import sqlite3

# 1 链接
connection = sqlite3.connect('data.db')
cursor = connection.cursor()

# 2 Query all data
# cursor.execute("SELECT * FROM events WHERE date='2088.10.15'")
# rows = cursor.fetchall()
# print(rows) # [('Lions', 'Lion City', '2088.10.15'), ('Monkey', 'Monkey City', '2088.10.15')]

# 2-1 Query certain columns
# cursor.execute("SELECT band,date FROM events WHERE date='2088.10.15'")
# rows = cursor.fetchall()
# print(rows) # [('Lions', '2088.10.15'), ('Monkey', '2088.10.15')]

# Insert
# new_cows = [
#     ("PPX", "PPX City", "2088.10.29"),
#     ("KK", "KK City", "2088.06.06"),
# ]
# cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_cows)
# connection.commit()


 # Query all data
cursor.execute("SELECT * FROM events ")
rows = cursor.fetchall()
print(rows) # (...('PPX', 'PPX City', '2088.10.29'), ('KK', 'KK City', '2088.06.06'))