import csv
import requests
import sys

if len(sys.argv) < 2:
    print('Please provide the user ID as an argument.')
    sys.exit(1)

user_id = sys.argv[1]

# Make a request to the API to get the user's tasks
url = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
response = requests.get(url)

if response.status_code != 200:
    print(f'Error: Request failed with status code {response.status_code}')
    sys.exit(1)

tasks = response.json()

# Create a CSV file with the specified format
csv_file = f'{user_id}.csv'

with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['USER_ID', 'USERNAME', 'TASK_COMPLETED_STATUS', 'TASK_TITLE'])

    for task in tasks:
    
        writer.writerow([user_id, 'Antonette', str(task['completed']), task['title']])

print(f'Tasks have been exported to {csv_file}')
