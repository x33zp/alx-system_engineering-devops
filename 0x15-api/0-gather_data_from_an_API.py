#!/usr/bin/python3
"""Uses a REST APIfor a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv


if __name__ == "__main__":
    id = int(argv[1])
    users_url = 'https://jsonplaceholder.typicode.com/users'
    todos_url = 'https://jsonplaceholder.typicode.com/todos'
    users = requests.get(users_url, params={'id': id}).json()
    todos = requests.get(todos_url, params={'userId': id}).json()

    completed = []
    for task in todos:
        if task.get('completed') is True:
            completed.append(task.get('title'))
    print('Employee {} is done with tasks({}/{}):'.format(users[0].get('name'),
                                                          len(completed),
                                                          len(todos)))
    [print("\t {}".format(title)) for title in completed]
