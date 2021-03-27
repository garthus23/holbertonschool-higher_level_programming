#!/usr/bin/python3
"""
    module sys anf mysqld
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

"""
    changes the name of a State object from the database
"""

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    x = session.query(State).get(2)
    x.name = 'New Mexico'
    session.commit()
