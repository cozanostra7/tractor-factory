from src.database import Base
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import String


class DepartmentsOrm(Base):
    __tablename__ = 'departments'

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100),nullable=False,unique=True)
    description:Mapped[str] = mapped_column(String(300))

