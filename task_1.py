class Version:

    @classmethod
    def verify_str(cls, value):
        """ Проверяет аргумент на формат ввода """
        if type(value) != str:
            raise TypeError('Неверный формат ввода!')
        if value.strip('., 0, 1, 2, 3, 4, 5, 6, 7, 8, 9') != '':
            raise ValueError('Неверный формат ввода!')
        if value.count('.') != 2:
            raise ValueError('Неверный формат ввода!')

    @classmethod
    def define_args(cls, value):
        """ Определяет аргументы x y z """
        x = int(value.split('.')[0])
        y = int(value.split('.')[1])
        z = int(value.split('.')[2])
        return x, y, z

    def __init__(self, value):
        self.verify_str(value)

        self.x, self.y, self.z = self.define_args(value)

    def __str__(self):
        return f"x = {self.x}, y = {self.y}, z = {self.z}"

    def __gt__(self, other):
        return self.x > other.x, self.y > other.y, self.z > other.z

    def __ge__(self, other):
        return self.x >= other.x, self.y >= other.y, self.z >= other.z

    def __eq__(self, other):
        return self.x == other.x, self.y == other.y, self.z == other.z


a = Version('645768568686811.22222.33333')
b = Version('1111.22222.333435533')
c = Version('111.22222.33333')
print(a)
print(b)
print(c)
print(a > b)
print(a >= b)
print(a < c)
print(a <= b)
print(a == c)
