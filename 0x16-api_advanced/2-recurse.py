#!/usr/bin/python3
"""Reddit API"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """Recursively query Reddict API and return a list"""
    try:
        url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
        headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0"}
        params = {"limit": 100, "after": after}

        req = requests.get(url, headers=headers,
                               params=params, allow_redirects=False)

        result = req.json().get('data')

        after = result.get('after')

        for child in result.get('children'):
            hot_list.append(child.get('data').get('title'))
        if after is not None:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    except Exception:
        print(None)
