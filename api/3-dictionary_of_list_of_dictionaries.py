#!/usr/bin/python3
"""
Starting with API
"""

if __name__ == '__main__':
    import requests
    import json
    dicti_list = []
    dicti2 = {}
    with open(f"todo_all_employees.json", "w") as f:
        uc = f'https://jsonplaceholder.typicode.com/users/'
        user_count = len(requests.get(uc).json())
        for userid in range(1, user_count+1):
            d = f'https://jsonplaceholder.typicode.com/users/{userid}'
            data = requests.get(d).json().get('username')
            fu = f'https://jsonplaceholder.typicode.com/users/{userid}/todos'
            todos = requests\
                .get(fu).json()
            for tasks in todos:
                status = tasks.get("completed")
                title = tasks.get("title")
                dicti = {
                    "username": data,
                    "task": title,
                    "completed": status
                }
                dicti_list.append(dicti)
            dicti2[userid] = dicti_list
            dicti_list = []
        f.write(json.dumps(dicti2))
