#!/usr/bin/python3
""""Doc"""
import requests


def number_of_subscribers(subreddit):
    """"Doc"""
    URL = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    my_headers = {
        "User-Agent": "LetsGo/0.1 by Justice00101"
        }

    raw_response = requests.get(URL, headers=my_headers, allow_redirects=False)

    if raw_response.status_code == 200:
        json_response = raw_response.json()
        sub_count = json_response['data']['subscribers']
        return sub_count

    else:
        return 0
