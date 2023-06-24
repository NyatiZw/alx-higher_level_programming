#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    if len(sys.argv) != 5:
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    db_url = f'mysql://{mysql_username}:{mysql_password}@localhost:3306/{database_name}'
    engine = create_engine(db_url)

    session = Session()

    state = session.query(State).filter(State.name == state_name).first()

    if state:
        print(f"State ID: {state.id}")
    else:
        print("Not found")

    session.close()
