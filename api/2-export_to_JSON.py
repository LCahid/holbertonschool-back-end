#!/usr/bin/python3
"""
Starting with API
"""

if __name__ == '__main__':
    import requests
    import sys
    import json
    userid = sys.argv[1]
    dicti_list = []
    data = requests\
        .get(f'https://jsonplaceholder.typicode.com/users/{userid}')\
        .json().get('username')
    todos = requests\
        .get(f'https://jsonplaceholder.typicode.com/users/{userid}/todos')\
        .json()
    with open(f"{userid}.json", "w") as f:
        for tasks in todos:
            status = tasks.get("completed")
            title = tasks.get("title")
            dicti = {
                "task": title,
                "completed": status,
                "username": data
            }
            dicti_list.append(dicti)
        dicti2 = {
            userid: dicti_list
        }
        f.write(json.dumps(dicti2))
