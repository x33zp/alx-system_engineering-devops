#!/usr/bin/python3
"""Uses a REST APIfor a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
from sys import argv


if __name__ == "__main__":
    id = argv[1]
    url = 'https://jsonplaceholder.typicode.com'
    user = requests.get(url + '/users/{}'.format(id)).json()
    todos = requests.get(url + '/todos', params={'userId': id}).json()

    completed = []
    for task in todos:
        if task.get('completed') is True:
            completed.append(task.get('title'))
    print('Employee {} is done with tasks({}/{}):'.format(user.get('name'),
                                                         len(completed),
                                                         len(todos)))
    [print("\t {}".format(title)) for title in completed]
