#!/usr/bin/python3
"""
Gets data from API
"""
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
    params = {"userId": emp_id, "completed": "true"}
    response = requests.get(url, params)
    tasks_completed = response.json()
    print("Employee {} is done with tasks({}/{}):"
          .format(emp.get("name"), len(tasks_completed), len(tasks)))

    for task in tasks_completed:
        print("\t {}".format(task.get("title")))
