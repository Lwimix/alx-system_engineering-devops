#!/usr/bin/python3
"""This module contains the to_json function"""
import json
import requests
import sys


if __name__ == '__main__':
    def to_json(employee_id):
        """Converts to JSON"""
        url = f'https://jsonplaceholder.typicode.com/users/{employee_id}'
        response = requests.get(url)
        user = response.json()
        name = user.get('username')
        my_id = employee_id
        inner = {}
        full = []
        if employee_id.isdigit():
            filename = f"{employee_id}.json"
            employee_id = int(employee_id)
            url2 = f'https://jsonplaceholder.typicode.com/todos?userId={my_id}'
            response2 = requests.get(url2)
            data2 = response2.json()
            for item in data2:
                inner["task"] = item.get("title")
                inner["completed"] = item.get("completed")
                inner["username"] = name
                full.append(inner)
            end = {f'{my_id}': full}
            with open(filename, 'w', newline='') as f:
                json.dump(end, f)

if len(sys.argv) > 1:
    to_json(sys.argv[1])
