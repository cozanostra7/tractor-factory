from src.database import Base
from sqlalchemy.orm import Mapped,mapped_column
from sqlalchemy import ForeignKey,String,func

class BrandsOrm(Base):
    __tablename__ = 'brands'

    id : Mapped[int] = mapped_column(primary_key=True)
    tractor_id:Mapped[int] = mapped_column(ForeignKey('tractors.id'))
    horse_power:Mapped[int]
    quantity:Mapped[int]
