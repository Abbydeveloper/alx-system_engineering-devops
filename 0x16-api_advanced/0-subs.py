#!/usr/bin/python3
"""Query the Reddit API and return the number of total subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Get number of subscribers"""

    url = "https://www.reddit.com/r/{:s}/about.json".format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0"}
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            return data['data']["subscribers"]

        return 0
    except (ValueError, KeyError):
        return 0
