#!/usr/bin/python3
""""3-count.py"""
import requests


def count_words(subreddit, word_list, after="", words_count={}):
    """"count words"""
    if not words_count:
        for word in word_list:
            if word.lower() not in words_count:
                words_count[word.lower()] = 0

    if after is None:
        wordict = sorted(words_count.items(), key=lambda x: (-x[1], x[0]))
        for word in wordict:
            if word[1]:
                print('{}: {}'.format(word[0], word[1]))
        return None
    URL = "https://www.reddit.com/r/{}/hot.json?limit=100".format(subreddit)
    my_headers = {
        "User-Agent": "LetsGo/0.1 (by u/Justice00101)"
        }
    params = {'after': after}
    response = requests.get(URL, headers=my_headers, params=params)

    if response.status_code != 200:
        return None

    try:
        hot = response.json()['data']['children']
        aft = response.json()['data']['after']
        for post in hot:
            title = post['data']['title']
            lower = [word.lower() for word in title.split(' ')]

            for word in words_count.keys():
                words_count[word] += lower.count(word)

    except Exception:
        return None

    count_words(subreddit, word_list, aft, words_count)
