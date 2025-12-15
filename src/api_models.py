from pydantic import BaseModel


class AddressCode(BaseModel):
    """Модель для кодов райнов/городов Мурманской области"""
    code : str
    name: str


class AddressCodeVacansyCount(BaseModel):
    """Модель для кодов райнов/городов Мурманской области с кол-во вакансий в базе"""
    code: str
    name: str
    vacansy_count: int = 0


class DistrictModel(BaseModel):
    """Модель района/города Мурманской области"""
    id : int
    name: str
    min_code: int
    max_code: int
    work_places : int = 0