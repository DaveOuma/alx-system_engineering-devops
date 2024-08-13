#!/usr/bin/python3
"""
Module 2-recurse
Defines a recursive function that queries the Reddit API to return a list of hot article titles.
"""

import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively queries the Reddit API to retrieve the titles of all hot articles for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query.
        hot_list (list): A list to store the titles of hot articles.
        after (str): The 'after' parameter for pagination (optional).

    Returns:
        list: A list of titles of hot articles or None if the subreddit is invalid.
    """
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    params = {"after": after} if after else {}
    
    # Send the GET request to the Reddit API
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Extract data from the JSON response
        data = response.json().get("data", {})
        hot_list.extend([post.get("data", {}).get("title") for post in data.get("children", [])])
        after = data.get("after")
        
        # Continue recursively if more data is available
        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list
    
    # Return None if the subreddit is invalid
    return None

