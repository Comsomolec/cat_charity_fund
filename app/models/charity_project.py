from sqlalchemy import Column, String, Text

from app.models.base import AbstractModel


MAX_LENGHT_NAME = 100
PATTERN = (
    'Благотворительный проект: {name}. Создан {date}. Объем {amount} '
    'Отметка о закрытии: {fully_invested}'
)


class CharityProject(AbstractModel):
    __tablename__ = 'charityproject'

    name = Column(String(MAX_LENGHT_NAME), unique=True, nullable=False)
    description = Column(Text, nullable=False)

    def __repr__(self):
        return PATTERN.format(
            name=self.name,
            date=self.create_date,
            amount=self.full_amount,
            fully_invested=self.fully_invested,
        )
