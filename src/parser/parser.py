import os
import json
from typing import Optional, Tuple

import requests

from .data import TRUD_VSEM_SEVER_ZAPAD_JSON_URL
from .proxy import ProxySetting
from .districts import DISTRICTS


class RequestError(Exception):
    """Класс исключения для всех ошибок запросов"""
    def __init__(self, message: str, url: str = None, status_code: int = None):
        self.message = message
        self.url = url
        self.status_code = status_code
        super().__init__(self.message)

    def __str__(self):
        base = f"RequestError: {self.message}"
        if self.url:
            base += f" (URL: {self.url})"
        if self.status_code:
            base += f" (Status: {self.status_code})"
        return base


class VacansyParsers(object):
    """Класс для парсинга вакансий с открытых данных trud-vsem.ru"""

    parser_url : str = TRUD_VSEM_SEVER_ZAPAD_JSON_URL
    proxy : ProxySetting = None

    def __init__(
            self, 
            proxy : ProxySetting = None,
            parser_url : str = TRUD_VSEM_SEVER_ZAPAD_JSON_URL
            ):
        self.proxy = proxy
        self.parser_url = parser_url

    def get_all_vacansy_dev(self, data_path: str = '') -> Tuple[Optional[Exception], Optional[dict]]:
        """Метод для получения всез вакансий НО С ФАЙЛА, который скачен
        с opendata trudvsem, на вход идет путь до файла формата json"""

        if os.path.isfile(data_path):
            try:
                with open(data_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    file.close()

                return None, data
            except Exception as ex:
                return ex, None
        else:
            ex = Exception('file on {} is not found'.format(data_path))
            return ex, None


    def get_all_vacansy(self) -> Tuple[Optional[Exception], Optional[requests.Response]]:
        """Метод для получения всех вакансий по parser_url"""
        response : requests.Response

        try:
            if self.proxy:
                response = requests.get(
                    url=self.parser_url,
                    proxies=self.proxy.get_proxy_for_requests()
                )
            else:
                response = requests.get(
                    url=self.parser_url
                )
        except Exception as ex:
            return ex, None
        
        if response.status_code != 200:
            ex = RequestError(
                "Request to {}".format(self.parser_url), 
                self.parser_url, 
                response.status_code
                )
            return ex, None

        else:
            return None, response
        
    def filter_vacansy_in_districs(self, vacancies: list) -> Tuple[Optional[Exception], list]:
        """Отфилтровать полученный вакансии, и возваращает list с вакансиями под наши районы,
        единственный нюанс, что наш фильтр превращает addressCode строкове в int
        """
        filter_vacancies : list = []

        try:
            for v in vacancies:
                for d in DISTRICTS:
                    addressCode : int = 0
                    
                    if len(v['addressCode']) < 17:
                        need_zero : int = 17 - len(v['addressCode'])
                        intermediateСode : str = v['addressCode']

                        for z in range(need_zero):
                            intermediateСode += '0'
                        
                        addressCode = int(intermediateСode)

                    elif len(v['addressCode']) == 17:
                        addressCode = int(v['addressCode'])


                    if d.min_code <= addressCode <= d.max_code:
                        v['addressCode'] = addressCode
                        filter_vacancies.append(v)
                        break

            return None, filter_vacancies
        
        except Exception as ex:
            return ex, filter_vacancies


        



