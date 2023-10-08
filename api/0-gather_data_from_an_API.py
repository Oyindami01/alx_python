import json
import requests
import sys

if __name__ == "__main__":
    emplooye_id = sys.argv[1]
    api_request = requests.get("https://jsonplaceholder.typicode.com/users/{}".format(emplooye_id))
    api_request1 = requests.get("https://jsonplaceholder.typicode.com/users/{}/todos".format(emplooye_id))
    data = api_request.text
    pjson = json.loads(data)
    data1 = api_request1.text
    pjson1 = json.loads(data1)

    title_count = 0
    title_complete = 0
    name_info = pjson['name']

# count the todo list and completed or not

    for itemss in pjson1:
        if 'title' in itemss:
            title_count += 1 
        if (itemss['completed'] == True):
            title_complete += 1

    print("Employee {} is done with tasks({}/{}):".format(name_info, title_complete, title_count))

# print all completed titles 

    for items in pjson1:
        if (items['completed'] == True):
            tasks_name = items['title']
            print("\t {}".format(tasks_name))