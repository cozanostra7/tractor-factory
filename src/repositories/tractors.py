from sqlalchemy import select,func

from src.repositories.base import BaseRepository
from src.models import TractorsOrm
from src.repositories.mappers.mapper import TractorMapper


class TractorsRepository(BaseRepository):
    model = TractorsOrm
    mapper = TractorMapper


    async def get_all_filtered(
        self,
        model: str | None,
        horse_power: str | None,
        limit: int,
        offset: int,
    ):
        query = select(TractorsOrm)

        if model:
            query = query.filter(
                func.lower(TractorsOrm.model)
                .contains(model.strip().lower())
            )

        if horse_power:
            query = query.filter(
                func.lower(TractorsOrm.horse_power)
                .contains(model.strip().lower())
            )

        query = query.limit(limit).offset(offset)

        result = await self.session.execute(query)
        return result.scalars().all()