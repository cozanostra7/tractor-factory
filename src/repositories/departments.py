from sqlalchemy import select, func
from sqlalchemy.orm import selectinload

from src.models import DepartmentsOrm, EmployeesOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mapper import DepartmentsMapper


class DepartmentRepository(BaseRepository):
    model = DepartmentsOrm
    mapper = DepartmentsMapper

    async def get_with_employees(self, department_id: int):

        query = (
            select(self.model)
            .options(selectinload(self.model.employees))
            .filter_by(id=department_id)
        )
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def get_all_with_employee_count(self):
        query = (
            select(
                self.model,
                func.count(EmployeesOrm.id).label('employee_count')
            )
            .outerjoin(EmployeesOrm, self.model.id == EmployeesOrm.department_id)
            .group_by(self.model.id)
        )
        result = await self.session.execute(query)
        return result.all()

    async def get_by_name(self, name: str):
        query = select(DepartmentsOrm)
        if name:
            query = query.filter(
                func.lower(DepartmentsOrm.name)
                .contains(name.strip().lower())
            )
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def get_active_employees_count(self, department_id: int) -> int:
        query = (
            select(func.count())
            .select_from(EmployeesOrm)
            .filter_by(department_id=department_id, is_active=True)
        )
        result = await self.session.execute(query)
        return result.scalar_one()