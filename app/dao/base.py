from typing import Union, Optional, Sequence

from sqlalchemy import update as sqlalchemy_update 
from sqlalchemy import delete as sqlalchemy_delete
from sqlalchemy import func
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession


from db.sessions import connection
from db.database import Base


class BaseDAO:
    model: Optional[Base]

    @classmethod
    @connection
    async def find_one_or_none(cls, *, session: AsyncSession, **filter_by) -> Union[Base, None]:
        query = select(cls.model).filter_by(**filter_by)
        result = await session.execute(query)
        return result.scalar_one_or_none()
    
    @classmethod
    @connection
    async def find_all(cls, *, session: AsyncSession, **filter_by) -> Sequence[Base]:
        query = select(cls.model).filter_by(**filter_by)
        result = await session.execute(query)
        return result.scalars().all()
    
    @classmethod
    @connection
    async def add(cls, *, session: AsyncSession, **data) -> None:
        new_instance = cls.model(**data)
        session.add(new_instance)
    
    @classmethod
    @connection
    async def delete(cls, *, session: AsyncSession, **delete_by) -> None:
        query = sqlalchemy_delete(cls.model).where(
            func.and_(*[getattr(cls.model, k) == v for k, v in delete_by.items()])
        )
        await session.execute(query)
    
    @classmethod
    @connection
    async def update(cls, *, session: AsyncSession, filter_by: dict, update_data: dict) -> None:
        query = (
            sqlalchemy_update(cls.model)
            .where(func.and_(*[getattr(cls.model, k) == v for k, v in filter_by.items()]))
            .values(**update_data)
        )
        await session.execute(query)
