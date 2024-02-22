#!/usr/bin/python3
"""
Gets data from API
"""
import json
import requests
import sys

if __name__ == "__main__":
    emp_id = sys.argv[1]

    url = "https://jsonplaceholder.typicode.com/users/{}".format(emp_id)
    response = requests.get(url)
    emp = response.json()

    params = {"userId": emp_id}
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url, params)
    tasks = response.json()

    li = []
    for task in tasks:
        li.append({
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": emp.get("username")})

    di = {str(emp.get("id")): li}

    with open("{}.json".format(emp_id), mode="w") as file:
        json.dump(di, file)
