from datetime import datetime

from .exceptions import (
    InvalidTaskStatus, TaskAlreadyDoneException, TaskDoesntExistException, InvalidTaskDueDateException)
from .utils import parse_date, parse_int


def new():
    return []


def create_task(tasks, name, description=None, due_on=None):
    result = {
        'task' : name,
        'description' : description,
    }
    if due_on and type(due_on) != datetime:
        due_on = parse_date(due_on)
        if due_on is None:
            raise InvalidTaskDueDateException
    result['due_on'] = due_on
    tasks.append(result)
    return result


def list_tasks(tasks, status='all'):
    if status not in ['all','done','pending']:
        raise InvalidTaskStatus


def complete_task(tasks, name):
    for task in tasks:
        if task['task'] == name:
            if task['status'] == 'done':
                
