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

    newstate = State(name="Louisiana")
    session.add(newstate)
    session.commit()

    state_id = session.query(State).filter(State.name == newstate.name).first()
    try:
        print("{}".format(state_id.id))
    except:
        print("Not found")

    session.close()
