#!/usr/bin/python3

"""This script updates the name of a state in a MySQL database.
It connects to the specified MySQL database using SQLAlchemy,
retrieves the state with the specified ID (2 by default),
updates its name to 'New Mexico', commits the transaction,
and closes the session.
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
    state = session.query(State).filter(State.id == 2).first()
    State.name = 'New Mexico'
    session.commit()
    session.close()
