#!/usr/bin/python3
"""Query the reddit API and print the titles of the first 10 hot posts list"""
import requests


def top_ten(subreddit):
    """Get top ten host posts"""

    try:
        limit = 10
        url = "https://api.reddit.com/r/{:s}/hot.json".format(subreddit)
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; \
            Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/111.0.0.0 Safari/537.36"
                      }
        params = {'after': "", "limit": limit}

        response = requests.get(url, headers=headers, params=params,
                                allow_redirects=False)
        
        if response.status_code != 200:
            print(None)
            return
        response = response.json()
        print(response.json())
        if 'data' in response and response['data']['children']:
            posts = response['data']['children']

            count = limit
            for post in posts:
                count = count - 1
                print(post['data']['title'], end="")
                if count > 0:
                    print("")

        else:
            print(None, end="")
    except requests.exceptions.RequestException:
        print(None)
        return
