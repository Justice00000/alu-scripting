#!/usr/bin/python3
""" a recursive function that queries the Reddit API """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """ returns list with titles """
    URL = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    my_headers = {
        "User-Agent": "LetsGo/0.1 (by u/Justice00101)""
        }
    params = {'after': after}
    response = requests.get(URL, headers=my_headers,
                            params=params, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()['data']
        for child in data['children']:
            title = child['data']['title']
            hot_list.append(title)
        # get next page of results
        try:
            after = data['after']
            return recurse(subreddit, hot_list, after)
        except KeyError as e:
            print('Key Error', str(e))
            pass
    else:
        return None
