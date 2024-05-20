#!/usr/bin/python3
"""Dictionary of list of dictionaries"""

import json
import requests as req
import sys

for __name__ == "__main__":
    try:
        url = "https://jsonplaceholder.typicode.com"
        users = req.get('{}/users'.format(url)).json()

        with open('todo_all_employees.json', 'w') as jsonfile:
            json.dump({user.get('id'): [{
                'username': user.get('username'),
                'task': todo.get('title'),
                'completed': todo.get('completed')}
                for todo in req.get('{}/todos', format(url)
                                    params={'userId': user.get('id')}).json()]
                                 for user in users}, jsonfile)

    except ValueError:
        pass
