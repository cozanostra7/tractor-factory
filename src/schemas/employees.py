from datetime import datetime
from typing import TYPE_CHECKING
from pydantic import BaseModel, Field, ConfigDict, field_validator

from src.models import EmployeeRole

if TYPE_CHECKING:
    from src.schemas.departments import Department

class EmployeesAdd(BaseModel):
    full_name: str
    position:str
    salary:int
    department_id: int
    role: EmployeeRole = Field(default=EmployeeRole.EMPLOYEE, description="Employee role")

    @field_validator('salary')
    @classmethod
    def validate_salary(cls, v):
        if v < 0:
            raise ValueError('Salary must be positive')
        return round(v, 2)

class Employees(EmployeesAdd):
    id:int
    hired_at:datetime
    is_active: bool

    model_config = ConfigDict(from_attributes=True)

class EmployeePatch(BaseModel):
    full_name: str | None = None
    position: str | None = None
    salary: float | None = None
    department_id: int | None = None
    is_active: bool | None = None

    @field_validator('salary')
    @classmethod
    def validate_salary(cls, v):
        if v is not None and v < 0:
            raise ValueError('Salary must be positive')
        return round(v, 2) if v is not None else None


class EmployeesWithDepartment(Employees):

    department: "Department"


class EmployeeListItem(BaseModel):

    id: int
    full_name: str
    position: str
    department_id: int
    is_active: bool
    role: EmployeeRole

    model_config = ConfigDict(from_attributes=True)


# Import after class definitions
from src.schemas.departments import Department

EmployeesWithDepartment.model_rebuild()