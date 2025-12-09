import sys

from parser import VacansyParsers
from db import DbController, Vacansy

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

err = dbCon.create_db_and_tables()

if err:
    print(err)
    sys.exit()


err = dbCon.delete_all_vacancies()
if err:
    print(err)
    sys.exit()

vp = VacansyParsers()

err, res = vp.get_all_vacansy_dev('./vacancy_5.json')

if err:
    print(err)
    sys.exit()

for vac in res['vacancies']:
    err = dbCon.create_vacansy_from_dict(vac)
    if err:
        print(err)
        sys.exit()
        
print('\n\n')
print(len(res['vacancies']))