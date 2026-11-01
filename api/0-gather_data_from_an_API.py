#!/usr/bin/python3
"""Gather employee TODO list progress from an API."""

import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    employee_url = (
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    )
    todos_url = (
        f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    )

    employee = requests.get(employee_url).json()
    todos = requests.get(todos_url).json()

    completed_tasks = [
        task for task in todos if task.get("completed")
    ]

    print(
        f"Employee {employee.get('name')} is done with tasks"
        f"({len(completed_tasks)}/{len(todos)}):"
    )

    for task in completed_tasks:
        print(f"\t {task.get('title')}")
