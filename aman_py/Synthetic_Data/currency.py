"""Generate currency-related data."""

from ..LOADER_DICTIONARY import Dictionary_GET

import random
import math
__all__ = ['Description_Curr', 'gen_curren']

def gen_curren():
    """Random currency gen_curren, e.g. `GBP`."""
    return random.choice(Dictionary_GET('currency_codes')).strip()

def Description_Curr():
    """Random currency like pounds in UK and Rupees in India S`."""
    return random.choice(Dictionary_GET('currency_descriptions')).strip()
