import json
import requests
import sys

def user_info(user_id):
    # Make a request to the API to get the user's tasks
    url = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
    response = requests.get(url)

    if response.status_code != 200:
        print(f'Error: Request failed with status code {response.status_code}')
        sys.exit(1)

    tasks = response.json()

    # Create a JSON file with the specified format
    json_file = f'{user_id}.json'

    data = {str(user_id): []}
    for task in tasks:
        
        data[str(user_id)].append({
            "task": task['title'],
            "completed": task['completed'],
            "username": "Antonette"  
        })

    with open(json_file, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=2)

    print(f'Tasks have been exported to {json_file}')

if len(sys.argv) < 2:
    print('Please provide the user ID as an argument.')
    sys.exit(1)

user_id = int(sys.argv[1])
user_info(user_id)
