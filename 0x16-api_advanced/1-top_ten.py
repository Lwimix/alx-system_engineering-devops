#!usr/bin/python3
"""
Contains the top_ten function
"""
import requests


def top_ten(subreddit):
    """
    Returns the top ten hot posts from a subreddit
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Chrome/79.0.3945.79'}
    params = {'limit': 10}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        print(None)
    else:
        check_sub = response.json()['data']['children'][0]['data']
        children = response.json()['data']['children']
        num = 0
        if 'subreddit' in check_sub.keys():
            for child in children:
                if num == 10:
                    break
                num = num + 1
                print(child['data']['title'])
        else:
            print(None)
