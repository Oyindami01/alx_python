import json
import requests

def get_user_data(user_id):
    url = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'
    response = requests.get(url)

    if response.status_code != 200:
        print(f'Error: Request failed with status code {response.status_code}')
        return None

    tasks = response.json()
    return tasks

def export_all_employees():
    all_data = {}

    for user_id in range(1, 11):  # Assuming user IDs from 1 to 10
        user_data = get_user_data(user_id)
        
        if user_data:
            username = user_data[0]["username"]
            formatted_data = [{"username": username, "task": task["title"], "completed": task["completed"]} for task in user_data]
            all_data[str(user_id)] = formatted_data

    with open('todo_all_employees.json', 'w') as jsonfile:
        json.dump(all_data, jsonfile, indent=2)

    print('Data for all employees has been exported to todo_all_employees.json')

if __name__ == '__main__':
    export_all_employees()
