import random
from string import ascii_uppercase, digits


class Chance:

    def string(self):
        return ''.join(random.choice(ascii_uppercase + digits) for _ in range(random.randint(10,30)))