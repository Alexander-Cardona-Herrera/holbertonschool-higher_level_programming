#!/usr/bin/python3
"""Start link class to table in database
"""
from sqlalchemy import (create_engine)
import sys
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(engine)
    session = Session()

    first_state = session.query(State).order_by(State.id).first()
    if (not first_state):
        print("Nothing")
    print("{}: {}".format(first_state.id, first_state.name))

    session.close()
