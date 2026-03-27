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


query_create = '''
CREATE TABLE IF NOT EXISTS Products (
    id SERIAL PRIMARY KEY,
    name TEXT,
    cost_price NUMERIC,
    selling_price NUMERIC,
    stock INTEGER
);

CREATE TABLE IF NOT EXISTS Sales (
    id SERIAL PRIMARY KEY,
    product_id INTEGER REFERENCES Products(id),
    quantity INTEGER,
    sale_date DATE
);
'''

query_top3 = '''
SELECT p.name,
       SUM(s.quantity * (p.selling_price - p.cost_price)) AS profit
FROM Products p
JOIN Sales s ON p.id = s.product_id
GROUP BY p.id, p.name
ORDER BY profit DESC
LIMIT 3;
'''

query_revenue = '''
SELECT SUM(s.quantity * p.selling_price)
FROM Sales s
JOIN Products p ON p.id = s.product_id
WHERE s.sale_date >= CURRENT_DATE - INTERVAL '7 days';
'''


query_low_stock = '''
SELECT name, stock
FROM Products
WHERE stock < 5;
'''

query_insert_products = '''
INSERT INTO Products (name, cost_price, selling_price, stock) VALUES
('Laptop', 800, 1200, 10),
('Phone', 300, 600, 3),
('Tablet', 200, 400, 8),
('Headphones', 50, 150, 2),
('Monitor', 150, 300, 6);
'''

query_insert_sales = '''
INSERT INTO Sales (product_id, quantity, sale_date) VALUES
(1, 2, CURRENT_DATE - INTERVAL '2 days'),
(2, 3, CURRENT_DATE - INTERVAL '1 day'),
(3, 1, CURRENT_DATE - INTERVAL '6 days'),
(1, 1, CURRENT_DATE - INTERVAL '8 days'), -- won't count in last week
(4, 5, CURRENT_DATE - INTERVAL '3 days'),
(5, 2, CURRENT_DATE - INTERVAL '4 days');
'''

cursor.execute(query_create)
conn.commit()

cursor.execute(query_insert_products)
cursor.execute(query_insert_sales)
conn.commit()

print("\nTop 3 products:")
cursor.execute(query_top3)
for row in cursor.fetchall():
    print(row)

print("\nRevenue last 7 days:")
cursor.execute(query_revenue)
print(cursor.fetchone()[0])

print("\nLow stock products:")
cursor.execute(query_low_stock)
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()