#!/usr/bin/python3
"""This module contains the number_of_subscribers function"""
import requests
import sys


def number_of_subscribers(subreddit):
    """Prints out number of subscribers for a subredddit"""
    url = f"https://www.reddit.com/r/{subreddit}/about/.json"
    header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            }
    response = requests.get(url, headers=header)
    data = response.json()
    if ("error" in data.keys()):
        return (0)
    else:
        return (data["data"]["subscribers"])
