
#!/usr/bin/python3

import requests
import sys


if __name__ == "__main__":

    employee_id = int(sys.argv[1])

    # Get employee information
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    employee = user_response.json()

    # Get employee TODO list
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Count completed tasks
    completed_tasks = [task for task in todos if task["completed"]]
    number_of_done_tasks = len(completed_tasks)
    total_tasks = len(todos)

    # Display employee progress
    print(
        f"Employee {employee['name']} is done with tasks"
        f"({number_of_done_tasks}/{total_tasks}):"
    )

    # Display completed task titles
    for task in completed_tasks:
        print(f"\t {task['title']}")
