from typing import Optional, Tuple

from sqlmodel import create_engine, SQLModel


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