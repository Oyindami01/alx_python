#!/usr/bin/python3
'''
A script to export data in the JSON format.
'''

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 export_to_JSON.py <USER_ID>")
        sys.exit(1)

    employee_id = sys.argv[1]

    try:
        api_request = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
        api_request1 = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}")

        if api_request.status_code == 200 and api_request1.status_code == 200:
            pjson = api_request.json()
            pjson1 = api_request1.json()

            filename = f"{employee_id}.json"
            
            # Create the dictionary structure
            result = {
                employee_id: [{
                    "task": item["title"],
                    "completed": item["completed"],
                    "username": pjson["username"]
                } for item in pjson1]
            }
            
            # Export data to a JSON file
            with open(filename, "w") as outfile:
                json.dump(result, outfile)
            print(f"Data exported to {filename}")
        else:
            print(f"User with ID {employee_id} not found.")
            sys.exit(1)

    except Exception as e:
        print(f"An error occurred: {str(e)}")
