import requests
import csv
import sys

def export_to_csv(user_id):
    try:
        # Fetch user data
        user_url = 'https://jsonplaceholder.typicode.com/users/' + str(user_id)
        response = requests.get(user_url)
        user_data = response.json()

        # Fetch tasks for the user
        tasks_url = 'https://jsonplaceholder.typicode.com/todos?userId=' + str(user_id)
        response = requests.get(tasks_url)
        tasks = response.json()

        # Create a CSV file named USER_ID.csv
        csv_filename = str(user_id) + '.csv'

        # Open the CSV file for writing
        with open(csv_filename, mode='w', newline='') as csv_file:
            fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            
            # Write the CSV header
            writer.writeheader()

            # Write task data to the CSV file
            for task in tasks:
                writer.writerow({
                    "USER_ID": user_id,
                    "USERNAME": user_data['username'],
                    "TASK_COMPLETED_STATUS": str(task['completed']),
                    "TASK_TITLE": task['title']
                })

        print(f'Data exported to {csv_filename}')
    
    except requests.exceptions.RequestException as e:
        print("Error fetching data:", e)
    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <USER_ID>")
    else:
        user_id = int(sys.argv[1])
        export_to_csv(user_id)