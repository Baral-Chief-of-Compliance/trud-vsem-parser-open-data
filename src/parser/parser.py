import requests
from typing import Optional, Tuple

from .data import TRUD_VSEM_SEVER_ZAPAD_JSON_URL
from .proxy import ProxySetting

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