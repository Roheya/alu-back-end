
#!/usr/bin/python3

import json
import requests
import sys

if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    # Get employee information
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    employee = user_response.json()

    username = employee["username"]

    # Get all tasks belonging to the employee
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Prepare the data in the required JSON format
    employee_tasks = []

    for task in todos:
        employee_tasks.append({
            "task": task["title"],
            "completed": task["completed"],
            "username": username
        })

    # Use employee ID as the main JSON key
    data = {
        str(employee_id): employee_tasks
    }

    # Export data to a JSON file
    filename = f"{employee_id}.json"

    with open(filename, mode="w", encoding="utf-8") as json_file:
        json.dump(data, json_file)

