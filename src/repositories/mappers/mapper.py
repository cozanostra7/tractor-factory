from src.models import TractorsOrm, BrandsOrm, DepartmentsOrm
from src.repositories.mappers.base import DataMapper
from src.schemas.brands import Brand
from src.schemas.departments import Department
from src.schemas.employees import Employees
from src.schemas.tractors import Tractor


class TractorMapper(DataMapper):
    db_model = TractorsOrm
    schema=Tractor


class BrandsMapper(DataMapper):
    db_model = BrandsOrm
    schema=Brand

class DepartmentsMapper(DataMapper):
    db_model = DepartmentsOrm
    schema = Department

class EmployeesMapper(DataMapper):
    db_model = DepartmentsOrm
    schema = Employees
