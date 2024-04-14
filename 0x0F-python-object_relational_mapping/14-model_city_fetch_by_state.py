#!/usr/bin/python3
"""
This script prints all City objects 
from the database hbtn_0e_14_usa
"""

from sys import argv
from model_city import City
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access to the database and get the cities
    from the database.
    """

    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    cts = session.query(City).order_by(City.id)
    for instance in cts:
        print('{2}: ({0}) {1}'.format(instance.id, instance.name, instance.state_id.name))