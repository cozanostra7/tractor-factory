from src.database import Base
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import ForeignKey, func, DateTime, String


class TractorsOrm(Base):
    __tablename__ ='tractors'

    id: Mapped[int] = mapped_column(primary_key=True)
    model: Mapped[str] = mapped_column(String(100))
    horse_power:Mapped[int]