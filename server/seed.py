#!/usr/bin/env python3

from app import db
from models import TodoItem

if __name__ == '__main__':
    db.create_all()

    task1 = TodoItem(title='Buy fruits and groceries', completed=False)
    task2 = TodoItem(title='Finish project and code challenges', completed=False)
    task3 = TodoItem(title='Go for a run', completed=True)

    db.session.add(task1)
    db.session.add(task2)
    db.session.add(task3)

    db.session.commit()
