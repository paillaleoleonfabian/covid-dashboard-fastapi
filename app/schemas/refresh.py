from pydantic import BaseModel

# recibe
class RefreshRequest(BaseModel):

    continent: str

# devuelve
class RefreshResponse(BaseModel):

    received: int
    inserted: int
    updated: int