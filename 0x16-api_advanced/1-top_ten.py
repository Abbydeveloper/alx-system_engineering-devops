#!/usr/bin/python3
"""Query the reddit API and print the titles of the first 10 hot posts list"""
import requests


def top_ten(subreddit):
    """Get top ten host posts"""

    if subreddit:
        try:
            limit = 10
            url = "https://api.reddit.com/r/{:s}/hot.json".format(subreddit)
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; \
                Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
                Chrome/111.0.0.0 Safari/537.36"
                      }
            params = {'after': None, "limit": limit}

            response = requests.get(url, headers=headers, params=params,
                                    allow_redirects=False)
            response.raise_for_status()
            response = response.json()

            if 'data' in response and response['data']['children']:
                posts = response['data']['children']

                count = limit
                for post in posts:
                    count = count - 1
                    print(post['data']['title'], end="")
                    if count > 0:
                        print("")

            else:
                print(None)
        except Exception:
            print(None)
    else:
        print(None)
