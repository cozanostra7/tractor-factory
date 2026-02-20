from datetime import datetime

from src.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, DateTime, Boolean, Numeric

from src.models import DepartmentsOrm


class EmployeesOrm(Base):
    __tablename__ = 'employees'

    id:Mapped[int] = mapped_column(primary_key=True)
    full_name:Mapped[str] = mapped_column(String(100),nullable=False)
    position:Mapped[str] = mapped_column(String(100),nullable=False)
    salary:Mapped[float] = mapped_column(Numeric(10,2),nullable=False)
    department_id:Mapped[int] = mapped_column(ForeignKey('departments.id',ondelete='CASCADE'),nullable=False)
    hired_at:Mapped[datetime] = mapped_column(DateTime,default=datetime.now)
    is_active: Mapped[bool] = mapped_column(Boolean,default=True,nullable=False)
    department: Mapped["DepartmentsOrm"] = relationship(back_populates="employees")
