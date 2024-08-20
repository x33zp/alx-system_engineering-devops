#!/usr/bin/python3
"""Reddit API"""
import requests

def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the
    first 10 hot posts listed for a given subreddit"""
    url = f'https://api.reddit.com/r/{subreddit}/hot'
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0"}
    params = {"limit": 10}

    res = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    if res.status_code != 200:
        print(f"Error: Received status code {res.status_code}")
        return
    
    try:
        result = res.json()
    except ValueError:
        print("Error: Failed to parse JSON")
        print("Response Content:", res.text)
        return

    hot = result.get('data')
    if hot is None:
        print("No data found for subreddit:", subreddit)
        return
    
    for title in hot.get('children', []):
        print(title.get('data', {}).get('title', "No title found"))
