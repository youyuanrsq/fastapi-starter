from passlib.context import CryptContext
from sqlalchemy import select

from src.auth.models import User
from src.auth.schemas import UserInDB

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


async def get_user(db, username: str):
    user: User = (
        (await db.execute(select(User).filter(User.username == username)))
        .scalars()
        .first()
    )

    if user is None:
        return None

    return UserInDB(
        username=user.username,
        disabled=user.is_del,
        hashed_password=user.hashed_password,
    )
