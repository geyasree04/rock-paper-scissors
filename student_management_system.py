import sqlite3

conn = sqlite3.connect("students.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
""")

cursor.execute(
    "INSERT INTO students(name, age) VALUES (?, ?)",
    ("Rahul", 20)
)

conn.commit()

cursor.execute("SELECT * FROM students")

for row in cursor.fetchall():
    print(row)

conn.close()