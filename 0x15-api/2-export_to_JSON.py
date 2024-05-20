#!/usr/bin/python3
"""Returns information of an employee with a given ID,
and exports data to JSON"""

import json
import requests
from sys import argv

if __name__ == '__main__':
    # Get the employee ID from command line arguments
    employee_id = int(argv[1])

    # Fetch TODO list data from the API
    resp = requests.get('https://jsonplaceholder.typicode.com/todos/')
    json_repr = resp.json()

    # Fetch employee name from the API using employee ID
    resp = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(employee_id)
    )
    name = resp.json().get('username')

    # Create a dictionary to store tasks
    tasks_dict = {}

    # Iterate through tasks and add relevant information to tasks_dict
    for task in json_repr:
        if task.get('userId') == employee_id:
            if str(employee_id) not in tasks_dict:
                tasks_dict[str(employee_id)] = []
            tasks_dict[str(employee_id)].append({
                'task': task.get('title'),
                'completed': task.get('completed'),
                'username': name
            })

    # Write tasks_dict to a JSON file
    with open('{}.json'.format(employee_id), 'w') as json_file:
        json.dump(tasks_dict, json_file)
