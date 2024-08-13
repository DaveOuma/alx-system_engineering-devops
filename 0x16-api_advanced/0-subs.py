#!/usr/bin/python3
"""
Module 0-subs
Defines a function that queries the Reddit API to return the number of subscribers.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Queries the Reddit API to get the number of subscribers for a given subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers to the subreddit, or 0 if the subreddit is invalid.
    """
    headers = {'User-Agent': 'Mozilla/5.0'}
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    
    # Send the GET request to the Reddit API
    response = requests.get(url, headers=headers, allow_redirects=False)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Extract data from the JSON response
        data = response.json().get("data", {})
        return data.get("subscribers", 0)
    
    # Return 0 if the subreddit is invalid
    return 0

