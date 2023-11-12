from sqlalchemy import Column, ForeignKey, Integer, Text

from app.models.base import BaseClass


class Donation(BaseClass):
    __tablename__ = 'donation'

    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text)
