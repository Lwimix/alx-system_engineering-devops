#!/usr/bin/python3
"""This module contains the number_of_subscribers function"""
import requests
import sys


def number_of_subscribers(subreddit):
    """Prints out number of subscribers for a subredddit"""
    url = "https://www.reddit.com/subreddits/search.json"
    params = {"q": f"{subreddit}"}
    header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            }
    response = requests.get(url, headers=header, params=params)
    data = response.json()
    for sub in data["data"]["children"]:
        if (sub["data"]["display_name"] == f"{subreddit}"):
            return (sub["data"]["subscribers"])
    return (0)
