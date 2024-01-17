#!/usr/bin/python3
"""This module contains the to_do function"""
import requests
import sys


def number_of_subscribers(subreddit):
    """Prints out number of subscribers for a subredddit"""
    url = "https://www.reddit.com/subreddits/search.json"
    params = {"q": f"{subreddit}"}
    header = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
            }
    try:
        response = requests.get(url, headers=header, params=params)
        data = response.json()
        for sub in data["data"]["children"]:
            if (sub["data"]["display_name"] == f"{subreddit}"):
                return (sub["data"]["subscribers"])
        return (0)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
    if len(sys.argv) > 1:
        number_of_subscribers(sys.argv[1])
