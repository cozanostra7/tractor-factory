from typing import Annotated
from fastapi import Depends,Query,HTTPException
from pydantic import BaseModel
from src.utils.db_manager import DBManager
from starlette.requests import Request
from src.database import async_session_maker








class Pagination_params(BaseModel):
    page: Annotated[int | None , Query(1, description='page', gt=0, lt=100)]
    per_page:Annotated[int | None , Query(None)]



PaginationDep = Annotated[Pagination_params,Depends()]







def get_db_manager():
    return DBManager(session_factory=async_session_maker)


async def get_db():
    async with get_db_manager() as db:
        yield db



DBDep = Annotated[DBManager,Depends(get_db)]