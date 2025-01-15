from pydantic import BaseModel, ConfigDict, Field
from typing import Annotated


class BrandBase(BaseModel):
    name: Annotated[str, Field(..., min_length=1, max_length=20)]


class BrandCreate(BrandBase):
    pass


class BrandUpdate(BrandBase):
    pass


class BrandUpdatePartial(BrandBase):
    name: str | None = None


class Brand(BrandBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
