class Counter:
    step = None
    stop = None

    def __init__(self, start):
        self.verify_int(start)
        self.__current_step = 0
        self.start = start

    @classmethod
    def verify_int(cls, value):
        """ Проверяет на целое число """
        if type(value) != int:
            raise TypeError('Значение должно быть целым числом!')

    def verify_step(self):
        """ Сравнивает step и stop если stop is not None"""
        if self.stop and self.step > self.stop:
            raise LookupError('Превышено значение step')

    def do_step(self):
        if self.step is not None:
            self.verify_int(self.step)
            self.verify_step()
            self.__current_step += self.step
        else:
            self.__current_step += 1

    def __str__(self):
        return f"Текущий шаг = {self.__current_step}"


a = Counter(4)
print(a)
a.do_step()
print(a)
b = Counter(1)
b.step = 6
b.do_step()
print(b)
c = Counter(24)
c.step = 20
c.stop = 19
c.do_step()
