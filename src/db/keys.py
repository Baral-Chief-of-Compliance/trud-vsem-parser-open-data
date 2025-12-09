KEYS_WICH_TURN_TO_STR : list = [
    'languageKnowledge',
    'skills',
    'shift',
    'hardSkills',
    'softSkills',
    'requiredDriveLicense'
]


KEYS_WICH_TURN_TO_MANY_KEYS : dict[str, list] = {
    'workPlace': [
        'workPlaceForeign',
        'workPlaceOrdinary',
        'workPlaceQuota',
        'workPlaceSpecial'
    ],
    'geo': [
        'latitude',
        'longitude'
    ],
    'educationRequirements': [
        'educationType'
    ],
    'company': [
        'companyCode',
        'url',
        'inn',
        'kpp',
        'ogrn'
    ],
}

KEYS_WICH_TURN_TO_MANY_KEYS_IN_LIST : dict[str: list] = {
        'contactList': [
        'contactType',
        'contactValue',
        'isModerated',
        'isPreferred'
    ]
}