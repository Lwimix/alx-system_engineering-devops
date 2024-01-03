#!/usr/bin/python3
import requests
import sys


def to_csv(employee_id):
    """Converts to CSV"""
    url = f'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)
    data = response.json()
    person = {}
    if employee_id.isdigit():
        filename = f"{employee_id}.csv"
        employee_id = int(employee_id)
        for obj in data:
            if employee_id == obj.get('id'):
                person = obj
                line = f'"{str(employee_id)}", "{person.get("username")}"'
                url2 = f'https://jsonplaceholder.typicode.com/todos'
                response2 = requests.get(url2)
                data2 = response2.json()
                with open(filename, 'w', newline='') as f:
                    for it in data2:
                        if it.get('userId') == employee_id:
                            comp = f'"{it.get("completed")}"'
                            task = f'"{it.get("title")}"'
                            f.write(f'{line}, {comp}, {task}\n')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        to_csv(sys.argv[1])
