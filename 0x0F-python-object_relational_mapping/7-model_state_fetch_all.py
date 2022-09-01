#!/usr/bin/python3
"""
this script list all states
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                          .format(argv[1], argv[2], argv[3]),
                          pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    for list in session.query(State).order_by(State.id):
        print(f"{list.id}: {list.name}")

    session.close()
