from pydantic import BaseModel,Field,ConfigDict

class BrandAddRequest(BaseModel):
    horse_power:int = Field(ge=30,le=120)
    quantity:int


class BrandAdd(BaseModel):
    tractor_id:int
    horse_power:int = Field(ge=30,le=120)
    quantity: int

class Brand(BrandAdd):
    id:int

    model_config = ConfigDict(from_attributes=True)

class BrandPatchRequest(BaseModel):
    horse_power:int | None = None
    quantity: int | None = None

class BrandPatch(BaseModel):
    tractor_id:int | None = None
    horse_power:int | None = None
    quantity: int | None = None




