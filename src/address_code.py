from api_models import AddressCode, DistrictModel

ADDRESSES_CODES = [
    AddressCode(code='5100000100000', name='Мурманск'),
    AddressCode(code='5100000600000', name='Мончегорск'),
    AddressCode(code='5100100100000', name='Кандалакша'),
    AddressCode(code='5100500000000', name='Печенгский район'),
    AddressCode(code='5100000200000', name='Апатиты'),
    AddressCode(code='5100000500000', name='Кировск'),
    AddressCode(code='5100000300000', name='Заозерск'),
    AddressCode(code='5100500200000', name='Заполярный'),
    AddressCode(code='5100001300000', name='Снежногорск'),
    AddressCode(code='5100000700000', name='Оленегорск'),
    AddressCode(code='5100001200000', name='Гаджиево'),
    AddressCode(code='5100300100000', name='Кола'),
    AddressCode(code='5100200100000', name='Ковдор'),
    AddressCode(code='5100600000000', name='Терский район')
]

DISTRICTS = [
    DistrictModel(
        id=0,
        name='Мурманск',
        min_code=51000001000000000,
        max_code=51000001999999999,
        work_places=0,
    ),
    DistrictModel(
        id=1,
        name='Видяево',
        min_code=51000000004000000,
        max_code=51000000004999999,
        work_places=0
    ),
    DistrictModel(
        id=2,
        name='Апатиты',
        min_code=51000002000000000,
        max_code=51000002999999999,
        work_places=0,
    ),
    DistrictModel(
        id=3,
        name='Заозерск',
        min_code=51000003000000000,
        max_code=51000003999999999,
        work_places=0
    ),
    DistrictModel(
        id=4,
        name='Кировск',
        min_code=51000005000000000,
        max_code=51000005999999999,
        work_places=0
    ),
    DistrictModel(
        id=5,
        name='Мончегорск',
        min_code=51000006000000000,
        max_code=51000006999999999,
        work_places=0
    ),
    DistrictModel(
        id=6,
        name='Оленегорск',
        min_code=51000007000000000,
        max_code=51000007999999999,
        work_places=0
    ),
    DistrictModel(
        id=7,
        name='Островной',
        min_code=51000008000000000,
        max_code=51000008999999999,
        work_places=0
    ),
    DistrictModel(
        id=8,
        name='Полярные Зори',
        min_code=51000009000000000,
        max_code=51000009999999999,
        work_places=0
    ),
    DistrictModel(
        id=9,
        name='Полярный',
        min_code=51000010000000000,
        max_code=51000019999999999,
        work_places=0
    ),
    DistrictModel(
        id=10,
        name='Североморск',
        min_code=51000011000000000,
        max_code=51000011999999999,
        work_places=0
    ),
    DistrictModel(
        id=11,
        name='Гаджиево',
        min_code=51000012000000000,
        max_code=51000012999999999,
        work_places=0
    ),
]