from asyncio import tasks
import random


class Employee:
    def __init__(self, name, role, salary):
        self.name = name
        self.role = role
        self.salary = salary
        self.tasks_completed = 0   
    def add_task(self):
        self.tasks_completed += 1

    def calculate_bonus(self):
        if self.tasks_completed > 5:
            return self.salary * 0.1
        return 0
    


employees = [
    Employee("John", "Manager", 5000),
    Employee("Anna", "Developer", 4000),
    Employee("Mike", "Designer", 3500)
]
for employee in employees:
    tasks = random.randint(0, 10)
    
    for _ in range(tasks):
        employee.add_task()

    bonus = employee.calculate_bonus()

    print(f"Name: {employee.name}")
    print(f"Role: {employee.role}")
    print(f"Tasks completed: {employee.tasks_completed}")
    print(f"Bonus: {bonus}")
    print("-" * 30)