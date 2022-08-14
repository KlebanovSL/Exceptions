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
    def point_index_list(cls, value):
        """ Создает список с номерами индексов точек в аргументе """
        point_index_list = []
        for i in range(0, len(value)):
            if value[i] == '.':
                point_index_list.append(i)
        return point_index_list

    @classmethod
    def define_args(cls, value):
        """ Определяет переменные срезами строк относительно индексов точек в аргументе, записанных в список """
        pil = cls.point_index_list(value)
        x = int(value[0: pil[0]])
        y = int(value[pil[0] + 1: pil[1]])
        z = int(value[pil[1] + 1:])
        return x, y, z

    def __init__(self, value):
        self.verify_str(value)
        self.point_index_list(value)

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
