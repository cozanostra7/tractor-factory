from fastapi import APIRouter, status, Query, Body, Depends, HTTPException
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

@router.get('/search')
async def search_employees(db:DBDep,
                           name:str = Query(...,min_length=2,description='Search by name'),
                           active_only:bool=Query(True)):

    employees = await db.employees.search_by_name(name,active_only)
    return {'status': 'Ok','data':employees}

@router.get('/{employee_id}')
async def get_single_employee(db:DBDep,employee_id:int):
    employee = await db.employees.get_with_department(employee_id)

    if not employee:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Employee with ID {employee_id} not found'
        )
    return {'status': 'Ok', 'data': employee}


@router.post('',response_model=Employees,status_code=status.HTTP_201_CREATED)
async def hire_employee(db:DBDep,employee_data:EmployeesAdd):
    await get_department_or_404(employee_data.department_id,db)
    employee = await db.employees.add(employee_data)
    await db.commit()

    return employee


@router.patch('/{employee_id}', response_model=Employees)
async def partially_edit_employee(
        employee_id: int,
        employee_info: EmployeePatch,
        db: DBDep
):

    existing = await db.employees.get_one_or_none(id=employee_id)
    if not existing:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Employee with id {employee_id} not found"
        )

    update_data = employee_info.model_dump(exclude_unset=True)
    if not update_data:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="No fields to update"
        )
    if "department_id" in update_data:
        await get_department_or_404(update_data["department_id"], db)


    await db.employees.edit(employee_info, partially_edited=True, id=employee_id)
    await db.commit()

    updated = await db.employees.get_one_or_none(id=employee_id)
    return updated

@router.post('/{employee_id}/deactivate')
async def deactivate_employee(db:DBDep,employee_id:int):
    existing = await db.employees.get_one_or_none(id=employee_id)
    if not existing:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Employee with ID {employee_id} not found'
        )
    await db.employees.deactivate(employee_id)
    await db.commit()

    employee = await db.employees.get_one_or_none(id=employee_id)
    return employee
