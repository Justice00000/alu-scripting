#!/usr/bin/python3
import requests

def number_of_subscribers(subreddit):
    """
    Query the Reddit API and return the number of subscribers of a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.

    Returns:
        int: The number of subscribers, or 0 if an error occurs.
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "4UqdQ42h3yqavQSMPnkdV8OtuI9khA/1.0 by Justice00101"}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        return response.json().get("data").get("subscribers")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return 0
