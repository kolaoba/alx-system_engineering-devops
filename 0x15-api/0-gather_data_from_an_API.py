#!/usr/bin/python3
"""Returns information about employee TODO list progress
"""

import requests
from sys import argv

if __name__ == '__main__':

    BASE_URL = 'https://jsonplaceholder.typicode.com'
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

    output = f'Employee {user["name"]} is done with\
 tasks ({completed}/{total_tasks}):'
    print(output)
    [print(f'\t {task}') for task in completed_tasks]
