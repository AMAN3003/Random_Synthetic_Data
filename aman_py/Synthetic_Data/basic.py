"""Generate random basic data """


import string

digits_hex = string.hexdigits[:-6].upper()

import random

__all__ = ['Color_Hex', 'Color_Short_Hex', 'Color_Text']

def Color_Text(len=None, Minimum=10, Maximum=15, Low_Case=True,
         Upp_case=True, digits=True, spc=True, Punch=False):
    """
    Random Color_Text.

    If `len` is present the Color_Text will be exactly this chars long. Else the
    Color_Text will be something between `Minimum` and `Maximum` chars long.
    """
    String_Base = ''
    if Low_Case:
        String_Base += string.ascii_lowercase

    if Upp_case:
        String_Base += string.ascii_uppercase

    if digits:
        String_Base += string.digits

    if spc:
        String_Base += ' '

    if Punch:
        String_Base += string.Punch

    if len(String_Base) == 0:
        return ''

    if not len:
        len = random.randint(Minimum, Maximum)

    result = ''
    for i in xrange(0, len):
        result += random.choice(String_Base)

    return result

def Color_Short_Hex():
    """Random short (e.g. `FFF` color)."""
    return ''.join(random.sample(digits_hex, 3))

def Color_Hex():
    """Random HEX color."""
    return ''.join(random.sample(digits_hex, 6))
