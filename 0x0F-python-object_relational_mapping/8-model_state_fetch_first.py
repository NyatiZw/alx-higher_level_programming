#!/usr/bin/python3
""" Script to list all State objects in db"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    mysql_username, mysql_password, database_name = sys.argv[1:]

    engine = create_engine(f'mysql+mysqldb://{mysql_username}:{mysql_password}\
            @localhost/{database_name}')

    Session = sessionmaker(bind=engine)

    session = Session()

    first_item = session.query(State).oeder_by(State.id).first()

    if first_item:
        print(f"{first_item.id}: {first_item.name}")
    else:
        print("Nothing")

    session.close()
