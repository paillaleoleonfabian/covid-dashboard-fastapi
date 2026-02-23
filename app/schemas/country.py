from pydantic import BaseModel
from pydantic import BaseModel, ConfigDict


class CountryBase(BaseModel):

    country: str
    continent: str | None

    cases: int | None
    deaths: int | None
    recovered: int | None
    active: int | None
    population: int | None
    last_updated: int | None

    flag: str | None


class CountryResponse(CountryBase):

    id: int

    model_config = ConfigDict(from_attributes=True)