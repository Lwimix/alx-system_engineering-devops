#!/usr/bin/python3
"""This module contains the to_do function"""
import requests
import sys


def top_ten(subreddit):
    """Prints out top ten posts for a subredddit"""
    url = f"https://www.reddit.com/r/{subreddit}/top.json"
    params = {
            "limit": 10
            }
    header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            }
    response = requests.get(url, headers=header, params=params)
    data = response.json()
    if ("error" in data.keys()):
        print(None)
    else:
        for sub in data["data"]["children"]:
            print(sub["data"]["title"])
