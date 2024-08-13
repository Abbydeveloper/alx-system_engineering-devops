#!/usr/bin/python3
import requests
"""Query the Reddit API and return the number of total subscribers"""


def number_of_subscribers(subreddit):
    """Get number of subscribers"""

    url = "https://www.reddit.com/r/" + subreddit + "/about.json"
    print(url)
    headers = {"User-Agent": "alx_se")
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data')
        return data.get("subscribers")
    else:
        return (0)
    return (0)
