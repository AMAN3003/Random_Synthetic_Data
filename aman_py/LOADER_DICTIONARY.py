
"""ITS IS  a DICTIONARY OF ALL THE DATAS."""

import codecs
import random
from os.path import abspath, dirname, join

Path_Dict_file = abspath(join(dirname(__file__), 'DATA'))

Cache_Dict = {}


def Dictionary_GET(Dictionary_Name):
    """
    IT LOAD A ``Dictionary_Name`` 
    IAND RETURNS THE CNTENTS AS STRING IF NOT LOADED
    """
    global Cache_Dict

    if Dictionary_Name not in Cache_Dict:
        try:
            Dict_File = codecs.open(
                join(Path_Dict_file, Dictionary_Name), 'r', 'utf-8'
            )
        except IOError:
            None
        else:
            Cache_Dict[Dictionary_Name] = Dict_File.readlines()
            Dict_File.close()

    return Cache_Dict[Dictionary_Name]
