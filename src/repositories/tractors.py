from sqlalchemy import select,func

from src.repositories.base import BaseRepository
from src.models import TractorsOrm

class TractorsRepository(BaseRepository):
    model = TractorsOrm

    async def get_all_filtered(
        self,
        model: str | None,
        horse_power: int | None,
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
                TractorsOrm.horse_power == horse_power
            )

        query = query.limit(limit).offset(offset)

        result = await self.session.execute(query)
        return result.scalars().all()