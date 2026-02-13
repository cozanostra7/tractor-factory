from fastapi import Body,Query,APIRouter


router = APIRouter(prefix='/tractors',tags=['Tractors'])

@router.get('')
async def show_tractors(
        pagination:PaginationDep,
        db:DBDep,
        model:str|None = Query(None,description='Model of the tractor'),
        horse_power:str|None = Query(None,description='Power of the tractor'),
):
    per_page = pagination.per_page or 5
    return await