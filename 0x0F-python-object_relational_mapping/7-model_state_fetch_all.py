import sys
from sqlalchemy import create_engine
from sqlalchemy import sessionmaker
from model_state import Base, State


if __name__ == '__main__':
    if len(sys.argv) != 4:
        sys.exit(1)


    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    engine = create_engine(f'mysql://{mysql_username}:{mysql_password}@localhost:3306/{database_name}')

    Base.metadata.bind = engine

    Session = sessionmaker(bind=engine)

    session = Session()

    states = session.query(State).order_by(State.id.asc()).all()

    for state in states:
        print(f"State ID: {state.id}, Name: {state.name}")
