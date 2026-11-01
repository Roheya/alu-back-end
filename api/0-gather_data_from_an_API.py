
#!/usr/bin/python3
"""Gather employee TODO list progress from an API."""

import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    employee = user_response.json()

    todos_url = (
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    )
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    employee_name = employee["name"]

    completed_tasks = [task for task in todos if task["completed"]]

    print(
        f"Employee {employee_name} is done with tasks"
        f"({len(completed_tasks)}/{len(todos)}):"
    )

    for task in completed_tasks:
        print(f"\t {task['title']}")

