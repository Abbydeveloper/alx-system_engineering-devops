#!/usr/bin/python3
"""Query the Reddit API and return a list containing the titles of all hot
articles for a given subreddit.
If not results are found, the function should return None"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """Define function recurse to get a list of hot titles recursively"""
    if subreddit:
        try:
            url = "https://api.reddit.com/r/{:s}/hot.json".format(subreddit)
            headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'}
            params = {'after': after, 'limit': 50}

            response = requests.get(url, params=params, headers=headers,
                                    allow_redirects=False)
            response.raise_for_status()
            response = response.json()
            if 'data' in response and response['data']['children']:
                posts = response['data']['children']
                for post in posts:
                    post = post['data']['title']
                    hot_list.append(post)

                after = response['data']['after']
                if after:
                    return recurse(subreddit, hot_list, after)
                else:
                    return hot_list
            else:
                return None
        except Exception:
            return None
    return None
