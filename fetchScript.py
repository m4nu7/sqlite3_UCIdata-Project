import sqlite3
mydb = sqlite3.connect("bag_of_words.db")
#limit_number = int(input("Enter the number of records you want to fetch : "))
cursor = mydb.cursor()
data = cursor.execute("SELECT * FROM words ;")
print(data.fetchall())
