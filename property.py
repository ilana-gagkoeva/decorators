class Student:
    """ Студент """

    def __init__(self, name: str, lastname: str):
        """ Запись имени и фамилии студента"""

        self._name = name
        self._lastname = lastname

    @property
    def name(self):
        """ Получение значения атрибута name """
        return self._name

    @name.setter
    def name(self, new_name: str):
        """ Изменение атрибута name на new_name """ 
        self._name = new_name

    @property
    def lastname(self):
        return self._lastname


    @name.deleter
    def name(self):
        """ Удаление атрибута name из класса """
        del self._name

# использование
s = Student('Pavapepe', 'Gemabodi')
print('Student name:', s.name)

# изменение имени
s.name = 'Pawape'
print('New student name:', s.name)

# удаление атрибута name
del s.name
s.name # <- ошибка, атрибута уже не существует