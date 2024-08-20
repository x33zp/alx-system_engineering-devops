#!/usr/bin/python3
"""Reddit API"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively query Reddict API and return a list"""
    url = 'https://api.reddit.com/r/{}/hot'.format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0"}
    params = {"limit": 100, "after": after}

    res = requests.get(url, headers=headers, params=params,
                       allow_redirects=False)

    try:
        result = res.json()
    except Exception:
        return None

    after = result.get('data').get('after')

    for child in result.get('data').get('children'):
        hot_list.append(child.get('data').get('title'))
    if after is not None:
        recurse(subreddit, hot_list, after)
    else:
        return hot_list
