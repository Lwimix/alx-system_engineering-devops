#!/usr/bin/python3
"""This module contains the to_json function"""
import requests
import sys


if __name__ == '__main__':
    def to_json(employee_id):
        """Converts to JSON"""
        url = f'https://jsonplaceholder.typicode.com/users'
        response = requests.get(url)
        data = response.json()
        person = {}
        end = {}
        my_id = employee_id
        inner = {}
        full = []
        if employee_id.isdigit():
            filename = f"{employee_id}.json"
            employee_id = int(employee_id)
            for obj in data:
                if employee_id == obj.get('id'):
                    person = obj
                    url2 = f'https://jsonplaceholder.typicode.com/todos'
                    response2 = requests.get(url2)
                    data2 = response2.json()
                    for item in data2:
                        if item.get('userId') == employee_id:
                            inner["task"] = item.get("title")
                            inner["completed"] = item.get("completed")
                            inner["username"] = person.get("username")
                            full.append(inner)
            end = {f'{my_id}': full}
            with open(filename, 'w', newline='') as f:
                f.write(f'{end}')

if len(sys.argv) > 1:
    to_json(sys.argv[1])
