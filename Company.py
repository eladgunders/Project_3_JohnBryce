from datetime import datetime
from sqlalchemy import Column, Integer, String, DateTime, REAL
from sqlalchemy.orm import relationship
from db_config import Base


class Company(Base):
    __tablename__ = 'company'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(50), unique=True, nullable=False)
    age = Column(Integer(), nullable=False, default=0)
    address = Column(String(50), nullable=False)
    salary = Column(REAL())

    def __repr__(self):
        return f'\n<Company id={self.id} name={self.name} age={self.age} address={self.self.adress} salary={self.salary}>'

    def __str__(self):
        return f'\n<Company id={self.id} name={self.name} age={self.age} address={self.self.adress} salary={self.salary}>'
