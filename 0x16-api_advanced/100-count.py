#!/usr/bin/python3
"""Query the Reddit API, parse the title of all hot articles and print a sorted count of given keywords"""
import requests


def count_words(subreddit, word_list, after=[], word_count):
    """Print a sorted count of given keywords"""

    url = "https://www.reddit.com/r/{:s}/hot.json".format(subreddit)
    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
    AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
            }
    params = {"after": after, "limit": 10}

    if not word_count:
        for word in word_list:
            word_count.word = 0
    if after is None:
        word_list = [[key, value] for key, value in word_count.items()]
        word_list = sorted(word_list, key=lambda x:(-x[1], x[0]))
        for word in word_list:
            if word[1]:
                print('{}:{}'.format(word[0].lower(), word[1]))
        return None


    response = requests. get(url, params, headers, allow_redirects=False)
    response = response.json()

    if 'data' in response and response['data']['children']:
        after = response['data']['after']
        posts = response['data']['children']
        for post in posts:
            title = post.get('title')
            lowercase = [s.lower() for s in title.split(' ')]
            for word in word_list:
                word_count[word] += lowercase.count(word.lower())
    else:
        return None

    count_words(subreddit, word_list, after, word_count)
