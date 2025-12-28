import sys
import logging
import threading
import time

from fastapi import FastAPI, HTTPException, Query
from metadata_api import DESCRIPTION, TAG_DISTRICTS,\
TAGS_METADATA, TITEL, SUMMARY, VERSION, TAG_VACANSY

from db import Vacansy, DbController
from parser import DISTRICTS, DistrictModel, VacansyParsers

logging.basicConfig(
    level=logging.INFO,
    filename="api_log.log",
    filemode="a",
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

dbCon = DbController(
    'pgadmin',
    'Bi>wu84w',
    'vacansy',
    'localhost',
    3333
)

vp = VacansyParsers()

err = dbCon.create_engine()

if err:
    logging.error('create_engin : {}'.format(err))
    sys.exit()

logging.info('create_engin success')


def get_vacansy_from_open_data():
    """Получить вакансии с open data"""

    err, res = vp.get_all_vacansy()

    json = res.json()

    if err:
        logging.error('get_vacansy_from_open_data : {}'.format(err))
        return
    
    err, filter_vacancies = vp.filter_vacansy_in_districs(json['vacancies'])

    if err:
        logging.error('filter_vacansy_in_districs : {}'.format(err))
        return
    
    err = dbCon.delete_all_vacancies()

    if err:
        logging.error('delete_all_vacancies : {}'.format(err))
        return
    
    for fv in filter_vacancies:
        err = dbCon.create_vacansy_from_dict(fv)

        if err:
            logging.error('create_vacansy_from_dict : vacansy : {}  err : {}'
                          .format(fv, err))
            
    logging.info('get_vacansy_from_open_data : success to get vacansy from open data')


def start_background_task():
    """Запусти фоновую задачу"""
    def worker():
        logger = logging.getLogger(__name__)
        logger.info('Фоновый поток запущен')
        while True:
            get_vacansy_from_open_data()
            time.sleep(60)

    thread = threading.Thread(target=worker, daemon=True)
    thread.start()
    logging.info('Background Task for get vacansy is start')


app = FastAPI(
    title=TITEL,
    summary=SUMMARY,
    description=DESCRIPTION,
    version=VERSION,
    openapi_tags=TAGS_METADATA
)


start_background_task()

@app.get('/vacansy/districts/{district_id}', response_model=list[Vacansy], tags=[TAG_VACANSY])
def get_vacansies_from_districts(
    district_id: int,
    offset: int=0,
    limit: int = Query(default=100, le=100),
    salary_min: int = 0,
    salary_max: int  = 99999999,
    vacancy_name: int | None = None
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
            salary_min=str(salary_min),
            salary_max=str(salary_max),
            vacancy_name=vacancy_name,
            limit=limit,
            offset=offset
        )

        if not err:
            logging.info('get_vacansies_from_districts {} : vacansy from district by id {}'
                         .format(200, district_id))
            return vacancies
        else:
            logging.error('get_vacansies_from_districts {} : err when get vacansy {}'
                          .format(400, err))
            return HTTPException(
                status_code=400,
                detail=f'Ошибка при получения вакансий из базы {err}'
            )
    else:
        logging.error('get_vacansies_from_districts {} : not found district by {}'
                      .format(404, district_id))
        return HTTPException(
            status_code=404,
            detail=f'Не нашел район/город по его {district_id}'
        )

    
@app.delete('/vacansy/delete/', tags=[TAG_VACANSY])
def delete_all_vacansy():
    """Удалить все вакансии из базы"""
    err = dbCon.delete_all_vacancies()
    if not err:
        logging.info('delete_all_vacansy {}'.format(200))
        return {'message': 'Все вакансии из базы удалены'}
    else:
        logging.info('delete_all_vacansy {} : {}'
                      .format(400, err))
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
            logging.info('get_districts_with_work_places {} : {}'
                         .format(400, err))
            raise HTTPException(
                status_code=400,
                detail=f'Ошибка во время получения вакансий с addressCode = ${ac.code}'
            )

    logging.info('get_districts_with_work_places {}'
                 .format(200))
    return addresses_code_with_vacansy