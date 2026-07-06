import sqlite3

connection = sqlite3.connect("pharmacy.db")

cursor = connection.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS employees (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        department TEXT,
        salary REAL
    )
""")

new_employee = ("Alice Smith", "Engineering", 85000.00)
cursor.execute(
    "INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)", 
    new_employee
)

connection.commit()

cursor.execute("SELECT * FROM employees")
rows = cursor.fetchall()

for row in rows:
    print(f"ID: {row[0]} | Name: {row[1]} | Dept: {row[2]} | Salary: ${row[3]}")

connection.close()