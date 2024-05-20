#!/usr/bin/python3
"""Export data in the JSON format."""

import json
import requests
import sys

if __name__ == "__main__":
    user_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user data
    user_response = requests.get(f"{base_url}/users/{user_id}")
    user_data = user_response.json()
    username = user_data.get("username")

    # Fetch tasks data for the user
    tasks_response = requests.get(f"{base_url}/todos?userId={user_id}")
    tasks_data = tasks_response.json()

    # Create dictionary to hold tasks
    tasks_dict = {user_id: []}

    # Populate tasks dictionary
    for task in tasks_data:
        task_dict = {
            "username": username,
            "task": task.get("title"),
            "completed": task.get("completed")
        }
        tasks_dict[user_id].append(task_dict)

    # Export to JSON file
    with open(f"{user_id}.json", "w") as json_file:
        json.dump(tasks_dict, json_file)
