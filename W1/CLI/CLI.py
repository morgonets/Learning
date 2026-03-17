import json
import os
from datetime import datetime

DATA_FILE = "data.json"


def load_data():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f, indent=4)


def add_task():
    task_name = input("Enter task name: ")
    duration = int(input("Enter duration in minutes: "))
    date = datetime.now().strftime("%Y-%m-%d")

    data = load_data()

    data.append({
        "task_name": task_name,
        "duration": duration,
        "date": date
    })

    save_data(data)
    print("Task saved.")


def generate_report():
    data = load_data()
    today = datetime.now().strftime("%Y-%m-%d")

    today_tasks = [task for task in data if task["date"] == today]

    if not today_tasks:
        print("No tasks for today.")
        return

    total_time = sum(task["duration"] for task in today_tasks)
    longest_task = max(today_tasks, key=lambda x: x["duration"])
    average_time = total_time / len(today_tasks)

    print("\n--- Daily Report ---")
    print(f"Date: {today}")
    print(f"Total time: {total_time} minutes")
    print(f"Longest task: {longest_task['task_name']} ({longest_task['duration']} min)")
    print(f"Average task duration: {average_time:.2f} minutes")


def main():
    print("1. Add task")
    print("2. Generate report")
    choice = input("Choose option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        generate_report()
    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()