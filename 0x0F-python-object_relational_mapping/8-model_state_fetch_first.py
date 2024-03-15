#!/usr/bin/python3

"""This script connects to a MySQL database using SQLAlchemy
and retrieves the first record from the 'states' table.
It takes command-line arguments for MySQL username, password,
and database name.The script connects to a MySQL server running
on localhost and uses SQLAlchemy ORM to interact with the database.
The retrieved record, if exists, is printed in the console.
Otherwise, it prints "Nothing"."""

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
    first = session.query(State).order_by(State.id).first()
    if first:
        print("{}: {}".format(first.id, first.name))
    else:
        print("Nothing")
    session.close()
