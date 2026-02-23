from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.config import settings
from app.schemas.country import CountryResponse
from app.schemas.refresh import RefreshRequest, RefreshResponse
import requests

from app.api.deps import get_db
from app.models.country import CountryCovid

router = APIRouter(prefix="/api")

@router.get("/countries",response_model=list[CountryResponse])
def get_countries(db: Session = Depends(get_db)):

    return db.query(CountryCovid).all()

@router.post("/countries/refresh",response_model=RefreshResponse)
def refresh_countries(
    request: RefreshRequest,
    db: Session = Depends(get_db)
):

    url = settings.COVID_API_URL
    response = requests.get(url)
    data = response.json()
    inserted = 0
    updated = 0

    for item in data:

        if item.get("continent") != request.continent:
            continue

        name = item["country"]

        record = (
            db.query(CountryCovid)
            .filter(CountryCovid.country == name)
            .first()
        )

        if record:
            record.cases = item.get("cases")
            record.deaths = item.get("deaths")
            record.recovered = item.get("recovered")
            record.active = item.get("active")
            record.population = item.get("population")
            record.last_updated = item.get("updated")

            if item.get("countryInfo"):
                record.flag = item["countryInfo"].get("flag")

            updated += 1

        else:

            new = CountryCovid(
                country=name,
                continent=item.get("continent"),
                cases=item.get("cases"),
                deaths=item.get("deaths"),
                recovered=item.get("recovered"),
                active=item.get("active"),
                population=item.get("population"),
                last_updated=item.get("updated"),
                flag=(
                    item["countryInfo"].get("flag")
                    if item.get("countryInfo")
                    else None
                )
            )

            db.add(new)
            inserted += 1

    db.commit()

    return {
        "received": len(data),
        "inserted": inserted,
        "updated": updated
    }

