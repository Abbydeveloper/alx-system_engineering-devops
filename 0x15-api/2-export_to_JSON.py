#!/usr/bin/python3
"""Export data to JSON"""
import json
import requests as req
import sys

if __name__ == "__main__":
    try:
        user_id = int(sys.argv[1])
        url = "https://jsonplaceholder.typicode.com"
        user_resp = req.get('{}/users/{}'.format(url, user_id)).json()
        user_name = user_resp.get('username')
        todo_resp = req.get('{}/todos'.format(url),
                            params={"userId": user_id}).json()

        with open('{}.json'.format(user_id), 'w') as jsonfile:
            json.dump({user_id: [{'task': todo.get('title'),
                                  'completed': todo.get('completed'),
                                  'username': user_name}
                                 for todo in todo_resp]},
                      jsonfile)

    except ValueError:
        pass
