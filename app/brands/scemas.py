from pydantic import BaseModel, ConfigDict


class BrandBase(BaseModel):
    name: str


class BrandCreate(BrandBase):
    pass


class BrandUpdate(BrandBase):
    pass


class BrandUpdatePartial(BrandBase):
    name: str | None = None


class Brand(BrandBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
