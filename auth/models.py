from sqlalchemy.orm import Mapped, mapped_column
from database import Base


class AuthDB(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    password: Mapped[str]
    type: Mapped[str]
