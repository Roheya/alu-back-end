
#!/usr/bin/python3

import json
import requests

if __name__ == "__main__":
    # Get all employees
    users_url = "https://jsonplaceholder.typicode.com/users"
    users_response = requests.get(users_url)
    users = users_response.json()

    # Get all tasks
    todos_url = "https://jsonplaceholder.typicode.com/todos"
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Store tasks for every employee
    all_tasks = {}

    for user in users:
        employee_id = str(user["id"])
        username = user["username"]

        employee_tasks = []

        for task in todos:
            if task["userId"] == user["id"]:
                employee_tasks.append({
                    "username": username,
                    "task": task["title"],
                    "completed": task["completed"]
                })

        all_tasks[employee_id] = employee_tasks

    # Export all employee tasks to JSON
    with open("todo_all_employees.json", "w", encoding="utf-8") as json_file:
        json.dump(all_tasks, json_file)

