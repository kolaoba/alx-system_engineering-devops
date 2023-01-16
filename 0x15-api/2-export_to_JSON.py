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
            tasks.append({"task": '{}'.format(todo.get("title")),
                          "completed": '{}'.format(str(todo.get("completed"))),
                          "username": '{}'.format(user.get("username"))})
        data = {"{}".format(argv[1]): tasks}
        json_string = json.dumps(data)
        f.write(json_string.rstrip())
