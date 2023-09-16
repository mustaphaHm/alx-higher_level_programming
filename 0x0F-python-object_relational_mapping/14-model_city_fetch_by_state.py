#!/usr/bin/python3
"""Get cities from db."""
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State, City).filter(City.state_id == State.id)\
                     .order_by(City.id.asc())
    for state, city in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
