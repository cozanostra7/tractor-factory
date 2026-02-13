from sqlalchemy import select,func

from repositories.base import BaseRepository
from src.models import TractorsOrm


class HotelsRepository(BaseRepository):
    model = TractorsOrm


    async def get_all(
            self,
            model,
            horse_power,
            limit,
            offset,):
        query = select(TractorsOrm)
        if model:
            query = query.filter(func.lower(TractorsOrm.model).contains(model.strip().lower()))
        if horse_power:
            query = query.filter(func.lower(TractorsOrm.horse_power).contains(horse_power.strip().lower()))
        query = (
            query
            .limit(limit)
            .offset(offset ))
        print(query.compile(compile_kwargs={"literal_binds": True}))
        result = await self.session.execute(query)

        return result.scalars().all()