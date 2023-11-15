from sqlalchemy import Column, ForeignKey, Integer, Text

from app.models.base import AbstractModel


PATTERN = (
    'Пожертвование: Внес {user}. Сумма {amount}. Дата {date}. '
    'Отметка о закрытии: {fully_invested}'
)


class Donation(AbstractModel):
    __tablename__ = 'donation'

    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(Text)

    def __repr__(self):
        return PATTERN.format(
            user=self.user_id,
            amount=self.invested_amount,
            date=self.create_date,
            fully_invested=self.fully_invested
        )
