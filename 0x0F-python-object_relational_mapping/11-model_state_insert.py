#!/usr/bin/python3

"""This script adds a new state to a MySQL database.
It connects to the specified MySQL database using SQLAlchemy,
creates a new State object with the provided state name
('Louisiana' by default), adds it to the 'states' table,
commits the transaction, and prints the ID of the newly added state.
"""

if __name__ == "__main__":

    import sys
    from sqlalchemy.schema import Table
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session
    from model_state import Base, State

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    new = State(name='Louisiana')
    session.add(new)
    new_state = session.query(State).filter(State.name == 'Louisiana').first()
    session.commit()
    print("{}".format(new_state.id))
    session.close()
