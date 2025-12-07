class ProxySetting(object):
    """Класс для данных прокси"""
    port : int = 0
    proxy_ip : str = ''
    username : str = ''
    password : str = ''
    use_https : bool = False

    def __init__(
            self, 
            port : int, 
            proxy_ip : str, 
            username : str ="", 
            password : str ="",
            use_https: bool = False
            ):
        self.port = port
        self.proxy_ip = proxy_ip
        self.username = username
        self.password = password
        self.use_https = use_https


    def get_http_proxy(self) -> str:
        """Возращает строку http://username:password@your_proxy_ip:port - если были переданы логин и пароль
        Иначе http://your_proxy_ip:port"""
        if self.username and self.password:
            return 'http://{}:{}@{}:{}'.format(
                self.username,
                self.password,
                self.proxy_ip,
                self.port
            )
        else:
            return 'http://{}:{}'.format(
                self.proxy_ip,
                self.port
            )
    
    def get_https_proxy(self) -> str:
        """Возращает строку https://username:password@your_proxy_ip:port - если были переданы логин и пароль
        Иначе https://your_proxy_ip:port"""

        http_proxy : str = self.get_http_proxy()
        return http_proxy[:4:]
    
    
    def get_proxy_for_requests(self) -> dict:
        """Получить словарь для proxy в пакете requests
        {
            "http": ...,
            "https": ...
        }
        """
        http_proxy_url : str = self.get_http_proxy()
        https_proxy_url : str = self.get_https_proxy() if self.use_https else self.get_http_proxy()

        return {
            "http" : http_proxy_url,
            "https" : https_proxy_url
        }