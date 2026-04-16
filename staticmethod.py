from random import randint 

class Worker:
    """ Работник отдела """

    @staticmethod
    def calculate_salary(productivity: float):
        """ Вычисление зарплаты работника по показателю его продуктивности """

        if productivity < .3:
            salary = randint(10_000, 20_000)

        elif productivity < .7:
            salary = randint(50_000, 70_000)

        elif productivity < .9:
            salary = randint(120_000, 140_000)
        else:
            salary = 256_000

        return salary

salary = Worker.calculate_salary(productivity=.42)
print(salary)