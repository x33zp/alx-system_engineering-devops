#!/usr/bin/python3
"""First 10 hot posts listed for a given subreddit"""

import requests


def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit"""
    url = 'https://api.reddit.com/r/{}/hot'.format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0"}
    params = {"limit": 10}

    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)
    result = res.json()

    try:
        hot = result.get('data')
        [print(title.get('data').get('title'))
         for title in hot.get('children')]
    except Exception:
        print(None)
