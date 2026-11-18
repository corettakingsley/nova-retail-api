
from pydantic import BaseModel, ConfigDict, Field
from decimal import Decimal


class ProductBase(BaseModel):
    name: str = Field(min_length=2, max_length=150)
    description: str | None = None
    price: Decimal = Field(gt=0, max_digits=10, decimal_places=2)
    stock_quantity: int = Field(default=0, ge=0)
    category_id: int | None = None
    image_url: str | None = Field(default=None, max_length=500)


class ProductCreate(ProductBase):
    pass


class ProductUpdate(ProductBase):
    pass


class ProductResponse(ProductBase):
    id: int
    is_active: bool

    model_config = ConfigDict(from_attributes=True)
