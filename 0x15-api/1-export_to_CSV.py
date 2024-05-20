#!/usr/bin/python3
"""Returns information of an employee with a given ID,
and exports data to CSV"""

import csv
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

    # Open CSV file to write data
    with open('{}.csv'.format(employee_id), 'w') as csv_data:
        # Create CSV writer with specified delimiter and quoting style
        csv_writer = csv.writer(
            csv_data,
            delimiter=",",
            quotechar='"',
            quoting=csv.QUOTE_ALL
        )

        # Iterate through tasks and write data to CSV file
        for task in json_repr:
            # Check if the task belongs to the specified employee
            if task.get('userId') == employee_id:
                # Write task information to CSV file
                csv_writer.writerow(
                    [
                        task.get('userId'),
                        name,
                        task.get('completed'),
                        task.get('title')
                    ]
                )
