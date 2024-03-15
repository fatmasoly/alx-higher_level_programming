#!/usr/bin/python3

"""This script queries a MySQL database for states whose names
contain the letter 'a'. It connects to the specified MySQL database
using SQLAlchemy, retrieves the relevant states from the 'states' table,
and prints their IDs and names."""

if __name__ == "__main__":

    import sys
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state in session.query(State)\
                        .filter(State.name.like('%a%'))\
                        .order_by(State.id):
        print("{}: {}".format(state.id, state.name))
    session.close()
