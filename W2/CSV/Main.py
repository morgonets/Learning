from dotenv import load_dotenv
import psycopg2
import os
import csv

load_dotenv()
PASSWORD = os.getenv("POSTGRE_SQL_PASSWORD")

conn = psycopg2.connect(
    host="localhost",
    database="test3",
    user="postgres",
    password=PASSWORD
)

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS clients (
    id SERIAL PRIMARY KEY,
    name TEXT,
    email TEXT,
    estimated_budget INTEGER
);
""")

skipped = 0
success = 0

with open("leads.csv", "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)

    for row in reader:

        name = row["name"]
        email = row["email"]
        budget = row["estimated_budget"]

        if email == "" or not budget.isdigit():
            print("Corrupted Data:", row)
            skipped += 1
            continue

        cursor.execute(
            "INSERT INTO clients (name, email, estimated_budget) VALUES (%s, %s, %s)",
            (name, email, int(budget))
        )

        success += 1

conn.commit()

print(f"Successfully migrated {success} leads to the database.")
print(f"{skipped} rows were skipped due to errors.")

cursor.close()
conn.close()