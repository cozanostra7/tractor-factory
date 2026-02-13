from pydantic import BaseModel, Field,ConfigDict


class TractorAdd(BaseModel):
    model:str
    horse_power:str


class Tractor(TractorAdd):
    id:int

    model_config = ConfigDict(from_attributes=True)


class Tractor_patch(BaseModel):
    model: str | None = Field(None),
    horse_power: str | None = Field(None)