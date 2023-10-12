#!/usr/bin/python3
'''
A script to export data in JSON format.
'''

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python 2-export_to_JSON.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]

    try:
        employee_id = int(employee_id)
    except ValueError:
        print("Employee ID must be an integer.")
        sys.exit(1)

    url_user = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    url_todos = f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos"

    user_response = requests.get(url_user)
    todos_response = requests.get(url_todos)

    if user_response.status_code != 200 or todos_response.status_code != 200:
        print("User or tasks not found. Please check the employee ID.")
        sys.exit(1)

    user_data = user_response.json()
    todos_data = todos_response.json()

    user_id = str(user_data['id'])
    username = user_data['username']

    tasks = [{
        "task": todo["title"],
        "completed": todo["completed"],
        "username": username
    } for todo in todos_data]

    user_data = {
        user_id: tasks
    }

    output_file = f"{user_id}.json"

    with open(output_file, "w") as file:
        json.dump(user_data, file)

    print(f"Data exported to {output_file}")
    