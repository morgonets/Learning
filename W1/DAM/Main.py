from dotenv import load_dotenv
import psycopg2
import os

load_dotenv()
PASSWORD = os.getenv("POSTGRE_SQL_PASSWORD")

conn = psycopg2.connect(
    host="localhost",
    database="test3",
    user="postgres",
    password=PASSWORD
)

cursor = conn.cursor()

query = '''
DROP SCHEMA public CASCADE;
CREATE SCHEMA public;

CREATE TABLE clients (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT
);
CREATE TABLE projects (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    client_id INTEGER REFERENCES clients(id)
);
CREATE TABLE employees (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    role TEXT,
    project_id INTEGER REFERENCES projects(id)
);
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL,
    status TEXT,
    project_id INTEGER REFERENCES projects(id)
);
'''
query_insert = '''
INSERT INTO clients (name) VALUES ('Google'), ('Amazon');

INSERT INTO projects (name, client_id)
VALUES ('Website Redesign', 1),
       ('Mobile App', 1),
       ('Cloud System', 2);

INSERT INTO employees (name, role, project_id)
VALUES ('Alice', 'Manager', 1),
       ('Bob', 'Developer', 1),
       ('Charlie', 'Manager', 2);

INSERT INTO tasks (title, status, project_id)
VALUES ('Design UI', 'Done', 1),
       ('Build API', 'In Progress', 1);
'''
query_work = '''
SELECT 
    c.name AS client_name,
    p.name AS project_name,
    e.name AS manager_name
FROM projects p
JOIN clients c ON p.client_id = c.id
JOIN employees e ON e.project_id = p.id
WHERE e.role = 'Manager'
AND c.name = 'Google';
'''
cursor.execute(query)
conn.commit()

cursor.execute(query_insert)
conn.commit()

cursor.execute(query_work)

results = cursor.fetchall()

print("Projects for Google:")
for row in results:
    print(f"Client: {row[0]}, Project: {row[1]}, Manager: {row[2]}")

cursor.close()
conn.close()