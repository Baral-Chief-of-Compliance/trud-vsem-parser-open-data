from typing import Optional

from sqlmodel import Field, SQLModel

class Vacansy(SQLModel, table=True):
    """Модель Вакансий в базе данных"""
    id : str = Field(default=None, primary_key=True)
    stateRegionCode : str = Field(default='Отсутствует')
    vacancyName : str = Field(default='Отсутствует')
    codeProfessionalSphere : str = Field(default='Отсутствует')
    professionalSphereName : str = Field(default='Отсутствует')
    vacancyAddress : str = Field(default='Отсутствует')
    vacancyAddressAdditionalInfo : str = Field(default='Отсутствует')
    salary : str = Field(default='Отсутствует')
    salaryMin : int = Field(default=0)
    salaryMax : int = Field(default=999999)
    socialProtecteds : str = Field(default='Отсутствует')
    languageKnowledge : str = Field(default='Отсутствует') #по данным с вакансиям, тут приходит list, но нам нужно сюда отпралвять строку просто с языками через ,
    busyType : str = Field(default='Отсутствует')
    skills : str = Field(default='Отсутствует') #аналогично, как с languageKnowledge, также строка с навыками через ,
    #ключи с workPlace
    workPlaceForeign : Optional[bool] = Field(default=None)
    workPlaceOrdinary : Optional[bool] = Field(default=None)
    workPlaceQuota : Optional[bool] = Field(default=None)
    workPlaceSpecial : Optional[bool] = Field(default=None)
    #конец workPlace

    trainingDays : int = Field(default=0)
    shift : str = Field(default='Отсутствует')  #аналогично, как с languageKnowledge, также строка с смежность или че через , хз я не понял
    hardSkills : str = Field(default='Отсутствует') #аналогично, как с languageKnowledge, также строка через ,
    softSkills : str = Field(default='Отсутствует') #аналогично, как с languageKnowledge, также строка через ,
    experienceRequirements : int = Field(default=0)
    scheduleType : str = Field(default='Отсутствует')
    careerPerspective : bool = Field(default=False)
    codeExternalSystem : str = Field(default='Отсутствует')
    needMedcard : str = Field(default='Отсутствует')
    sourceType : str = Field(default='Отсутствует')
    requiredDriveLicense : str = Field(default='Отсутствует')  #аналогично, как с languageKnowledge, также строка через ,
    changeTime : str = Field(default='Отсутствует')
    contactPerson : str = Field(default='Отсутствует')
    fullCompanyName : str = Field(default='Отсутствует')
    companyBusinessSize : str = Field(default='Отсутствует')
    dateModify : str = Field(default='Отсутствует')
    workPlaces : int = Field(default=1)
    isUzbekistanRecruitment : bool = Field(default=False)
    federalDistrictCode : int 
    datePublished : str = Field(default='Отсутствует')
    accommodationCapability : bool = Field(default=False)
    foreignWorkersCapability : bool = Field(default=False)
    isQuoted : bool = Field(default=False)
    creationDate : str = Field(default='Отсутствует')
    responsibilities : str = Field(default='Отсутствует')
    addressCode : str = Field(default='Отсутствует')
    regionName : str = Field(default='Отсутствует')
    status : str = Field(default='Отсутствует')
    vacancyUrl : str = Field(default='Отсутствует')
    #ключи с geo
    latitude : Optional[float] = Field(default=0.0)
    longitude : Optional[float] = Field(default=0.0)
    #конец ключей с geo

    #ключи с educationRequirements
    educationType : str = Field(default='Отсутствует')
    #конец ключей с educationRequirements (но не факт)

    # есть такой ключи premium там идет {} хз зачем там

    #ключи с company
    companyCode : str = Field(default='Отсутствует')
    url : str = Field(default='Отсутствует')
    inn : str = Field(default='Отсутствует')
    kpp : str = Field(default='Отсутствует')
    ogrn : str = Field(default='Отсутствует')
    #конец ключей с company

    isModerated : Optional[bool] = Field(default=None)
    deleted : Optional[bool] = Field(default=None)
    visibility : str = Field(default='Отсутствует')

    #ключи с contactList
    contactType : str = Field(default='Отсутствует')
    contactValue : str = Field(default='Отсутствует')
    isModerated : Optional[bool] = Field(default=None)
    isPreferred : Optional[bool] = Field(default=None)
    #конец ключей с contactList