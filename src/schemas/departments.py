from pydantic import BaseModel,Field,ConfigDict
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.schemas.employees import Employees

class DepartmentAdd(BaseModel):
    name: str
    description:str |None=None

class Department(DepartmentAdd):
    id:int

    model_config = ConfigDict(from_attributes=True)

class DepartmentPatchRequest(BaseModel):
    name: str | None = Field(None, max_length=100)
    description: str | None = Field(None, max_length=300)

class DepartmentPatch(BaseModel):
    name: str | None = None
    description: str | None = None


class DepartmentWithStats(Department):
    employee_count: int = Field(description="Number of employees in department")


class DepartmentWithEmployees(Department):
    employees: list["Employees"] = Field(default_factory=list)


from src.schemas.employees import Employees
DepartmentWithEmployees.model_rebuild()
