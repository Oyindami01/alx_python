#!/usr/bin/python3
'''
A script to export data in the JSON format.
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

    api_request = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}")
    api_request1 = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}/todos")

    if api_request.status_code != 200 or api_request1.status_code != 200:
        print("User or tasks not found. Please check the employee ID.")
        sys.exit(1)

    pjson = api_request.json()
    pjson1 = api_request1.json()

    name_info = pjson['username']

    filename = f"{employee_id}.json"

    # Create the dictionary structure
    result = {
        str(employee_id): [{
            "task": item["title"],
            "completed": item["completed"],
            "username": name_info
        } for item in pjson1]
    }
    # Export data to a JSON file

    with open(filename, "w") as outfile:
        json.dump(result, outfile)

    print("Data exported to", filename)
