"""Generate random personal information."""

import random

from ..LOADER_DICTIONARY import Dictionary_GET

__all__ = ['Per_Gender', 'Gender_ABBR', 'Race', 'language']


def Per_Gender():
    """this is Random function which Generates  Per_Gender."""
    return random.choice(Dictionary_GET('genders')).strip()


def Gender_ABBR():
    """this is Random function which Generates  abbreviated Per_Gender."""
    return Per_Gender()[0:1]

def Race():
    """this is Random function which Generates  Race."""
    return random.choice(Dictionary_GET('races')).strip()


def language():
    """this is Random function which Generates  language name, e.g. ``Polish``."""
    return random.choice(Dictionary_GET('languages')).strip()
