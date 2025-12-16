from pydantic import BaseModel


class DistrictModel(BaseModel):
    """Модель района/города Мурманской области"""
    id : int
    name: str
    min_code: int
    max_code: int
    work_places : int = 0