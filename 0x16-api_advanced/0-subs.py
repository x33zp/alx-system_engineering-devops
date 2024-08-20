#!/usr/bin/python3
""" A function that queries the Reddit API and returns the number of
    subscribers (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given, the function should return 0. """

import requests


def number_of_subscribers(subreddit):
    """ Qeries the Reddit API and returns the number of subscribers """
    if subreddit is None or not isinstance(subreddit, str):
        return 0

    url = 'https://api.reddit.com/r/{}/about'.format(subreddit)
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0"}

    res = requests.get(url, headers=headers, allow_redirects=False)

    try:
        result = res.json().get('data')
    except Exception:
        return 0

    return result.get('subscribers')
