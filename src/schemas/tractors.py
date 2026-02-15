from pydantic import BaseModel, Field,ConfigDict


class TractorAdd(BaseModel):
    brand:str


class Tractor(TractorAdd):
    id:int

    model_config = ConfigDict(from_attributes=True)


class Tractor_patch(BaseModel):
    brand: str | None = Field(None),