"""THIS Generates Random Names of the People """

import random

from ..LOADER_DICTIONARY import Dictionary_GET

__all__ = [
    'first_name', 'Last_Name', 'FULLNAME', 'MALE_1ST_NAME',
    'FEMALE_1st_NAME', 'Comp_Name', 'JOB', 'Job_Desgn_Suffix',
    'title', 'suffix', 'LOC', 'Indtry'
]


def first_name():
    """Generates the random name of male or the female """
    Dictionary_ = Dictionary_GET('male_first_names')
    Dictionary_ += Dictionary_GET('female_first_names')

    return random.choice(Dictionary_).strip()


def FEMALE_1st_NAME():
    """generate first name which appears to be female """
    return random.choice(Dictionary_GET('female_first_names')).strip()




def MALE_1ST_NAME():
    """Generates a first name which apperas to be male"""
    return random.choice(Dictionary_GET('male_first_names')).strip()

def Last_Name():
    """Generates last name """
    return random.choice(Dictionary_GET('last_names')).strip()

def Job_Desgn_Suffix():
    """generates the tittle of the job"""
    return random.choice(Dictionary_GET('job_title_suffixes')).strip()

def LOC():
    """give a arbitary location , e.g. ``MI6 Headquarters``."""
    return random.choice(Dictionary_GET('locations')).strip()

def JOB():
    """Random job title."""
    STR_RES = random.choice(Dictionary_GET('job_titles')).strip()
    STR_RES = STR_RES.replace('#{N}', Job_Desgn_Suffix())
    return STR_RES

def FULLNAME():
    """
    its the same as calling first name and last name function
    """
    return first_name() + ' ' + Last_Name()



def title():
    """Random tittle for the person like Dr,Engn."""
    return random.choice(Dictionary_GET('name_titles')).strip()


def suffix():
    """Generates Random suffix for the name like."""
    return random.choice(Dictionary_GET('name_suffixes')).strip()

def Comp_Name():
    """Comapny name"""
    return random.choice(Dictionary_GET('company_names')).strip()

def Indtry():
    """NAME OF THE INDUSTRY"""
    return random.choice(Dictionary_GET('industries')).strip()
