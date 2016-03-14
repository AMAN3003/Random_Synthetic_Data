"""CREATES THE FAKE DATA"""

import random
import string

from ..LOADER_DICTIONARY import Dictionary_GET

__all__ = [
    'STREET_LOCO', 'STREET_Num', 'Street_SUFF', 'Street_ADD',
    'City', 'State', 'State_ABB', 'PinCode', 'MobNO', 'Country',
    'World_Continent'
]

def Country():
    """This function generates random values of  Country name."""
    return random.choice(Dictionary_GET('countries')).strip()




def Street_ADD():
    """
    This function generates random values of  street address. Equivalent of ``STREET_Num() + ' ' + 
    STREET_LOCO() + ' ' + Street_SUFF()``.
    """
    return '%s %s %s' % (STREET_Num(), STREET_LOCO(), Street_SUFF())

def STREET_LOCO():
    """This function generates random values of  street name."""
    return random.choice(Dictionary_GET('street_names')).strip()

def STREET_Num():
    """This function generates random values of  street number."""
    length = int(random.choice(string.digits[1:6]))
    return ''.join(random.sample(string.digits, length))



def Street_SUFF():
    """This function generates random values of  street suffix."""
    return random.choice(Dictionary_GET('street_suffixes')).strip()

def MobNO():
    """This function generates random values of  MobNO number in `#-(###)###-####` Style_Format."""
    Style_Format = '#-(###)###-####'

    Random_Val_Result = ''
    for i in Style_Format:
        if i == '#':
            Random_Val_Result += str(random.randint(0, 9))
        else:
            Random_Val_Result += i

    return Random_Val_Result


def State():
    """This function generates random values of  US State name."""
    return random.choice(Dictionary_GET('states')).strip()


def City():
    """This function generates random values of  City name."""
    return random.choice(Dictionary_GET('cities')).strip()


def State_ABB():
    """This function generates random values of  US abbreviated State name."""
    return random.choice(Dictionary_GET('state_abbrevs')).strip()


def PinCode():
    """This function generates random values of  ZIP code, either in `#####` or `#####-####` Style_Format."""
    Style_Format = '#####'
    if random.random() >= 0.5:
        Style_Format = '#####-####'

    Random_Val_Result = ''
    for i in Style_Format:
        if i == '#':
            Random_Val_Result += str(random.randint(0, 9))
        else:
            Random_Val_Result += i

    return Random_Val_Result


def MobNO():
    """This function generates random values of  MobNO number in `#-(###)###-####` Style_Format."""
    Style_Format = '#-(###)###-####'

    Random_Val_Result = ''
    for i in Style_Format:
        if i == '#':
            Random_Val_Result += str(random.randint(0, 9))
        else:
            Random_Val_Result += i

    return Random_Val_Result


def World_Continent():
    """This function generates random values of  World_Continent name."""
    return random.choice(Dictionary_GET('continents')).strip()
