#!/usr/bin/python3
"""Get First state from db."""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State).filter(State.name.like('%a%'))\
                     .order_by(State.id.asc())
    for state in results:
        print("{}: {}".format(state.id, state.name))
