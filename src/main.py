from parser import VacansyParsers


vp = VacansyParsers()

err, res = vp.get_all_vacansy_dev('./vacancy_5.json')

if err:
    print(err)
else:

    for vac in res['vacancies'][:10]:
        keys = vac.keys()

        for k in keys:
            print(k)
            print('__________________________________________')
            print('{} тип {}'.format(vac[k], type(vac[k])))
            print('__________________________________________')
            print('\n')
        
        print('\n\n')