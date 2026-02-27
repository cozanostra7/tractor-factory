from http import HTTPStatus
from sys import prefix

from fastapi import APIRouter, status, Query, Body, Depends
from src.api.dependencies import DBDep, get_department_or_404, get_employee_or_404
from src.schemas.employees import (EmployeesAdd,
                                   Employees,
                                   EmployeePatch,
                                   EmployeesWithDepartment,
                                   EmployeeListItem,
                                   EmployeeRole)


router = APIRouter(prefix='/employees',tags=['Employees'])

@router.get('',response_model=list[EmployeeListItem])
async def get_all_employees(db:DBDep,active_only:bool=Query(description='Return only active employees'),
                            department_id:int|None=Query(None,description='filter by department'),
                            role:EmployeeRole|None=Query(None,description='filter by role')):
    if department_id:
        employees = await db.employees.get_by_department(department_id, active_only)
    elif role:
        employees = await db.employees.get_by_role(role,active_only)
    else:
        employees = await db.employees.get_all_employees(active_only)


    return employees

@router.post('',response_model=Employees,status_code=status.HTTP_201_CREATED)
async def hire_employee(db:DBDep,employee_data:EmployeesAdd):
    await get_department_or_404(employee_data.department_id,db)
    employee = await db.employees.add(employee_data)
    await db.commit()