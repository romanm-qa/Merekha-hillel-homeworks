from pydantic import BaseModel, ConfigDict, Field


class Car(BaseModel):
    model_config = ConfigDict(strict=True)

    brand: str = Field(min_length=1)
    year: int = Field(ge=1886)
    engine_volume: float = Field(ge=0)
    price: int = Field(gt=0)
