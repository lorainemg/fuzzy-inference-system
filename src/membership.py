# from abc import abstractmethod, ABCMeta


# class FuzzySet(metaclass=ABCMeta):
#     @abstractmethod
#     def evaluate(self, x:int):
#         return NotImplementedError()


class Triangular:
    """
    Fuzzy Set with Triangular-shape function defined with a, b, and m points
              .
             /|\
            / | \
           /  |  \
         _/   |   \_
          |   m   |
          a       b
    """
    def __init__(self, a:int, m:int, b:int):
        self.a = a
        self.b = b
        self.m = m
    
    def __call__(self, x:int) -> int:
        if x <= self.a or x >= self.b: 
            return 0
        elif self.a < x <= self.m:
            return (x-self.a) / (self.m-self.a)
        elif self.m < x < self.b:
            return (self.b-x) / (self.b-self.m)


class SFunction:
    """
    Fuzzy Set with a S-shaped function
             __
            /|
           / |
          /| |
       __/ | |
         | m |
         a   b

    a: point for minimum function evaluation
    m: x-value for middle function evaluation
    b: point for maximum function evaluation
    """
    def __init__(self, a:int, b:int, m:int):
        self.a = a
        self.b = b
        self.m = m

    def __call__(self, x:int) -> int:
        if x <= self.a:
            return 0
        elif self.a < x <= self.m:
            return 2((x-self.a)/(self.b-self.a))**2 
        elif m < x < b:
            return 1 - 2((x-self.a)/(self.b-self.a))**2
        else:
            return 1


class Trapezoidal:
    """
    Trapezoid-shape function defined with points a, b, c and d
               _____
              /     \
             /|     |\
            / |     | \
           /  |     |  \
         _/   |     |   \_
          |   b     c   |
          a             d
    """
    def __init__(self, a:int, b:int, c:int, d:int):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
    
    def __call__(self, x:int) -> int:
        if x <= self.a or x >= self.d:
            return 0
        elif self.a < x <= self.b:
            return (x-self.a) / (self.b-self.a)
        elif self.b < x < self.c:
            return 1
        elif self.b < x < self.d:
            return (self.d-x) / (self.d-self.c)


class Singleton:
    """
    Fuzzy Set with an only element of universe with membership above zero
    """
    def __init__(self, a:int):
        self.a = a

    def __call__(self, x:int) -> int:
        if x == self.a:
            return 1
        else:
            return 0