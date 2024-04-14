#!/usr/bin/python3
"""
This script adds the State object 
“Louisiana” to the database hbtn_0e_6_usa
"""

from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and get the states
    from the database.
    """

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    new_st = State("Louisiana")
    session.add(new_st)

    state = session.query(State).order_by(State.id)
    if state is not None:
        for st in state:
            print('{0}: {1}'.format(st.id, st.name))
    else:
        print("Not found")
    session.commit()
    session.close()