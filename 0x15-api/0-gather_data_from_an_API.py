#!/usr/bin/python3
"""Returns information about employee TODO list progress"""

import requests
from sys import argv

if __name__ == '__main__':

    BASE_URL = 'https://jsonplaceholder.typicode.com'
    user = requests.get('{}/users/{}'.format(BASE_URL, argv[1])).json()
    todos = requests.get(
        '{}/todos'.format(BASE_URL),
        params={
            "userId": argv[1]}).json()

    total_tasks = len(todos)
    completed = 0
    completed_tasks = []
    for todo in todos:
        if todo["completed"]:
            completed += 1
            completed_tasks.append(todo.get("title"))

    output = 'Employee {} is done with tasks ({}/{}):'.format(user.get("name"),
                                                              completed,
                                                              total_tasks)
    print(output)
    [print('\t {}'.format(task)) for task in completed_tasks]
