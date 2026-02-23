from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from app.db.session import engine, Base
from app.api.routes import router

app = FastAPI()

#registro api
app.include_router(router)

#templates
templates = Jinja2Templates(directory="app/templates")

#HTML
@app.get("/")
def home(request: Request):

    return templates.TemplateResponse(
        "index.html",
        {"request": request}
    )


#crear tabla info covid al iniciar
Base.metadata.create_all(bind=engine)