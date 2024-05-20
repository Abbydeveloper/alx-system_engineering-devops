#!/usr/bin/python3
""" Export to CSV"""

import csv
import requests as req
import sys

if __name__ == "__main__":
    try:
        user_id = int(sys.argv[1])
        url = "https://jsonplaceholder.typicode.com"
        user_resp = req.get('{}/users/{}'.format(url, user_id)).json()
        todo_resp = req.get('{}/todos'.format(url),
                            params={'userId': user_id}).json()
        user_name = user_resp.get("username")

        with open('{}.csv'.format(user_id), 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
            [writer.writerow([user_id, user_name, elm.get('completed'),
                              elm.get('title')]) for elm in todo_resp]
    except ValueError:
        pass
