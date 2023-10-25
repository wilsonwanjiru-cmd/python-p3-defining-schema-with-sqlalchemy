# Import necessary modules
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

# Define a declarative base
Base = declarative_base()

# Define a class for the 'students' table
class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

if __name__ == '__main__':
    # Create an SQLite database engine
    engine = create_engine('sqlite:///students.db')

    # Create the 'students' table in the database
    Base.metadata.create_all(engine)
