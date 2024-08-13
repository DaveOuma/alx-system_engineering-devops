#!/usr/bin/python3
"""
Module 100-count
Defines a recursive function that queries the Reddit API to count occurrences of keywords in hot article titles.
"""

import requests


def count_words(subreddit, word_list, after=None, word_count={}):
    """
    Recursively queries the Reddit API to count and sort keywords in the titles of hot articles for a subreddit.
    
    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (list): A list of keywords to count.
        after (str): The 'after' parameter for pagination (optional).
        word_count (dict): A dictionary to store the count of each keyword (optional).

    Returns:
        None: Prints the count of keywords in descending order or nothing if the subreddit is invalid.
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
        titles = [post.get("data", {}).get("title").lower() for post in data.get("children", [])]
        after = data.get("after")
        
        # Count occurrences of each keyword in titles
        for word in word_list:
            count = sum(title.split().count(word.lower()) for title in titles)
            if word.lower() in word_count:
                word_count[word.lower()] += count
            else:
                word_count[word.lower()] = count
        
        # Continue recursively if more data is available
        if after:
            return count_words(subreddit, word_list, after, word_count)
        
        # Print the sorted word count
        for word, count in sorted(word_count.items(), key=lambda item: (-item[1], item[0])):
            if count > 0:
                print(f"{word}: {count}")
    return None

