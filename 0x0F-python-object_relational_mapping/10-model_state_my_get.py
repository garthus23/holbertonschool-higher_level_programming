#!/usr/bin/python3
"""
    module sys anf mysqld
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

"""
    prints the State object with the name passed as argument
"""

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = (session.query(State.id).
             filter(State.name.like(sys.argv[4])).first())

    if query:
        print(query[0])
    else:
        print('Not found')
