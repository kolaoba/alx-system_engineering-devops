#!/usr/bin/python3
"""Script uses REST API for a given employee to
return information about his/her TODO list progress"""

import requests
from sys import argv

BASE_URL = 'https://jsonplaceholder.typicode.com'


if __name__ == '__main__':

    user = requests.get(f'{BASE_URL}/users/{argv[1]}').json()
    todos = requests.get(
        f'{BASE_URL}/todos',
        params={
            "userId": argv[1]}).json()

    total_tasks = len(todos)
    completed = 0
    completed_tasks = []
    for todo in todos:
        if todo["completed"]:
            completed += 1
            completed_tasks.append(todo["title"])

    output = f'Employee {user["name"]} is done with \
               tasks ({completed}/{total_tasks}):'
    print(output)
    for task in completed_tasks:
        print(f'\t {task}')
