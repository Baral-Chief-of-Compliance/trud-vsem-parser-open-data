from typing import Optional, Dict, Any, Union

from sqlmodel import create_engine,\
SQLModel, Session, delete, select
from sqlalchemy import func

from .models import *
from .keys import KEYS_WICH_TURN_TO_STR, KEYS_WICH_TURN_TO_MANY_KEYS,\
KEYS_WICH_TURN_TO_MANY_KEYS_IN_LIST


class DbController(object):
    """Класс для взаимодействия с базо данных"""

    ip : str
    port : int
    username : str
    password : str
    db_name : str

    def __init__(
            self,
            username : str,
            password : str,
            db_name : str,
            ip:str ='localhost',
            port:int ='5432'
            ):
        self.username = username
        self.password = password
        self.db_name = db_name
        self.ip = ip
        self.port = port

    def create_engine(self) -> Optional[Exception]:
        """Создать Engine для работы с базой данных postgresql"""
        try:
            self.engine = create_engine(
                'postgresql://{}:{}@{}:{}/{}'.format(
                    self.username,
                    self.password,
                    self.ip,
                    self.port,
                    self.db_name
                ))
            
            return None
        except Exception as ex:
            return ex
            
    def create_db_and_tables(self) -> Optional[Exception]:
        """Создание таблиц"""
        try:
            SQLModel.metadata.create_all(self.engine)
            return None
        except Exception as ex:
            return ex
        

    def delete_all_vacancies(self) -> Optional[Exception]:
        """Удалить все вакансии из таблицы"""
        try:
            with Session(self.engine) as session:
                session.exec(delete(Vacansy))
                session.commit()
            
            return None
        except Exception as ex:
            return ex
        

    def create_vacansy_from_dict(self, vacansy_dict: Dict[str, Any]) -> Optional[Exception]:
        """Добаить в базу вакансию с помощбю словаря"""
        try:
            copy_vacansy_dict = vacansy_dict.copy()

            for k in KEYS_WICH_TURN_TO_STR:
                if k in vacansy_dict:
                    if isinstance(vacansy_dict[k], list):
                        if len(vacansy_dict[k]) > 0:
                            if isinstance(vacansy_dict[k][0], dict):
                                copy_vacansy_dict[k] = ''.join(str(item) for item in vacansy_dict[k])
                        else:
                            copy_vacansy_dict[k] = ', '.join(vacansy_dict[k])
                    elif isinstance(vacansy_dict[k], dict):
                        copy_vacansy_dict[k] = str(vacansy_dict[k])
                    elif isinstance(vacansy_dict[k], str):
                        copy_vacansy_dict[k] = vacansy_dict[k]
                    else:
                        copy_vacansy_dict[k] = 'Отсутсвуют'


            for k in KEYS_WICH_TURN_TO_MANY_KEYS.keys():
                if k in vacansy_dict:
                    del copy_vacansy_dict[k]
                    inside_keys = KEYS_WICH_TURN_TO_MANY_KEYS[k]
                    inside_values = vacansy_dict[k]

                    for ik in inside_keys:
                        if ik in inside_values:
                            copy_vacansy_dict[ik] = inside_values[ik]

            for k in KEYS_WICH_TURN_TO_MANY_KEYS_IN_LIST.keys():
                if k in vacansy_dict:
                    del copy_vacansy_dict[k]
                    inside_keys = KEYS_WICH_TURN_TO_MANY_KEYS_IN_LIST[k]
                    inside_values = vacansy_dict[k][0]

                    for ik in inside_keys:
                        if ik in inside_values:
                            copy_vacansy_dict[ik] = inside_values[ik]

            vacansy = Vacansy(**copy_vacansy_dict)



            with Session(self.engine) as session:
                session.add(vacansy)
                session.commit()

            return None
        except Exception as ex:
            return ex
        
    def get_count_work_place(self, min_code: int, max_code: int) -> Union[Optional[Exception], int]:
        """Получить количество рабочих мест в выбранном городе или районе"""
        vacansy_count : int = 0
        try:
            with Session(self.engine) as session:
                statement = select(Vacansy).where(
                    Vacansy.addressCode >= min_code,
                    Vacansy.addressCode <= max_code
                )

                res = session.exec(statement)
                vacancies = res.all()

                for v in vacancies:
                    vacansy_count += v.workPlaces
            
            return None, vacansy_count
        
        except Exception as ex:
            return ex, vacansy_count
        
    def get_vacancies_between_address_codes(
            self, 
            min_code: int,
            max_code: int,
            limit: int,
            offset: int = 0) ->  Union[Optional[Exception], list[Vacansy]]:
        """Получить вакансии с района/города по его id"""
        try:
            with Session(self.engine) as session:
                vacancies = session.exec(
                    select(Vacansy).where(
                    Vacansy.addressCode >= min_code,
                    Vacansy.addressCode <= max_code
                ).order_by(Vacansy.vacancyName).offset(offset).limit(limit)).all()
                return None, vacancies
        except Exception as ex:
            return ex, []
