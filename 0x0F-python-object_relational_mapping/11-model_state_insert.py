#!/usr/bin/python3
"""
    module sys anf mysqld
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

"""
    script that adds the State object “Louisiana” to the database
"""

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                           sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    c1 = State(name='Louisiana')
    session.add(c1)
    session.commit()
    query = (session.query(State.id).
             filter(State.name.like('Louisiana')).first())
    if query:
        print(query[0])
    else:
        print('Not found')
