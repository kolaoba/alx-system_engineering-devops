#!/usr/bin/python3
"""Exports information about Employee TODO list progress
and exports data to csv
"""

import requests
from sys import argv
import csv


BASE_URL = 'https://jsonplaceholder.typicode.com'

user = requests.get('{}/users/{}'.format(BASE_URL, argv[1])).json()
todos = requests.get('{}/todos'.format(BASE_URL),
                     params={"userId": argv[1]}).json()

with open('{}.csv'.format(argv[1]), 'w', encoding='utf8') as f:
    writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    for todo in todos:
        writer.writerow(['{}'.format(argv[1]), '{}'.format(user.get("name")),
                         '{}'.format(str(todo.get("completed"))),
                         '{}'.format(todo.get("title"))])
