from sqlmodel import Field, SQLModel

class Vacansy(SQLModel, table=True):
    """Модель Вакансий в базе данных"""
    id : str = Field(default=None, primary_key=True)
    stateRegionCode : str 
    vacancyName : str 
    codeProfessionalSphere : str 
    professionalSphereName : str 
    vacancyAddress : str 
    vacancyAddressAdditionalInfo : str 
    salary : str 
    salaryMin : int = Field(default=0)
    salaryMax : int = Field(default=999999)
    socialProtecteds : str 
    languageKnowledge : str  #по данным с вакансиям, тут приходит list, но нам нужно сюда отпралвять строку просто с языками через ,
    busyType : str 
    skills : str  #аналогично, как с languageKnowledge, также строка с навыками через ,
    #ключи с workPlace
    workPlaceForeign : bool 
    workPlaceOrdinary : bool 
    workPlaceQuota : bool 
    workPlaceSpecial : bool 
    #конец workPlace

    trainingDays : int = Field(default=0)
    shift : str  #аналогично, как с languageKnowledge, также строка с смежность или че через , хз я не понял
    hardSkills : str  #аналогично, как с languageKnowledge, также строка через ,
    softSkills : str  #аналогично, как с languageKnowledge, также строка через ,
    experienceRequirements : int = Field(default=0)
    scheduleType : str 
    careerPerspective : bool = Field(default=False)
    codeExternalSystem : str 
    needMedcard : str 
    sourceType : str 
    requiredDriveLicense : str  #аналогично, как с languageKnowledge, также строка через ,
    changeTime : str 
    contactPerson : str 
    fullCompanyName : str 
    companyBusinessSize : str 
    dateModify : str 
    workPlaces : int = Field(default=1)
    isUzbekistanRecruitment : bool = Field(default=False)
    federalDistrictCode : int 
    datePublished : str 
    accommodationCapability : bool = Field(default=False)
    foreignWorkersCapability : bool = Field(default=False)
    isQuoted : bool = Field(default=False)
    creationDate : str 
    responsibilities : str 
    addressCode : str 
    regionName : str 
    status : str 
    vacancyUrl : str 
    #ключи с geo
    latitude : float 
    longitude : float 
    #конец ключей с geo

    #ключи с educationRequirements
    educationType : str 
    #конец ключей с educationRequirements (но не факт)

    # есть такой ключи premium там идет {} хз зачем там

    #ключи с company
    companyCode : str
    url : str
    inn : str
    kpp : str
    ogrn : str
    #конец ключей с company

    isModerated : bool
    deleted : bool
    visibility : str 

    #ключи с contactList
    contactType : str
    contactValue : str
    isModerated : bool
    isPreferred : bool
    #конец ключей с contactList