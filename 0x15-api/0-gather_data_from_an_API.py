#!/usr/bin/python3
'''Returns todo list from API for employee id passed'''

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
    print('Employee', user.get('name'),
          'is done with tasks({}/{}):'.
          format(len(completed), len(user_todos)))
    [print('\t', todo.get('title')) for todo in completed]

if __name__ == '__main__':
    do_request()
