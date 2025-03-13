from enum import Enum
import re

class ObjectType(Enum):
    ALPHABETICAL = "Alphabetical"
    REAL_NUMBER = "Real Number"
    INTEGER = "Integer"
    ALPHA_NUMERIC = "Alpha Numeric"

    @staticmethod
    def get_from_object(object):
        if re.match(r'^[a-zA-Z]+$', object):
            return ObjectType.ALPHABETICAL
        
        if re.match(r'^-?\d+$', object):
            return ObjectType.INTEGER
        
        if re.match(r'^-?\d+\.\d+$', object):
            return ObjectType.REAL_NUMBER
        
        if re.match(r'^[a-zA-Z0-9]+$', object):
            return ObjectType.ALPHA_NUMERIC
