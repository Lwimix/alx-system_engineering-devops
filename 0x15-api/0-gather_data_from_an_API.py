#!/usr/bin/python3
import requests
import sys


def to_do(employee_id):
    """Prints to do list"""
    """Prints the tofo list"""
    url = f'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)
    data = response.json()
    person = {}
    if employee_id.isdigit():
        employee_id = int(employee_id)
        for obj in data:
            if employee_id == obj['id']:
                person = obj
                url2 = f'https://jsonplaceholder.typicode.com/todos'
                response2 = requests.get(url2)
                data2 = response2.json()
                tasks = 0
                i = 0
                for piece in data2:
                    if piece['userId'] == employee_id:
                        tasks = tasks + 1
                        if piece['completed'] is True:
                            i = i + 1
                print(f"Employee {person['name']} is done with ({i}/{tasks})")
                for item in data2:
                    if item['userId'] == employee_id:
                        tasks = tasks + 1
                        if item['completed'] is True:
                            print(f"\t{item['title']}")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        to_do(sys.argv[1])
