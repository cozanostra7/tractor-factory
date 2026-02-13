from src.models import TractorsOrm
from src.repositories.mappers.base import DataMapper
from src.schemas.tractors import Tractor


class TractorMapper(DataMapper):
    db_model = TractorsOrm
    schema=Tractor