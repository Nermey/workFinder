from sqlalchemy.orm import Mapped, mapped_column
from database import Base


class UsersAuth(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    password: Mapped[str]


class CompanyAuth(Base):
    __tablename__ = "company"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
