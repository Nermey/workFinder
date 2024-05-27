from database import session, engine, Base
from sqlalchemy import select
from models import AuthDB


class Auth_obj:
    @staticmethod
    async def create_table():
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    @staticmethod
    async def add_new_user(email, password):
        async with session() as conn:
            user_obj = AuthDB(email=email, password=password)
            conn.add(user_obj)
            await conn.commit()

    @staticmethod
    async def check_user_exist(email):
        async with session() as conn:
            query = select(AuthDB).filter_by(email=email)
            res = await conn.execute(query)
            user = res.first()
            return user is None

    @staticmethod
    async def authentication(email, password):
        async with session() as conn:
            query = select(AuthDB).filter_by(email=email, password=password)
            res = await conn.execute(query)
            user = res.scalars().all()
            #user_dto = [UserDTO.model_validate(row, from_attributes=True) for row in user]
            #return [len(user) != 0, user_dto[0].id]
            return len(user) != 0

    @staticmethod
    async def change_email(user_id, new_email):
        async with session() as conn:
            user = await conn.get(AuthDB, user_id)
            user.email = new_email
            await conn.commit()

    @staticmethod
    async def change_password(user_id, new_password):
        async with session() as conn:
            user = await conn.get(AuthDB, user_id)
            user.password = new_password
            await conn.commit()
