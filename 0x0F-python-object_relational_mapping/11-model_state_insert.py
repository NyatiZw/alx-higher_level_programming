#!/usr/bin/python3
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    db_url = f'mysql://{username}:{password}@localhost:3306/{dbname}'
    engine = create_engine(db_url)

    Base.metadata.bind = engine

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")

    session.add(new_state)

    session.commit()

    print(f"New State ID: {new_state.id}")

    session.close()
