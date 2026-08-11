from typing import Literal

from pydantic import BaseModel, ConfigDict, Field


class Expense(BaseModel):
    model_config = ConfigDict(strict=True)

    id: int
    car_id: int = Field(alias="carId")
    reported_at: str = Field(alias="reportedAt")
    mileage: int
    liters: int
    total_cost: int = Field(alias="totalCost")


class ExpenseResponse(BaseModel):
    model_config = ConfigDict(strict=True)

    status: Literal["ok"]
    data: Expense


class Car(BaseModel):
    model_config = ConfigDict(strict=True)

    id: int
    car_brand_id: int = Field(alias="carBrandId")
    car_model_id: int = Field(alias="carModelId")
    mileage: int


class CarResponse(BaseModel):
    model_config = ConfigDict(strict=True)

    status: Literal["ok"]
    data: Car


class StatusResponse(BaseModel):
    model_config = ConfigDict(strict=True)

    status: Literal["ok"]
