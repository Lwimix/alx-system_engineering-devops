#!/usr/bin/python3
import requests
import sys


def to_do(employee_id):
    """Prints the tofo list"""
    url = f'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)
    data = response.json()
    person = {}
    if employee_id.isdigit():
        filename = f"{employee_id}.csv"
        employee_id = int(employee_id)
        for obj in data:
            if employee_id == obj['id']:
                person = obj
                line = f'"{str(employee_id)}", "{person["username"]}"'
                url2 = f'https://jsonplaceholder.typicode.com/todos'
                response2 = requests.get(url2)
                data2 = response2.json()
                with open(filename, 'w', newline='') as f:
                    for it in data2:
                        if it['userId'] == employee_id:
                            comp = f'"{it["completed"]}"'
                            task = f'"{it["title"]}"'
                            f.write(f'{line}, {comp}, {task}\n')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        to_do(sys.argv[1])
