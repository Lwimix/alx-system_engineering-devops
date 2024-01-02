#!/usr/bin/python3
import requests
import sys


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
        employee_id = int(employee_id)
        for obj in data:
            if employee_id == obj['id']:
                person = obj
                url2 = f'https://jsonplaceholder.typicode.com/todos'
                response2 = requests.get(url2)
                data2 = response2.json()
                for item in data2:
                    if item['userId'] == employee_id:
                        inner["task"] = item["title"]
                        inner["completed"] = item["completed"]
                        inner["username"] = person["username"]
                        full.append(inner)
        end = {f'{my_id}': full}
        print(end)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        to_json(sys.argv[1])
