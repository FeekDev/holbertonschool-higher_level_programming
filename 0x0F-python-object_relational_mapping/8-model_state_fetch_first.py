#!/usr/bin/python3
"""
this script filtr the nth position id
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

    result = session.query(State).first()
    if result is not None:
        print(f"{result.id}: {result.name}")
    else:
        print('Nothing')

    session.close()
