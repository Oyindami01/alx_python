"""
Module for defining a State class using SQLAlchemy.

This module contains the definition of the State class,which represents a state
in a database table. The State class inherits from SQLAlchemy's Base class and
is used to interact with a MySQL database.

Usage:
    To use this module, you need to create an instance of the State class and
    configure the database connection details. Then you can create tables in
    the database and perform CRUD (Create, Read, Update, Delete) operations.

"""


from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class State(Base):
    """
    Represents a state in the database.

    Attributes:
        id (int): Unique identifier for the state (auto-generated).
        name (str): Name of the state (up to 128 characters).
    """

    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    engine = create_engine(
        'mysql://your_username:your_password@localhost:3306/your_database'
    )

    # Create tables based on the defined classes (e.g., State)
    Base.metadata.create_all(engine)

    # Create a session to interact with the database
    Session = sessionmaker(bind=engine)
    session = Session()