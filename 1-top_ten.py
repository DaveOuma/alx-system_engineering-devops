#!/usr/bin/python3
"""
Module 1-top_ten
Defines a function that queries the Reddit API to print the top 10 hot posts of a subreddit.
"""

import requests


def top_ten(subreddit):
    """
    Queries the Reddit API to print the titles of the first 10 hot posts for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        None: Prints the titles of the top 10 posts or None if the subreddit is invalid.
    """
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    
    # Send the GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Extract data from the JSON response
        data = response.json().get("data", {}).get("children", [])
        
        # Print each post title
        for post in data:
            print(post.get("data", {}).get("title"))
    else:
        # Print None if the subreddit is invalid
        print(None)

