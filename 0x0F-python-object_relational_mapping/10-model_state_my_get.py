#!/usr/bin/python3
"""
this script list all states
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State)\
                   .filter(State.name == sys.argv[4])\
                   .order_by(State.id)

    if query.count() > 0:
        for result in query:
            print(result.id)
    else:
        print('Not found')

    session.close()
