#!/usr/bin/python3
"""Script uses REST API for a given employee to
return information about his/her TODO list progress
and exports data to json
"""

import json
import requests
from sys import argv

if __name__ == '__main__':
    BASE_URL = 'https://jsonplaceholder.typicode.com'

    user = requests.get('{}/users/{}'.format(BASE_URL, argv[1])).json()
    todos = requests.get(
        '{}/todos'.format(BASE_URL),
        params={
            "userId": argv[1]}).json()

    with open('{}.json'.format(argv[1]), 'w', encoding='utf8') as f:
        tasks = []
        for todo in todos:
            tasks.append({"task": todo.get("title"),
                          "completed": todo.get("completed"),
                          "username": user.get("username")})
        data = {argv[1]: tasks}
        json.dump(data, f)
