from fastapi import Query, Body, APIRouter, HTTPException
from starlette import status
from fastapi_cache.decorator import cache
from src.api.dependencies import DBDep
from src.schemas.brands import BrandAddRequest, BrandAdd, BrandPatch, BrandPatchRequest

router = APIRouter(prefix='/tractors',tags=['Brands'])


@router.get('/{tractor_id}/brands')
@cache(expire=10)
async def show_all_brands(
        db:DBDep,
        tractor_id:int|None,
        ):
    return await db.brands.get_all_filtered(
        horse_power=None,
        quantity=None,
        tractor_id=tractor_id
    )

@router.get('/{tractor_id}/brands/{brand_id}')
@cache(expire=10)
async def get_brand(tractor_id:int,brand_id:int,db:DBDep):
    return await db.brands.get_one_or_none(id=brand_id,tractor_id=tractor_id)

@router.post('/{tractor_id}/brands')
async def produce_tractors(db:DBDep,tractor_id:int,brand_info:BrandAddRequest = Body
    (openapi_examples=
     {'1': {'summary': 'Brands. Write quantity and horse power only!', 'value': {
         'horse_power': 100,
         'quantity':10
     }}})):
    _brand_info = BrandAdd(tractor_id=tractor_id,**brand_info.model_dump())
    brand = await db.brands.add(_brand_info)
    await db.commit()
    return {'status': 'Ok', "data": brand}

@router.put('/{tractor_id}/brands/{brand_id}')
async def edit_brands(tractor_id:int,brand_id:int,
                      brand_info:BrandAddRequest,db:DBDep):
    _brand_info = BrandAdd(tractor_id=tractor_id,**brand_info.model_dump())
    await db.brands.edit(_brand_info,id=brand_id)
    await db.commit()
    return {'status':'Ok'}

@router.patch('/{tractor_id}/brands/{brand_id}')
async def partially_edit(tractor_id:int,brand_id:int,brand_info:BrandPatchRequest,db:DBDep):
    existing = await db.brands.get_one_or_none(id=brand_id)
    if not existing:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Brand with id {brand_id} in tractor with ID {tractor_id} not found"
        )
    _brand_info_dict = brand_info.model_dump(exclude_unset=True)
    _brand_info = BrandPatch(tractor_id=tractor_id,**_brand_info_dict)
    await db.brands.edit(_brand_info,partially_edited=True,id=brand_id,tractor_id=tractor_id)
    await db.commit()
    return {'status': 'Ok'}


@router.delete('/{tractor_id}/brands/{brand_id}')
async def delete_brand(db:DBDep,tractor_id:int,brand_id:int):
    await db.brands.delete(id=brand_id,tractor_id=tractor_id)
    await db.commit()
    return {'status': 'Ok'}



