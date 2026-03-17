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

CREATE TABLE Clients(
    client_id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE Projects(
    project_id SERIAL PRIMARY KEY,
    client_id INT REFERENCES Clients(client_id)
);

CREATE TABLE Tasks(
    task_id SERIAL PRIMARY KEY,
    project_id INT REFERENCES Projects(project_id)
);
'''

query1 = '''
SELECT 
    c.name,
    p.project_id,
    t.task_id
FROM Clients c
JOIN Projects p ON c.client_id = p.client_id
JOIN Tasks t ON p.project_id = t.project_id;
'''
query_insert = '''
INSERT INTO Clients (name) VALUES
('Google'),
('Tesla');

INSERT INTO Projects (client_id) VALUES
(1),
(1),
(2);

INSERT INTO Tasks (project_id) VALUES
(1),
(1),
(2),
(3);
'''
cursor.execute(query)
conn.commit()
cursor.execute(query_insert)
conn.commit()
cursor.execute(query1)
rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
conn.close()