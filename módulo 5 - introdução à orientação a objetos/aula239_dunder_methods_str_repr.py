# Python Dunder Methods __repr__ e __str__
# Dunder = Double Underscore = __dunder__
# Antigo e útil: https://rszalski.github.io/magicmethods/
# https://docs.python.org/3/reference/datamodel.html#specialnames
# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str
class Ponto:
    def __init__(self, x, y, z='String'):
        self.x = x
        self.y = y
        self.z = z

    #Este método é usado simplesmente para saber o retorno dos dados da classe
    def __str__(self):
        return f'({self.x}, {self.y})'

    #Este método é usado para mostrar a representação da classe
    #Normalmente usada para outros desenvolvedores
    def __repr__(self):
        # class_name = self.__class__.__name__ -> esta forma e a de baixo tem o mesmo resultado
        class_name = type(self).__name__
        #A fim de mostrar a representação de cada dado do objeto, devem ser escritos dessa forma
        #Assim será possível ver o que é string, int, float, bool ...
        return f'{class_name}(x={self.x!r}, y={self.y!r}, z={self.z!r})'


p1 = Ponto(1, 2)
p2 = Ponto(978, 876)
print(p1)
print(repr(p2))
print(f'{p2!r}')