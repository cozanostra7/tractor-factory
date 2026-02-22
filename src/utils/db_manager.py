
from src.repositories.tractors import TractorsRepository
from src.repositories.brands import BrandsRepository
from src.repositories.departments import DepartmentRepository
from src.repositories.employees import EmployeesRepository


class DBManager:

    def __init__(self,session_factory):
        self.session_factory = session_factory

    async def __aenter__(self):
        self.session = self.session_factory()
        self.tractors = TractorsRepository(self.session)
        self.brands = BrandsRepository(self.session)
        self.departments = DepartmentRepository(self.session)
        self.employees = EmployeesRepository(self.session)



        return self

    async def __aexit__(self,*args):
        await self.session.rollback()
        await self.session.close()


    async def commit(self):
        await self.session.commit()