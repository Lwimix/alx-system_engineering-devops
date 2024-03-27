#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}.json"
    headers = {'User-Agent': 'Chrome/79.0.3945.79'}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return (0)
    else:
        check_sub = response.json()['data']['children'][0]['data']
        if 'subreddit' in check_sub.keys():
            mydict = response.json()['data']['children']
        else:
            return (0)
    return (mydict[0]['data']['subreddit_subscribers'])
