"""THIS IS THE SCRIPT FOR GENERATION OF INTERNET IP ADDRESS OF USER,HIS COMPANY DOMAIN NAME,HIS USER NAME IN MEDICAL HEALTHCARD ETC."""

import random

from ..LOADER_DICTIONARY import Dictionary_GET
from .name import first_name

__all__ = [
    'User_Name', 'Top_Level_Domain', 'DOMAIN',
    'Email_Id','ip_v4'
]


def DOMAIN():
    """
    Random domain name.

    Lowercased STR_Res of :py:func:`~forgery_py.forgery.name.company_name()` 
    plus :py:func:`~Top_Level_Domain()`.
    """
    STR_Res = random.choice(Dictionary_GET('company_names')).strip()
    STR_Res += '.' + Top_Level_Domain()

    return STR_Res.lower()

def Top_Level_Domain():
    """Random TLD."""
    return random.choice(Dictionary_GET('top_level_domains')).strip()



def User_Name(NUM_WITH=False):
    """
    This Generates random Username based on the First name appended with the number    
    """
    STR_Res = first_name()
    if NUM_WITH:
        STR_Res += str(random.randint(63, 94))

    return STR_Res.lower()

def ip_v4():
    """generates a random Ip ADDDRESS OF THE USER DEVICE """
    return '.'.join([str(random.randint(0, 255)) for k in xrange(0, 4)])

def Email_Id(NAME=None):
    """
    IT GENERATE THE EMAIL ID BASED ON THE COMPANY NAME IN WHICH INDIVISUAL IS WORKING AND 
    IF THE USER NAME IS NONE THAN IT CALL Username() to get default name
    """
    if not NAME:
        NAME = User_Name()
    else:
        NAME = NAME.strip().replace(' ', '_').lower()

    return NAME + '@' + DOMAIN()

