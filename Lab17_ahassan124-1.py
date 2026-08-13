"""
Program: Lab 17 - Hacker News API Refactor
Author: Abass Hassan
Purpose: Retrieve top Hacker News articles from the Hacker News API
and safely display their titles and comment counts without crashing
when an article has no comments.
Starter Code: Based on the hn_submissions.py example from
Python Crash Course, Chapter 17.
Date: August 13, 2026
"""

import requests


url = "https://hacker-news.firebaseio.com/v0/topstories.json"

response = requests.get(url, timeout=10)

print(f"Status code: {response.status_code}")

submission_ids = response.json()

submission_dicts = []

for submission_id in submission_ids[:30]:
    url = (
        "https://hacker-news.firebaseio.com/v0/item/"
        f"{submission_id}.json"
    )

    response = requests.get(url, timeout=10)
    response_dict = response.json()

    submission_dict = {
        "title": response_dict["title"],
        "comments": response_dict.get("descendants", 0),
    }

    submission_dicts.append(submission_dict)

submission_dicts = sorted(
    submission_dicts,
    key=lambda submission: submission["comments"],
    reverse=True,
)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Comments: {submission_dict['comments']}")