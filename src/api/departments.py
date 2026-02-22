from fastapi import APIRouter, Depends, HTTPException, status, Query, Body

from src.api.dependencies import get_db, get_department_or_404, DBDep
from src.schemas.departments import (
    Department,
    DepartmentAdd,
    DepartmentPatch,
    DepartmentWithStats,
)
from src.schemas.employees import EmployeeListItem


router = APIRouter(prefix="/departments", tags=["Departments"])

@router.get('', response_model=list[DepartmentWithStats])
async def show_departments(db: DBDep):
    departments = await db.departments.get_all_with_employee_count()
    return [
        DepartmentWithStats(
            id=dept.id,
            name=dept.name,
            description=dept.description,
            employee_count=employee_count
        )
        for dept, employee_count in departments
    ]


@router.get("/search", response_model=DepartmentWithStats)
async def search_department_by_name(db:DBDep,
        name: str = Query(..., description="Department name to search")
):
    department = await db.departments.get_by_name(name)

    if not department:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Department with name '{name}' not found"
        )

    employee_count = await db.departments.get_active_employees_count(department.id)

    return DepartmentWithStats(
        id=department.id,
        name=department.name,
        description=department.description,
        employee_count=employee_count
    )


@router.get('/{departments_id}',response_model=DepartmentWithStats)
async def show_a_department_by_id(db:DBDep,department_id:int):
    department = await get_department_or_404(department_id, db)
    employee_count = await db.departments.get_active_employees_count(department_id)
    return DepartmentWithStats(
        id=department.id,
        name=department.name,
        description=department.description,
        employee_count=employee_count
    )



@router.post("",  status_code=status.HTTP_201_CREATED)
async def create_department(
        db: DBDep,
        department_data: DepartmentAdd = Body(),
):
    existing = await db.departments.get_by_name(department_data.name)
    if existing:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Department '{department_data.name}' already exists"
        )

    department = await db.departments.add(department_data)
    await db.commit()

    return {'status': 'Ok', "data": department}