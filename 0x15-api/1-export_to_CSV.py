#!/usr/bin/python3
"""Uses a REST APIfor a given employee ID,
saves information about his/her TODO list progress
to CSV file.
"""

import requests
from sys import argv
import csv


if __name__ == "__main__":
    id = int(argv[1])
    users_url = 'https://jsonplaceholder.typicode.com/users'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    users = requests.get(users_url, params={'id': id}).json()
    todos = requests.get(todos_url, params={'userId': id}).json()

    username = users[0].get('username')

    with open('{}.csv'.format(str(id)), 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for task in todos:
            writer.writerow(["{}".format(id), "{}".format(username),
                             "{}".format(task.get("completed")),
                             "{}".format(task.get("title"))])
    file.close()
