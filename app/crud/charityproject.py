from typing import Optional

from fastapi.encoders import jsonable_encoder

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql.expression import false

from app.crud.base import CRUDBase
from app.models import CharityProject


class CRUDCharityProject(CRUDBase):
    async def update(
            self,
            db_obj,
            obj_in,
            session: AsyncSession,
    ):
        obj_data = jsonable_encoder(db_obj)
        update_data = obj_in.dict(exclude_unset=True)

        for field in obj_data:
            if field in update_data:
                setattr(db_obj, field, update_data[field])
        session.add(db_obj)
        await session.commit()
        await session.refresh(db_obj)
        return db_obj

    async def remove(
            self,
            db_obj,
            session: AsyncSession,
    ):
        await session.delete(db_obj)
        await session.commit()
        return db_obj

    async def get_project_id_by_name(
        self,
        project_name: str,
        session: AsyncSession,
    ) -> Optional[int]:
        project_id = await session.execute(
            select(CharityProject.id).where(
                CharityProject.name == project_name
            )
        )
        return project_id.scalars().first()

    async def get_project_invested_amount(
        self,
        project_id: int,
        session: AsyncSession,
    ) -> Optional[int]:
        invested_amount = await session.execute(
            select(CharityProject.invested_amount).where(
                CharityProject.id == project_id
            )
        )
        return invested_amount.scalars().first()

    async def get_project_status(
        self,
        project_id: int,
        session: AsyncSession,
    ) -> bool:
        status = await session.execute(
            select(CharityProject.fully_invested).where(
                CharityProject.id == project_id
            )
        )
        return status.scalars().first()

    async def get_open_project(
        self,
        session: AsyncSession,
    ) -> CharityProject:
        project = await session.execute(
            select(CharityProject)
            .where(CharityProject.fully_invested == false())
            .order_by(CharityProject.create_date)
        )
        return project.scalars().first()


charityproject_crud = CRUDCharityProject(CharityProject)
