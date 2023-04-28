#!/usr/bin/python3
'''Export list of dictionaries'''

import json
import requests
import sys

url = 'https://jsonplaceholder.typicode.com/'


def do_request():
    '''Performs request'''
    # Get users
    response = requests.get(url + 'users/')
    if response.status_code != 200:
        return print('Error: status_code:', response.status_code)
    users = response.json()

    # Get todos
    response = requests.get(url + 'todos/')
    if response.status_code != 200:
        return print('Error: status_code:', response.status_code)
    todos = response.json()

    # Create list of dictionaries for export
    data = {}
    for user in users:
        user_todos = [todo for todo in todos
                      if todo.get('userId') == user.get('id')]
        user_todos = [{'username': user.get('username'),
                       'task': todo.get('title'),
                       'completed': todo.get('completed')}
                      for todo in user_todos]
        data[str(user.get('id'))] = user_todos

    with open('todo_all_employees.json', 'w') as file:
        json.dump(data, file)


if __name__ == '__main__':
    do_request()
