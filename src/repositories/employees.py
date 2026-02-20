from sqlalchemy import select

from src.models import EmployeesOrm
from src.repositories.base import BaseRepository
from sqlalchemy.ext.asyncio import AsyncSession
from src.repositories.mappers.base import DataMapper
from src.repositories.mappers.mapper import EmployeesMapper
from src.schemas.employees import EmployeesAdd, EmployeePatch


class EmployeesRepository(DataMapper):
    model = EmployeesOrm
    mapper = EmployeesMapper

    async def add(self, data: EmployeesAdd) -> EmployeesOrm:
        employee = EmployeesOrm(**data.model_dump())
        self.session.add(employee)
        await self.session.flush()
        return employee

    # READ ONE
    async def get_one(self, employee_id: int) -> EmployeesOrm | None:
        result = await self.session.execute(
            select(EmployeesOrm).where(EmployeesOrm.id == employee_id)
        )
        return result.scalar_one_or_none()

    # READ ALL
    async def get_all(self) -> list[EmployeesOrm]:
        result = await self.session.execute(select(EmployeesOrm))
        return result.scalars().all()

    # UPDATE (PATCH)
    async def update(
            self,
            employee_id: int,
            data: EmployeePatch
    ) -> EmployeesOrm | None:
        employee = await self.get_one(employee_id)
        if not employee:
            return None

        for key, value in data.model_dump(exclude_unset=True).items():
            setattr(employee, key, value)

        await self.session.flush()
        return employee

    async def deactivate(self, employee_id: int) -> bool:
        employee = await self.get_one(employee_id)
        if not employee:
            return False

        employee.is_active = False
        await self.session.flush()
        return True