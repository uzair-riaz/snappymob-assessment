import random
import string
from object_type import ObjectType

class RandomObjectGenerator:
    @staticmethod
    def alphabetical_object(min_length=3, max_length=10):
        length = random.randint(min_length, max_length)
        return ''.join(random.choice(string.ascii_letters) for _ in range(length))
    
    @staticmethod
    def real_object(min_val=-1000, max_val=1000):
        return random.uniform(min_val, max_val)
    
    @staticmethod
    def integer_object(min_val=-1000, max_val=1000):
        return random.randint(min_val, max_val)
    
    @staticmethod
    def alpha_numeric_object(min_length=3, max_length=10):
        length = random.randint(min_length, max_length)
        spaces_before = ' ' * random.randint(0, 10)
        spaces_after = ' ' * random.randint(0, 10)
        return spaces_before + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length)) + spaces_after
    
    @staticmethod
    def generate_random_object():
        object_type = random.choice(list(ObjectType))
        
        if object_type == ObjectType.ALPHABETICAL:
            return RandomObjectGenerator.alphabetical_object()
        elif object_type == ObjectType.REAL_NUMBER:
            return RandomObjectGenerator.real_object()
        elif object_type == ObjectType.INTEGER:
            return RandomObjectGenerator.integer_object()
        else:
            return RandomObjectGenerator.alpha_numeric_object()