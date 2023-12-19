#!/usr/bin/python3
"""Write a Python script that, using this REST API,
for a given employee ID, returns information about
his/her TODO list progress."""
import requests
from sys import argv
employee_id = argv[1]
req_name = requests.get(
    "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)).json()
name = req_name["name"]
req_todo = requests.get(
    "https://jsonplaceholder.typicode.com/users/{}/todos".format(employee_id)).json()
completed_tasks = 0
for i in req_todo:
    if i["completed"]:
        completed_tasks += 1
print("Employee {} is done with tasks({}/{}):".format(name,
      completed_tasks, len(req_todo)))
for i in req_todo:
    print("  {}".format(i["title"]))
