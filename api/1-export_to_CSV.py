#!/usr/bin/python3
"""
Starting with API
"""

if __name__ == '__main__':
    import requests
    import sys
    userid = sys.argv[1]
    data = requests\
        .get(f'https://jsonplaceholder.typicode.com/users/{userid}')\
        .json().get('username')
    todos = requests\
        .get(f'https://jsonplaceholder.typicode.com/users/{userid}/todos')\
        .json()
    with open(f"{userid}.csv", "a") as f:
        for tasks in todos:
            status = tasks.get("completed")
            title = tasks.get("title")
            f.write(f'"{userid}","{data}","{status}","{title}"\n')
