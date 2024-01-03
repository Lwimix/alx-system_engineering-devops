#!/usr/bin/python3
"""This module contains the to_do function"""
import requests
import sys


if __name__ == '__main__':
    def to_do(employee_id):
        """Prints to do list"""
        url = f'https://jsonplaceholder.typicode.com/users'
        response = requests.get(url)
        data = response.json()
        person = {}
        if employee_id.isdigit():
            employee_id = int(employee_id)
            for obj in data:
                if employee_id == obj.get('id'):
                    person = obj
                    url2 = f'https://jsonplaceholder.typicode.com/todos'
                    response2 = requests.get(url2)
                    data2 = response2.json()
                    tasks = 0
                    i = 0
                    name = person.get('name')
                    for piece in data2:
                        if piece.get('userId') == employee_id:
                            tasks = tasks + 1
                            if piece.get('completed') is True:
                                i = i + 1
                    print(f"Employee {name} is done with tasks({i}/{tasks}):")
                    for item in data2:
                        if item.get('userId') == employee_id:
                            tasks = tasks + 1
                            if item.get('completed') is True:
                                print(f"\t {item.get('title')}")


if len(sys.argv) > 1:
    to_do(sys.argv[1])
