from fastapi import Body,Query,APIRouter
from src.api.dependencies import PaginationDep, DBDep
from src.schemas.tractors import TractorAdd

router = APIRouter(prefix='/tractors',tags=['Tractors'])

@router.get('')
async def show_tractors(
        pagination:PaginationDep,
        db:DBDep,
        model:str|None = Query(None,description='Model of the tractor'),
        horse_power:str|None = Query(None,description='Power of the tractor'),
):
    per_page = pagination.per_page or 5
    return await db.tractors.get_all_filtered(
        model = model,
        horse_power=horse_power,
        limit=per_page,
        offset=per_page * (pagination.page - 1)
    )


@router.get('/{tractor_id}')
async def get_hotel(tractor_id: int, db: DBDep):
        return await db.tractors.get_one_or_none(
            id=tractor_id)


@router.post('')
async def create_tractors(db:DBDep,hotel_info:TractorAdd = Body
    (openapi_examples=
     {'1':{'summary':'Tractors','value':{
    'model':'Lovol',
    'horse_power':'1000'
}}})):

        tractor = await db.tractors.add(hotel_info)
        await db.commit()
        return {'status': 'Ok',"data":tractor}
