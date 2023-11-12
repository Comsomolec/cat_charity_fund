from datetime import datetime as dt
from typing import Union

from sqlalchemy.ext.asyncio import AsyncSession

from app.crud import charityproject_crud, donation_crud
from app.models import Donation, CharityProject


async def investment_process(
    obj_in: Union[Donation, CharityProject],
    session: AsyncSession
):
    project = await charityproject_crud.get_open_project(session)
    donation = await donation_crud.get_open_donation(session)
    if not project or not donation:
        await session.commit()
        await session.refresh(obj_in)
        return obj_in
    project_balance = project.full_amount - project.invested_amount
    donation_balance = donation.full_amount - donation.invested_amount
    if project_balance > donation_balance:
        project.invested_amount += donation_balance
        donation.invested_amount += donation_balance
        donation.fully_invested = True
        donation.close_date = dt.now()
    elif project_balance == donation_balance:
        project.invested_amount += donation_balance
        donation.invested_amount += donation_balance
        donation.fully_invested, project.fully_invested = True, True
        donation.close_date, project.close_date = dt.now(), dt.now()
    elif project_balance < donation_balance:
        donation.full_amount -= project_balance
        project.invested_amount += project_balance
        donation.invested_amount += project_balance
        project.fully_invested = True
        project.close_date = dt.now()
    session.add(project)
    session.add(donation)
    await session.commit()
    await session.refresh(project)
    await session.refresh(donation)
    return await investment_process(obj_in, session)
