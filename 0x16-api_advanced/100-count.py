#!/usr/bin/python3
'''Get ALL hot posts of a given Reddit subreddit'''
import requests


def count_words(subreddit, word_list, instances={}, after="", count=0):
    """Queries the Reddit API, parses titles of hot articles,
    and prints a sorted count of given keywords.

    Args:
        subreddit (str): The subreddit to search.
        word_list (list): The list of keywords to count.
        instances (dict): Key/value pairs of keywords/counts.
        after (str): The parameter for the next page of the API results.
        count (int): The parameter of results matched thus far.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)

    try:
        if response.status_code == 200:
            results = response.json()
            data = results.get("data")
            after = data.get("after")
            count += data.get("dist")
            children = data.get("children")

            for child in children:
                title = child.get("data").get("title").lower()
                title_words = title.split()

                for keyword in word_list:
                    keyword = keyword.lower()
                    if keyword in title_words:
                        instances[keyword] = instances.get(keyword, 0)
                        + title_words.count(keyword)

            if after is not None:
                count_words(subreddit, word_list, instances, after, count)

    except Exception as e:
        print("An error occurred:", e)

    if after is None:
        sorted_instances = sorted(instances.items(),
                                  key=lambda x: (-x[1], x[0]))

        for keyword, count in sorted_instances:
            print(f"{keyword}: {count}")


# Example usage:
# subreddit = "programming"
# word_list = ["python", "java", "javascript"]
# count_words(subreddit, word_list)
