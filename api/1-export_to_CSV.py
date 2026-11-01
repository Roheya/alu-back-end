
#!/usr/bin/python3

import csv
import requests
import sys


if __name__ == "__main__":

    employee_id = int(sys.argv[1])

    # Get employee information
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    user_response = requests.get(user_url)
    employee = user_response.json()

    username = employee["username"]

    # Get all employee tasks
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Create CSV file
    filename = f"{employee_id}.csv"

    with open(filename, mode="w", newline="", encoding="utf-8") as csv_file:

        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)

        # Write all employee tasks
        for task in todos:
            writer.writerow([
                employee_id,
                username,
                task["completed"],
                task["title"]
            ])

