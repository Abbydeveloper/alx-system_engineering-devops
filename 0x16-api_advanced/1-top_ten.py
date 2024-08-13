#!/usr/bin/python3
"""Query the reddit API and print the titles of the first 10 hot posts list"""
import requests


def top_ten(subreddit):
    """Get top ten host posts"""

    url = "https://www.reddit.com/r/{:s}/hot.json".format(subreddit)
    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
            }
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)

        if response.status_code == 200:
            data = response.json()['data']['children']

            for post in data:
                print(post['data']['title'])

        else:
            print(None)
    except (KeyError, ValueError):
        print(None)
