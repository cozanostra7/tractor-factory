from fastapi import Body,Query,APIRouter
from src.api.dependencies import PaginationDep, DBDep
from src.schemas.tractors import TractorAdd, Tractor_patch

router = APIRouter(prefix='/tractors',tags=['Tractors'])

@router.get('')
async def show_tractors(
        pagination:PaginationDep,
        db:DBDep,
        brand:str|None = Query(None,description='Model of the tractor'),
):
    per_page = pagination.per_page or 5
    return await db.tractors.get_all_filtered(
        brand = brand,
        limit=per_page,
        offset=per_page * (pagination.page - 1)
    )


@router.get('/{tractor_id}')
async def get_tractors(tractor_id: int, db: DBDep):
        return await db.tractors.get_one_or_none(
            id=tractor_id)


@router.post('')
async def create_tractors(db:DBDep,tractor_info:TractorAdd = Body
    (openapi_examples=
     {'1':{'summary':'Tractors.Write the brand name ONLY!','value':{
    'brand':'Lovol',
}}})):

        tractor = await db.tractors.add(tractor_info)
        await db.commit()
        return {'status': 'Ok',"data":tractor}

@router.put('/{tractor_id}')
async def edit_tractors(tractor_id:int,tractor_info:TractorAdd,db:DBDep):
    await db.tractors.edit(tractor_info,id=tractor_id)
    await db.commit()
    return {'status':'Ok'}

@router.patch('/tractor_id')
async def edit_single_info_tractor(tractor_id:int,tractor_info:Tractor_patch,db:DBDep):
    await db.tractors.edit(tractor_info,partially_edited=True,id=tractor_id)
    await db.commit()
    return {'status': 'Ok'}


@router.delete('')
async def delete_tractor(tractor_id:int,db:DBDep):
    await db.tractors.delete(id=tractor_id)
    await db.commit()
    return {'status':'Ok'}
