from enum import Enum
import re

class ObjectType(Enum):
    ALPHABETICAL = 0
    REAL_NUMBER = 1
    INTEGER = 2
    ALPHA_NUMERIC = 3
    
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
