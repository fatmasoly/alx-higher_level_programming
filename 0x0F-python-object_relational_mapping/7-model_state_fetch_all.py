#!/usr/bin/python3

"""This script connects to a MySQL database using SQLAlchemy
and retrieves all records from the 'states' table.
It takes command-line arguments for MySQL username, password,
and database name.The script connects to a MySQL server running
on localhost and uses SQLAlchemy ORM to interact with the database.
The retrieved records are printed in
the console in ascending order of their IDs."""

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
    for state in session.query(State).order_by(State.id).all():
        print("{}: {}".format(state.id, state.name))
    session.close()
