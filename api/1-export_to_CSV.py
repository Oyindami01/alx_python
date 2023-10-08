import csv
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

            # Define the CSV filename based on the USER_ID
            csv_filename = f"{user_id}.csv"

            # Write the tasks to a CSV file
            with open(csv_filename, mode='w', newline='') as csv_file:
                fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
                writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                writer.writeheader()

                for task in tasks:
                    writer.writerow({
                        "USER_ID": user_id,
                        "USERNAME": "Replace with actual username",  # Replace with the actual username retrieval logic
                        "TASK_COMPLETED_STATUS": str(task["completed"]),
                        "TASK_TITLE": task["title"]
                    })

            print(f"Tasks exported to {csv_filename}")
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
