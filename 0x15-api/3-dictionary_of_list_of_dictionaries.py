#!/usr/bin/python3
"""
Gets data from API
"""
import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/"
    response = requests.get(url)
    emps = response.json()

    di = {}
    for emp in emps:
        params = {"userId": str(emp.get("id"))}
        url = "https://jsonplaceholder.typicode.com/todos"
        response = requests.get(url, params)
        tasks = response.json()

        li = []
        for task in tasks:
            li.append({
                "username": emp.get("username"),
                "task": task.get("title"),
                "completed": task.get("completed")})

        di[str(emp.get("id"))] = li

    with open("todo_all_employees.json", mode="w") as file:
        json.dump(di, file)
