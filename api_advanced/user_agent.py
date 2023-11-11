#!/usr/bin/python3
import requests

def get_user_agent(url="https://www.whatismybrowser.com/detect/what-is-my-user-agent"):
    try:
        response = requests.get(url)
        user_agent = response.headers['User-Agent']
        return user_agent
    except Exception as e:
        print(f"Error: {e}")
        return None

user_agent = get_user_agent()
if user_agent:
    print("Your User-Agent is:")
    print(user_agent)
