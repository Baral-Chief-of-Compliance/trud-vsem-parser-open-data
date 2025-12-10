import sys

from fastapi import FastAPI
from sqlmodel import Session, select
from metadata_api import DESCRIPTION, TAG_VACANSY,\
TAGS_METADATA, TITEL, SUMMARY, VERSION

from db import Vacansy, DbController


dbCon = DbController(
    'pgadmin',
    'Bi>wu84w',
    'vacansy',
    'localhost',
    3333
)

err = dbCon.create_engine()

if err:
    print(err)
    sys.exit()

app = FastAPI(
    title=TITEL,
    summary=SUMMARY,
    description=DESCRIPTION,
    version=VERSION,
    openapi_tags=TAGS_METADATA
)

@app.get("/vacansy/", response_model=list[Vacansy], tags=[TAG_VACANSY])
def get_all_vacansy():
    """Получить все вакансии из базы"""
    with Session(dbCon.engine) as session:
        vacansys = session.exec(select(Vacansy)).all()
        return vacansys
