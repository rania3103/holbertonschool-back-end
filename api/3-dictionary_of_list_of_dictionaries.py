#!/usr/bin/python3
"""Using what you did in the task #0,
extend your Python script to export data in the JSON format."""
import requests
from sys import argv
from json import dump
if __name__ == "__main__":
    req_employee = requests.get(
        "https://jsonplaceholder.typicode.com/users").json()
    req_todo = requests.get(
        "https://jsonplaceholder.typicode.com/todos").json()
    filename = "todo_all_employees.json"
    nested_dic = {}
    for employee in req_employee:
        l = []
        for task in req_todo:
            if task["userId"] == employee["id"]:
                dict = {"task": task["title"],
                        "completed": task["completed"],
                        "username": employee["username"]}
                l.append(dict)
        nested_dic[employee["id"]] = l
    with open(filename, "w") as f:
        dump(nested_dic, f)
