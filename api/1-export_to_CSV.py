#!/usr/bin/python3
"""Using what you did in the task #0, extend your Python
script to export data in the CSV format."""
import requests
from sys import argv
if __name__ == "__main__":
    employee_id = argv[1]
    req_employee = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id))
    req_employee = req_employee.json()
    username = req_employee["username"]
    req_todo = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(
            employee_id))
    req_todo = req_todo.json()
    filename = "{}.csv".format(employee_id)
    with open(filename, "w") as f:
        for i in req_todo:
            f.write(
                '"{}","{}","{}","{}"\n'.format(
                    employee_id,
                    username,
                    i["completed"],
                    i["title"]))
