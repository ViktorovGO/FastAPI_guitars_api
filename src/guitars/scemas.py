from pydantic import BaseModel, ConfigDict, Field
from typing import Annotated


class GuitarBase(BaseModel):
    article: Annotated[str, Field(..., min_length=1, max_length=20)]
    brand_id: Annotated[int, Field(ge=0)]
    title: Annotated[str, Field(..., min_length=1, max_length=100)]
    price: Annotated[int, Field(ge=0)]


class GuitarCreate(GuitarBase):
    pass

class GuitarUpdate(GuitarBase):
    pass


class GuitarUpdatePartial(GuitarBase):
    article: str | None = None
    brand_id: Annotated[int, Field(ge=0)] | None = None
    title: str | None = None
    price: Annotated[int, Field(ge=0)] | None = None


class Guitar(GuitarBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
