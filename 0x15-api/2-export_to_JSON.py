#!/usr/bin/python3
'''Export todo list to json file'''

import json
import requests
import sys

url = 'https://jsonplaceholder.typicode.com/'


def do_request():
    '''Performs request'''

    # Get employee id
    if len(sys.argv) < 2:
        return print('USAGE:', __file__, '<employee id>')
    employee_id = sys.argv[1]
    try:
        _employee_id = int(sys.argv[1])
    except ValueError:
        return print('Employee ID must be an integer')

    # Get user
    response = requests.get(url + 'users/' + employee_id)
    if response.status_code == 404:
        return print('User ID not found')
    elif response.status_code != 200:
        return print('Error: status_code:', response.status_code)
    user = response.json()

    # Get todos
    response = requests.get(url + 'todos/')
    if response.status_code != 200:
        return print('Error: status_code:', response.status_code)
    todos = response.json()

    # Display employee todo list progress
    user_todos = [todo for todo in todos
                  if todo.get('userId') == user.get('id')]
    completed = [todo for todo in user_todos if todo.get('completed')]

    user_todos = [{'task': todo.get('title'),
                   'completed': todo.get('completed'),
                   'username': user.get('username')}
                  for todo in user_todos]
    data = {employee_id: user_todos}
    with open(employee_id + '.json', 'w') as file:
        json.dump(data, file)


if __name__ == '__main__':
    do_request()
