#!/usr/bin/python3
"""Script uses REST API for a given employee to
return information about his/her TODO list progress
and exports data to csv
"""

import requests
from sys import argv
import csv


BASE_URL = 'https://jsonplaceholder.typicode.com'

user = requests.get(f'{BASE_URL}/users/{argv[1]}').json()
todos = requests.get(f'{BASE_URL}/todos', params={"userId": argv[1]}).json()

with open(f'{argv[1]}.csv', 'w', encoding='utf8') as f:
    writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    for todo in todos:
        writer.writerow([f"{argv[1]}", f'{user["name"]}',
                         f'{str(todo["completed"])}',
                         f'{todo["title"]}'])
