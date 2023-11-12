from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import false

from app.crud.base import CRUDBase
from app.models import Donation, User


class CRUDDonation(CRUDBase):
    async def get_by_user(
        self,
        user: User,
        session: AsyncSession,
    ) -> list[Donation]:
        donations = await session.execute(
            select(Donation).where(Donation.user_id == user.id)
        )
        donations = donations.scalars().all()
        return donations

    async def get_open_donation(
        self,
        session: AsyncSession,
    ) -> Donation:
        donation = await session.execute(
            select(Donation)
            .where(Donation.fully_invested == false())
            .order_by(Donation.create_date)
        )
        return donation.scalars().first()


donation_crud = CRUDDonation(Donation)
