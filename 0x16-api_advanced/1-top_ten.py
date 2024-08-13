#!/usr/bin/python3
"""Query the reddit API and print the titles of the first 10 hot posts list"""


def top_ten(subreddit):
    """Get top ten host posts"""

    url = "https://wwworeddit.com/r/{:s}/hot/.json".format(subreddit)
    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
            }
    params = { "limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()
            return data
        return None
    except (KeyError, ValueError):
        return None
