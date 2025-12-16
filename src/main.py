import sys

from parser import VacansyParsers
from db import DbController, Vacansy

from address_code import ADDRESSES_CODES
from api_models import AddressCodeVacansyCount

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

# err = dbCon.create_db_and_tables()

# if err:
#     print(err)
#     sys.exit()


# err = dbCon.delete_all_vacancies()
# if err:
#     print(err)
#     sys.exit()

vp = VacansyParsers()

err, res = vp.get_all_vacansy_dev('./vacancy_5.json')

if err:
    print(err)
    sys.exit()


vacansy_count : int = 0
work_place : int = 0
murmansk_region_vacansy_count : int = 0
murmansk_region_work_place : int = 0

address_with_work_palce : list[AddressCodeVacansyCount] = []
for ac in ADDRESSES_CODES:
    address_with_work_palce.append(
        AddressCodeVacansyCount(
            code=ac.code,
            name=ac.name,
            vacansy_count=0
        )
    )


murmansks_code = {}


for vac in res['vacancies']:

    for ac in address_with_work_palce:
        if vac['addressCode'] == ac.code:
            ac.vacansy_count += vac['workPlaces']

    if vac['stateRegionCode'] == '5100000000000':
        murmansk_region_vacansy_count += 1
        murmansk_region_work_place += vac['workPlaces']
        if vac['addressCode'] in murmansks_code:
            murmansks_code[vac['addressCode']]['work_place'] += vac['workPlaces']
        else:
            murmansks_code[vac['addressCode']] = {
                'work_place' : vac['workPlaces'],
                'vacancyAddress' : vac['vacancyAddress']
            }

    if vac['addressCode'] == '5100000100000':
        vacansy_count += 1
        work_place += vac['workPlaces']


print(murmansk_region_vacansy_count)
print(murmansk_region_work_place)
print(vacansy_count)
print(work_place)

for ac in address_with_work_palce:
    print('код {} наименование {} кол-во рабочих мест {}'.format(
        ac.code,
        ac.name,
        ac.vacansy_count
    ))


vacansy_witch_code_from_dict : int = 0
print('\n\nКоды котрые я нашел в мурманской области')
for k in murmansks_code.keys():
    print('код {}, адресс {} кол-во рабочих мест {}'.format(
        k,
        murmansks_code[k]['vacancyAddress'],
        murmansks_code[k]['work_place']
    ))
    vacansy_witch_code_from_dict += murmansks_code[k]['work_place']

print('\nКол-во рабочих мест из этих кодов {}'.format(vacansy_witch_code_from_dict))
print('При этом всего кодов, которые находятся в Мурманске 5100000000000 {}'.format(len(murmansks_code.keys())))
print('Кол-во рабочих мест по коду 5100000000000 {}'.format(murmansk_region_work_place))

print('\n\n\nСейчас отсортирую все коды МО')
for k in sorted(murmansks_code.keys()):
    print('{} ---- {}'.format(k, murmansks_code[k]['vacancyAddress']))



print('\n\n\n\n')
print('Проверка работы фильтра')

err, filter_vacancies = vp.filter_vacansy_in_districs(
    res['vacancies']
)

if err:
    print(err)
    sys.exit()

# print(filter_vacancies)
print(len(filter_vacancies))


for fv in filter_vacancies:
    err = dbCon.create_vacansy_from_dict(fv)

    if err:
        print(err)
        sys.exit()