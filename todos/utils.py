import json
from datetime import datetime
from .exceptions import InvalidTaskDueDateException


def parse_date(date_str):
    formats = ['%Y-%M-%D', '%Y-%M-%D %H:%M:%S']
    try:
        return datetime.strptime(date_str, formats)
    except:
        return None

def parse_int(value):
    try:
        return int(value)
    except ValueError:
        return None


def serialize(tasks):
    pass


def unserialize(blob):
    pass


def summary(tasks):
    pass
