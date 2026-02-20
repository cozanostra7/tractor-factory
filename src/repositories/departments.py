from src.models import DepartmentsOrm
from src.repositories.base import BaseRepository
from src.repositories.mappers.mapper import DepartmentsMapper


class DepartmentRepository(BaseRepository):
    model = DepartmentsOrm
    mapper = DepartmentsMapper

