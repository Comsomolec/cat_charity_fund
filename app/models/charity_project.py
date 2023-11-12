from sqlalchemy import Column, String, Text

from app.models.base import BaseClass


MAX_LENGHT_NAME = 100


class CharityProject(BaseClass):
    __tablename__ = 'charityproject'

    name = Column(String(MAX_LENGHT_NAME), unique=True, nullable=False)
    description = Column(Text, nullable=False)
