from datetime import datetime
import enum
from src.database import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey, DateTime, Boolean, Numeric, func, Enum, text


class EmployeeRole(str, enum.Enum):
    ADMIN = "admin"
    HR = "hr"
    LOGISTICS = "logistics"
    PRODUCTION = "production"
    QA = "qa"
    EMPLOYEE = "employee"


class EmployeesOrm(Base):
    __tablename__ = 'employees'

    id:Mapped[int] = mapped_column(primary_key=True)
    full_name:Mapped[str] = mapped_column(String(100),nullable=False)
    position:Mapped[str] = mapped_column(String(100),nullable=False)
    salary:Mapped[float] = mapped_column(Numeric(10,2),nullable=False)
    department_id:Mapped[int] = mapped_column(ForeignKey('departments.id',ondelete='CASCADE'),nullable=False)
    hired_at:Mapped[datetime] = mapped_column(DateTime,server_default=text("CURRENT_TIMESTAMP"))
    is_active: Mapped[bool] = mapped_column(Boolean,default=True,nullable=False)
    department: Mapped["DepartmentsOrm"] = relationship(back_populates="employees")

    role: Mapped[EmployeeRole] = mapped_column(
        Enum(EmployeeRole),
        default=EmployeeRole.EMPLOYEE
    )
