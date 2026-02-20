from datetime import datetime

from pydantic import BaseModel,Field,ConfigDict

class EmployeesAdd(BaseModel):
    full_name: str
    position:str
    salary:int
    department_id: int

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