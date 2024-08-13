#!/usr/bin/python3
"""Query the reddit API and print the titles of the first 10 hot posts list"""
import requests


def top_ten(subreddit):
    """Get top ten host posts"""

    if subreddit:
        try:
            url = "https://api.reddit.com/r/{:s}/hot.json".format(subreddit)
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; \
                Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/111.0.0.0 Safari/537.36"
                      }
            params = {'after': None, "limit": 10}

            response = requests.get(url, headers=headers, params=params,
                                    allow_redirects=False)
            response.raise_for_status()
            response = response.json()
            if 'data' in response and response['data']['children']:
                posts = response.json()['data']['children']

                for post in posts:
                    print(post['data']['title'])

            else:
                print(None)
        except Exception:
            print(None)
    else:
        print(None)
