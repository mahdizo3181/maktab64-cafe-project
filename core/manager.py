from sqlalchemy import Column, ForeignKey, String, create_engine, Integer, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from abc import ABC, abstractmethod

Base = declarative_base()
engine = create_engine('postgresql://postgres:123456@localhost/postgres')
session = sessionmaker(bind=engine)()


class BaseManager(ABC):
    @classmethod
    @abstractmethod
    def create(cls, table: str, row_id):
        """
        to create an object and save into data base
        """
