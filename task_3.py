from string import ascii_letters

text_1 = "Введите строку\nВведите 'exit' для выхода: -- "
text_2 = "Введите смещение\nВведите 'exit' для выхода: -- "
text_3 = "Введите 1 для шифрования\nВведите введите 2 для дешифрования\nВведите 'exit' для выхода: -- "


class MyCripto:
    user_value = None
    user_string = None

    def __init__(self, value: int):
        self.verify_int(value)
        self.value = value

    @classmethod
    def verify_int(cls, value):
        """ Int validate """
        if type(value) is not int:
            raise ValueError('Значение должно быть целым числом!')
        else:
            return value

    @classmethod
    def verify_str(cls, string):
        """ Str validate """
        if type(string) is not str:
            raise TypeError('Введите строку!')

    @classmethod
    def verify_ascii(cls, string):
        """ Проверка строки на английские символы с регистром и без """
        for i in string:
            if i not in ascii_letters:
                raise ValueError('Строка должна содержать буквы только английского алфавита!')

    def encrypt(self, string):
        """ Принимает строку и возвращает зашифрованную строку """
        encrypt_string = ''  # Задаем пустую строку, для добавления символов после шифрования
        self.verify_str(string)
        self.verify_ascii(string)
        for i in string:
            for j in ascii_letters:
                if i == j:  # Находит совпадение символов в строках
                    index = ascii_letters.find(j)  # Присваивает номер индекса совпавшего элемента в строке ascii
                    if index + self.value > len(ascii_letters) - 1:
                        encrypt_string += ascii_letters[index + self.value - len(ascii_letters)]
                    else:
                        encrypt_string += ascii_letters[index + self.value]
        return encrypt_string

    def decrypt(self, string):
        """ Принимает строку и возвращает дешифрованную строку """
        decrypt_string = ''  # Задаем пустую строку, для добавления символов после дешифрования
        self.verify_str(string)
        self.verify_ascii(string)
        for i in string:
            for j in ascii_letters:
                if i == j:  # Находит совпадение символов в строках
                    index = ascii_letters.find(j)  # Присваивает номер индекса совпавшего элемента в строке ascii
                    decrypt_string += ascii_letters[index - self.value]
        return decrypt_string


def interface():
    """ Открывает интерфейс работы с пользователем """
    out = False

    while (user_value := input(text_2)) != 'exit':
        try:
            user_object = MyCripto(int(user_value))  # Создает обьект пользователя
        except:
            print('Значение должно быть целым числом!')
            continue

        while (user_string := input(text_1)) != 'exit':
            try:
                user_object.verify_ascii(user_string)
            except:
                print('Строка должна содержать буквы только английского алфавита!')
                continue
            else:
                out = True

            while (user_choice := input(text_3)) != 'exit':
                try:
                    int(user_choice)
                except:
                    print('Введите число!')
                    continue
                if int(user_choice) != 1 and int(user_choice) != 2:
                    print('1 или 2!')
                    continue
                user_choice = int(user_choice)
                if user_choice == 1:
                    print(user_object.encrypt(user_string))
                if user_choice == 2:
                    print(user_object.decrypt(user_string))
                else:
                    out = True
                interface()

            if out:
                break
        if out:
            print('Асталависта!')
            break


interface()


