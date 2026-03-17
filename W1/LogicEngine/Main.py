import json
x = int(input("Enter the amount of min spent: "))
today_date = 0
with open("customers.json", "r", encoding="utf-8") as file:
    data = json.load(file)

customers = data["customers"]

for customer in customers:
    if customer["amount_spent"] > x and customer["days_since_last_order"] > (today_date + 30) and customer["subscription_status"]:
        print(customer["name"], customer["amount_spent"])