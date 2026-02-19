from src.models import TractorsOrm, BrandsOrm
from src.repositories.mappers.base import DataMapper
from src.schemas.brands import Brand
from src.schemas.tractors import Tractor


class TractorMapper(DataMapper):
    db_model = TractorsOrm
    schema=Tractor


class BrandsMapper(DataMapper):
    db_model = BrandsOrm
    schema=Brand