import csv
import json
import requests
import sys

def export_tasks_to_csv(user_id):
    # Define the URL of the API
    url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

    try:
        # Send a GET request to the API
        response = requests.get(url)

        # Check if the request was successful
        if response.status_code == 200:
            tasks = response.json()

            # Define a dictionary to store tasks for all users
            all_user_tasks = {}

            # Loop through the tasks and organize them by user ID
            for task in tasks:
                user_id = task["userId"]
                username = "Replace with actual username"  # Replace with the actual username retrieval logic
                task_info = {
                    "username": username,
                    "task": task["title"],
                    "completed": task["completed"]
                }

                if user_id not in all_user_tasks:
                    all_user_tasks[user_id] = []

                all_user_tasks[user_id].append(task_info)

            # Define the JSON filename
            json_filename = "todo_all_employees.json"

            # Write the tasks to a JSON file
            with open(json_filename, 'w') as json_file:
                json.dump(all_user_tasks, json_file)

            print(f"Tasks exported to {json_filename}")
        else:
            print("Failed to retrieve tasks. API request failed.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <USER_ID>")
    else:
        user_id = int(sys.argv[1])
        export_tasks_to_csv(user_id)
