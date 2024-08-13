#!/usr/bin/python3
"""Query the Reddit API and return the number of total subscribers"""
import requests


def number_of_subscribers(subreddit):
    """Get number of subscribers"""

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /CNwante)"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        try:
            data = response.json()
            return data['data']['subscribers']
        except (ValueError, KeyError):
            return 0
    else:
        return 0
