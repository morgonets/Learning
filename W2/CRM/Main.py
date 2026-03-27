import Filters
import Templates

clients = [
    {"name": "Alice", "amount": 120, "date": "2024-01-10"},
    {"name": "Bob", "amount": 40, "date": "2024-02-05"},
    {"name": "Charlie", "amount": 200, "date": "2024-03-01"}
]
filtered_clients = Filters.filtering_by_amount(clients, min_amount=100)
for client in filtered_clients:
    message = Templates.message(client["name"], client["amount"])
    print(message)
filtered_clients1 = Filters.filtering_by_date(clients, start_date="2024-02-01")
for client in filtered_clients1:
    message1 = Templates.reminder_message(client["name"])
    print(message1)# This code defines a list of clients with their names, amounts, and dates.
# Bim 
# ? Bam
# * Bom
# ! Bym
# TODO Homework