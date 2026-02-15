from sqlalchemy import select,func

from src.repositories.base import BaseRepository
from src.models import TractorsOrm
from src.repositories.mappers.mapper import TractorMapper


class TractorsRepository(BaseRepository):
    model = TractorsOrm
    mapper = TractorMapper


    async def get_all_filtered(
        self,
        brand: str | None,
        limit: int,
        offset: int,
    ):
        query = select(TractorsOrm)

        if brand:
            query = query.filter(
                func.lower(TractorsOrm.brand)
                .contains(brand.strip().lower())
            )

        query = query.limit(limit).offset(offset)

        result = await self.session.execute(query)
        return result.scalars().all()