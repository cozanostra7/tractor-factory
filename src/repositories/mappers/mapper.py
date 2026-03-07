from src.models import TractorsOrm, BrandsOrm, DepartmentsOrm, EmployeesOrm
from src.models.users import UsersOrm
from src.repositories.mappers.base import DataMapper
from src.schemas.brands import Brand
from src.schemas.departments import Department
from src.schemas.employees import Employees
from src.schemas.tractors import Tractor
from src.schemas.users import User


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
    db_model = EmployeesOrm
    schema = Employees

class UsersMapper(DataMapper):
    db_model = UsersOrm
    schema = User
