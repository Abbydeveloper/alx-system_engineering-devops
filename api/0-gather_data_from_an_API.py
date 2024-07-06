#!/usr/bin/python3
""" Gather data from an API"""

import requests as req
import sys


if __name__ == '__main__':
    try:
        url = "https://jsonplaceholder.typicode.com"
        user_id = int(sys.argv[1])
        user_resp = req.get('{}/users/{}'.format(url, user_id)).json()
        todo_resp = req.get('{}/todos'.format(url),
                            params={'userId': user_id}).json()
        completed_tasks = [title.get('title') for title in todo_resp
                           if title.get('completed') is True]
        print('Employee {} is done with tasks({}/{}):'
              .format(user_resp.get('name'),
                      len(completed_tasks),
                      len(todo_resp)))
        for task in completed_tasks:
            print('\t ' + task)
    except ValueError:
        pass
