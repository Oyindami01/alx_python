#!/usr/bin/python3
'''
A script to export data in the JSON format.
'''

import json
import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python 2-export_to_JSON.py <USER_ID>")
    sys.exit(1)

user_id = sys.argv[1]

# Define the URL for the user's tasks
url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

# Send a GET request to the API
response = requests.get(url)

# Check if the request was successful
if response.status_code != 200:
    print(f"Failed to retrieve data for USER_ID {user_id}")
    sys.exit(1)

# Parse the JSON response
tasks = response.json()

# Create a dictionary to store the tasks
task_dict = {user_id: []}

# Populate the dictionary with task information
for task in tasks:
    task_info = {
        "task": task["title"],
        "completed": task["completed"],
        "username": user["username"]  # Assuming you have the user's information
    }
    task_dict[user_id].append(task_info)

# Write the task dictionary to a JSON file
with open(f"{user_id}.json", "w") as json_file:
    json.dump(task_dict, json_file)

print(f"Data exported to {user_id}.json")