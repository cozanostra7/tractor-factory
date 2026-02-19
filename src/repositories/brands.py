from sqlalchemy import select,func

from src.repositories.base import BaseRepository
from src.models import BrandsOrm
from src.repositories.mappers.mapper import BrandsMapper


class BrandsRepository(BaseRepository):
    model = BrandsOrm
    mapper = BrandsMapper


    async def get_all_filtered(
        self,
        tractor_id:int | None,
        horse_power: int | None,
        quantity:int | None

    ):
        query = select(BrandsOrm).filter(BrandsOrm.tractor_id==tractor_id)

        if horse_power is not None:
            query = query.filter(BrandsOrm.horse_power==horse_power)

        if quantity is not None:
            query = query.filter(BrandsOrm.quantity==quantity)


        result = await self.session.execute(query)
        return result.scalars().all()