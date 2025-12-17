import sys

from fastapi import FastAPI, HTTPException, Query
from metadata_api import DESCRIPTION, TAG_DISTRICTS,\
TAGS_METADATA, TITEL, SUMMARY, VERSION, TAG_VACANSY

from db import Vacansy, DbController
from parser import DISTRICTS, DistrictModel

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


@app.get('/vacansy/districts/{district_id}', response_model=list[Vacansy], tags=[TAG_VACANSY])
def get_vacansies_from_districts(
    district_id: int,
    offset: int=0,
    limit: int = Query(default=100, le=100)
    ):
    """Получить все вакансии из района/города МО по его district_id"""
    find_district : bool = False

    district : DistrictModel
    for d in DISTRICTS:
        if d.id == district_id:
            district = d
            find_district = True
            break
    if find_district:
        err, vacancies = dbCon.get_vacancies_between_address_codes(
            district.min_code,
            district.max_code,
            limit=limit,
            offset=offset
        )

        if not err:
            return vacancies
        else:
            return HTTPException(
                status_code=400,
                detail=f'Ошибка при получения вакансий из базы {err}'
            )
    else:
        return HTTPException(
            status_code=404,
            detail=f'Не нашел район/город по его {district_id}'
        )

    
@app.delete('/vacansy/delete/', tags=[TAG_VACANSY])
def delete_all_vacansy():
    """Удалить все вакансии из базы"""
    err = dbCon.delete_all_vacancies()
    if not err:
        return {'message': 'Все вакансии из базы удалены'}
    else:
        raise HTTPException(
            status_code=400,
            detail='Ошибка при удалении всех вакансий из базы'
        )
    

@app.get('/districts/', response_model=list[DistrictModel], tags=[TAG_DISTRICTS])
def get_districts_with_work_places():
    """Получить районы и города Мурманской области c кол-во рабочих мест"""
    addresses_code_with_vacansy : list[DistrictModel] = DISTRICTS.copy()

    for ac in addresses_code_with_vacansy:
        err, ac.work_places = dbCon.get_count_work_place(
            min_code = ac.min_code,
            max_code = ac.max_code
        )
        if err:
            raise HTTPException(
                status_code=400,
                detail=f'Ошибка во время получения вакансий с addressCode = ${ac.code}'
            )

    return addresses_code_with_vacansy