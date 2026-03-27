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

cursor.execute("DROP TABLE IF EXISTS products;")

cursor.execute('''
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name TEXT NOT NULL,
    stock INT NOT NULL
);
''')

cursor.execute('''
INSERT INTO products (name, stock) VALUES
('Laptop', 10),
('Mouse', 50),
('Keyboard', 30),
('Monitor', 20),
('USB Cable', 5);
''')

query = '''
SELECT 
    name,
    stock,
    (SELECT AVG(stock) FROM products) - stock AS gap
FROM products
WHERE stock < (SELECT AVG(stock) FROM products);
'''

cursor.execute(query)
results = cursor.fetchall()

print("Products below average stock:\n")

for name, stock, gap in results:
    print(f"{name} | Stock: {stock} | Gap: {round(gap, 2)}")

conn.commit()

cursor.close()
conn.close()