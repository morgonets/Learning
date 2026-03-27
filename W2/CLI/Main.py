from dotenv import load_dotenv
import psycopg2
import os

load_dotenv()
PASSWORD = os.getenv("POSTGRE_SQL_PASSWORD")#personal

conn = psycopg2.connect(
    host="localhost",#personal
    database="test3",#personal
    user="postgres",#personal
    password=PASSWORD#personal
)

cursor = conn.cursor()

query = '''
CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    status TEXT NOT NULL
);

'''
cursor.execute(query) 
conn.commit()
def add_task(conn):
    name = input("Text name of task:")
    status = input("What status is it:")

    cur = conn.cursor()
    cur.execute(
        "INSERT INTO tasks (name, status) VALUES (%s, %s)",
        (name, status)
    )
    conn.commit()
    cur.close()

    print("Task added!")
def show_unfinished_tasks(conn):
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM tasks WHERE status != %s",
        ("done",)
    )

    tasks = cur.fetchall()

    if not tasks:
        print("No unfinished tasks.")
    else:
        for task in tasks:
            print(task)
while True:
    print("\n1. Add task")
    print("2. Show unfinished tasks")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        add_task(conn)

    elif choice == "2":
        show_unfinished_tasks(conn)

    elif choice == "3":
        break

    else:
        print("Invalid option")

cursor.close()
conn.close()