#!/usr/bin/python3
import requests
"""Query the Reddit API and return the number of total subscribers"""


def number_of_subscribers(subreddit):
    """Get number of subscribers"""

    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    print(url)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0")
    try:
        response = requests.get(url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json().get('data')
            return data.get("subscribers")
        
        return (0)
    except (ValueError, TypeError):
        return (0)
