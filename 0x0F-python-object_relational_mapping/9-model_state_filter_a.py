#!/usr/bin/python3
""" Script to list all State objects in db"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine(f'mysql+mysqldb://{mysql_username}:{mysql_password}\
            @localhost/{database_name}')

    Session = sessionmaker(bind=engine)

    session = Session()

    states = session.query(State).filter(State.name.like('½a½')).\
    order_by(State.id.asc()).all()

    for state in states:
        print(f"State ID: {state.id}, Name: {state.name}")

    session.close()
