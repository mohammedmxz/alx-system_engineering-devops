#!/usr/bin/python3
"""
Gets data from API
"""
import csv
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

    ll = []
    for task in tasks:
        li = []
        li.append(emp.get("id"))
        li.append(emp.get("username"))
        li.append(task.get("completed"))
        li.append(task.get("title"))
        ll.append(li)

    with open("{}.csv".format(emp_id), mode="w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        writer.writerows(ll)
