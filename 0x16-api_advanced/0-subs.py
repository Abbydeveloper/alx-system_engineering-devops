#!/usr/bin/python3
"""Query the Reddit API and return the number of total subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Get number of subscribers"""

    url = "https://www.reddit.com/r/{:s}/about.json".format(subreddit)
    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
        AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
            }
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            return data['data']["subscribers"]

        return 0
    except (ValueError, KeyError):
        return 0
