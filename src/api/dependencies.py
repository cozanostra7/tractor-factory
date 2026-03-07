from typing import Annotated
from fastapi import Depends,Query,HTTPException
from pydantic import BaseModel
from starlette import status

from src.models import EmployeeRole
from src.services.auth import AuthService
from src.utils.db_manager import DBManager
from starlette.requests import Request
from src.database import async_session_maker
from src.schemas.employees import Employees





class Pagination_params(BaseModel):
    page: Annotated[int | None , Query(1, description='page', gt=0, lt=100)]
    per_page:Annotated[int | None , Query(None)]



PaginationDep = Annotated[Pagination_params,Depends()]


def get_token(request: Request) -> str:
    token = request.cookies.get('access_token', None)
    if not token:
        raise HTTPException(status_code=401,detail='You are not authorized')
    return token

def get_current_user_id(token: str = Depends(get_token)) -> int:
    data = AuthService().decode_token(token)
    return data['user_id']


UserIDDep = Annotated[int,Depends(get_current_user_id)]


def get_db_manager():
    return DBManager(session_factory=async_session_maker)


async def get_db():
    async with get_db_manager() as db:
        yield db


async def get_department_or_404(
    department_id: int,
    db: DBManager = Depends(get_db)
):
    department = await db.departments.get_one_or_none(id=department_id)
    if not department:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Department with id {department_id} not found"
        )
    return department


async def get_employee_or_404(
    employee_id: int,
    db: DBManager = Depends(get_db)
):

    employee = await db.employees.get_one_or_none(id=employee_id)
    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with id {employee_id} not found"
        )
    return employee


DBDep = Annotated[DBManager,Depends(get_db)]