from functools import wraps

from sqlalchemy.ext.asyncio import async_sessionmaker

from db.database import engine


async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

def connection(func=None, commit: bool = False):
    if func is None:
        return lambda f: connection(f, commit=commit)

    @wraps(func)
    async def wrapper(*args, **kwargs):
        async with async_session_maker() as session:
            try:
                result = await func(*args, session=session, **kwargs)
                if commit:
                    await session.commit()
                return result
            except Exception as e:
                await session.rollback()
                raise e 
            finally:
                await session.close()
    return wrapper