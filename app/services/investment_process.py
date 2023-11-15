from datetime import datetime as dt

from app.models.base import AbstractModel


def investment_process(target: AbstractModel, sources: list[AbstractModel], ):
    target.invested_amount = (
        0 if target.invested_amount is None else target.invested_amount
    )
    for object in sources:
        if target.fully_invested:
            break
        object_amount = object.full_amount - object.invested_amount
        target_amount = target.full_amount - target.invested_amount
        invest_amount = (
            target_amount if target_amount < object_amount else object_amount
        )
        for element in [target, object]:
            element.invested_amount += invest_amount
            if element.full_amount == element.invested_amount:
                element.fully_invested = True
                element.close_date = dt.now()
    return sources
