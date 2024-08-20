#!/usr/bin/python3
""" A function that queries the Reddit API and returns the number of
    subscribers (not active users, total subscribers) for a given subreddit.
    If an invalid subreddit is given, the function should return 0. """
import requests


def number_of_subscribers(subreddit):
    url = 'https://api.reddit.com/r/{}/about'.format(subreddit)

    res = requests.get(url, allow_redirects=False)
    result = res.json()

    try:
        return result.get('data').get('subscribers')
    except Exception as e:
        return 0
