from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload
from src.models import EmployeesOrm, EmployeeRole
from src.repositories.mappers.base import DataMapper
from src.repositories.mappers.mapper import EmployeesMapper
from src.repositories.base import BaseRepository


class EmployeesRepository(BaseRepository):
    model = EmployeesOrm
    mapper = EmployeesMapper
    db_model = EmployeesOrm
    schema = EmployeesMapper.schema



    async def get_with_department(self, employee_id: int):
        query = (
            select(self.model)
            .options(selectinload(self.model.department))
            .filter_by(id=employee_id)
        )
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def get_by_department(self, department_id: int, active_only: bool = True):
        filters = {"department_id": department_id}
        if active_only:
            filters["is_active"] = True
        return await self.get_all(**filters)

    async def get_by_role(self, role: EmployeeRole, active_only: bool = True):
        filters = {"role": role}
        if active_only:
            filters["is_active"] = True
        return await self.get_all(**filters)

    async def get_by_position(self, position: str, active_only: bool = True):
        filters = {"position": position}
        if active_only:
            filters["is_active"] = True
        return await self.get_all(**filters)

    async def deactivate(self, employee_id: int):
        return await self.edit(
            {"is_active": False},
            id=employee_id
        )

    async def activate(self, employee_id: int):
        return await self.edit(
            {"is_active": True},
            id=employee_id
        )

    async def get_all_with_departments(self, active_only: bool = True):
        query = select(self.model).options(selectinload(self.model.department))

        if active_only:
            query = query.filter_by(is_active=True)

        result = await self.session.execute(query)
        return result.scalars().all()

    async def search_by_name(self, name: str, active_only: bool = True):
        query = select(self.model).filter(
            self.model.full_name.ilike(f"%{name}%")
        )

        if active_only:
            query = query.filter_by(is_active=True)

        result = await self.session.execute(query)
        return result.scalars().all()