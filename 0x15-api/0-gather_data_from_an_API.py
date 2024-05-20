#!/usr/bin/python3
"""returns information about the employee's TODO list progress using REST API"""
import requests
import sys

def get_employee_todo_progress(employee_id):
    # URL of the API
    url = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    # Sending a GET request to the API
    response = requests.get(url)

    # Checking if the request was successful
    if response.status_code != 200:
        print("Failed to retrieve data from the API.")
        return

    # Extracting JSON data from the response
    todos = response.json()

    # Counting completed and total tasks
    total_tasks = len(todos)
    completed_tasks = sum(1 for todo in todos if todo['completed'])

    # Getting employee name
    employee_name = todos[0]['username'] if todos else "Unknown"

    # Displaying progress
    print(f"Employee {employee_name} is done with tasks ({completed_tasks}/{total_tasks}):")
    
    # Displaying completed tasks
    for todo in todos:
        if todo['completed']:
            print(f"\t{todo['title']}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py EMPLOYEE_ID")
        sys.exit(1)

    employee_id = sys.argv[1]

    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    get_employee_todo_progress(employee_id)

