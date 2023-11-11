#!/usr/bin/python3
"""3-count.py"""
import requests

def count_words(subreddit: str, word_list: list, after: str = "", words_count: dict = {}):
    """Count occurrences of specified words in subreddit post titles."""
    subreddit_lower = subreddit.lower()

    if not words_count:
        words_count = {word.lower(): 0 for word in word_list}

    if after is None:
        sorted_words_count = sorted(words_count.items(), key=lambda x: (-x[1], x[0]))
        for word, count in sorted_words_count:
            if count:
                print(f'{word}: {count}')
        return None

    url = f"https://www.reddit.com/r/{subreddit_lower}/hot.json?limit=100"
    headers = {"User-Agent": "LetsGo/1.0 by Justice00101"}
    params = {'after': after}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()

        hot = response.json()['data']['children']
        after_token = response.json()['data']['after']

        for post in hot:
            title = post['data']['title']
            lower_title_words = [word.lower() for word in title.split(' ')]

            for word in words_count:
                words_count[word] += lower_title_words.count(word)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None
    except KeyError:
        print("Error: Failed to parse Reddit API response.")
        return None

    count_words(subreddit, word_list, after_token, words_count)
