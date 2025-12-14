import sys

from fastapi import FastAPI, HTTPException
from sqlmodel import Session, select
from metadata_api import DESCRIPTION, TAG_VACANSY,\
TAGS_METADATA, TITEL, SUMMARY, VERSION,\
TAG_ADDRESS

from db import Vacansy, DbController
from api_models import AddressCode, AddressCodeVacansyCount
from address_code import ADDRESSES_CODES


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

@app.get('/vacansy/', response_model=list[Vacansy], tags=[TAG_VACANSY])
def get_all_vacansy():
    """Получить все вакансии из базы"""
    with Session(dbCon.engine) as session:
        vacansys = session.exec(select(Vacansy)).all()
        return vacansys
    

@app.delete('/vacansy/delete/', tags=[TAG_VACANSY])
def delete_all_vacansy():
    """Удалить все вакансии из базы"""
    err = dbCon.delete_all_vacancies()
    if err:
        return {'message': 'Все вакансии из базы удалены'}
    else:
        raise HTTPException(
            status_code=400,
            detail='Ошибка при удалении всех вакансий из базы'
        )
    

@app.get('/addresses/', response_model=list[AddressCode], tags=[TAG_ADDRESS])
def get_all_addresses():
    """Получить адреса и коды городов и районов Мурманской области"""
    return ADDRESSES_CODES


@app.get('/addresses/vacansy-count/', response_model=list[AddressCodeVacansyCount], tags=[TAG_ADDRESS])
def get_all_addresse_with_vacansy_count():
    """Получить адреса и коды городов и районов Мурманской области c кол-во Вакансий"""
    addresses_code_with_vacansy : list[AddressCodeVacansyCount] = []
    for ac in ADDRESSES_CODES:
        err, vacansy_count = dbCon.get_count_vacansy(ac.code)

        if err:
            raise HTTPException(
                status_code=400,
                detail=f'Ошибка во время получения вакансий с addressCode = ${ac.code}'
            )
        else:
            addresses_code_with_vacansy.append(
                AddressCodeVacansyCount(
                    code=ac.code,
                    name=ac.name,
                    vacansy_count=vacansy_count
                )
            )

    return addresses_code_with_vacansy