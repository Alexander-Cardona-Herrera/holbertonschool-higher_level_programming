#!/usr/bin/python3
"""Start link class to table in database
"""
from sqlalchemy import (create_engine)
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()

    for states, cities in session.query(State, City)\
            .filter(State.id == City.state_id).order_by(City.id).all():
        print("{}: ({}) {}".format(
            states.name, cities.id, cities.name))
    session.close()
