#!/usr/bin/python3

"""This script deletes states from a MySQL database
whose names contain the letter 'a'. It connects to
the specified MySQL database using SQLAlchemy, queries the 'states'
table to find states with names containing the letter 'a',
deletes them from the database, commits the transaction,
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
    for state in session.query(State).filter(State.name.like('%a%')):
        session.delete(state)
    session.commit()
    session.close()
