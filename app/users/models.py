from sqlalchemy.orm import Mapped, mapped_column

from db.database import Base, str_uniq


class User(Base):
    username: Mapped[str_uniq]
    email: Mapped[str_uniq]
    password: Mapped[str]
    is_superuser: Mapped[bool] = mapped_column(default=False)
    is_active: Mapped[bool] = mapped_column(default=True)