from pydantic import BaseModel,Field,ConfigDict

class DepartmentAdd(BaseModel):
    name: str
    description:str |None=None

class Department(DepartmentAdd):
    id:int

    model_config = ConfigDict(from_attributes=True)

class DepartmentPatch(BaseModel):
    name: str | None = None
    description: str | None = None

