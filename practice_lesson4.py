# 1)
class Rectangle:
    def __init__(self, first_side, second_side):
        self.first_side = first_side
        self.second_side = second_side

    def calculate_area(self):
        return self.first_side * self.second_side

    def calculate_perimeter(self):
        return (self.first_side + self.second_side) * 2


some_figure = Rectangle(4, 8)
print(some_figure.calculate_area(), some_figure.calculate_perimeter())

# 2)
import datetime
class Human:
    def __init__(self, name, city, born_year):
        self.name = name
        self.city = city
        self.born_year = born_year

    def age(self):
        current_year = datetime.datetime.now().year
        return current_year - self.born_year


first_person = Human('Андрей', 'Саратов', 1998)
print(first_person.age())

# 3)
class Calculator:
    def __init__(self, first_number, second_number):
        self.first_number = first_number
        self.second_number = second_number

    def addition(self):
        return self.first_number + self.second_number

    def subtraction(self):
        return self.first_number - self.second_number

    def multiplication(self):
        return self.first_number * self.second_number

    def division(self):
        return self.first_number / self.second_number


new_operation = Calculator(10, 2)
print(new_operation.division())

# 4)
class InfoAboutScores:
    def __init__(self, main_score, additional_score):
        self.main_score = main_score
        self.additional_score = additional_score

    def __str__(self):
        return f"First score: {self.main_score}, second score: {self.additional_score}"


User1 = InfoAboutScores(219, 352)
print(User1)

# 5)
class Employee:
    def __init__(self, name, post):
        self.name = name
        self.post = post

    def get_paid(self):
        pass

class Manager(Employee):
    def get_paid(self):
        return 60000


class Worker(Employee):
    def get_paid(self):
        return 40000


first_employee = Manager('Сергей', 'Менеджер')
second_employee = Worker('Наталья', 'Рабочий')

print(f"Сотрудник {first_employee.name} получает {first_employee.get_paid()} руб в месяц")
print(f"Сотрудник {second_employee.name} получает {second_employee.get_paid()} руб в месяц")

# 6)
# Множественное наследование
class First:
    def top_method(self):
        return 'Выполнение метода top'


class Second:
    def bottom_method(self):
        return 'Выполнение метода bottom'


class Third(First, Second):
    pass


some_object = Third()
print(some_object.top_method(), some_object.bottom_method(), sep='\n')

# Миксины
class Mixin:
    def some_method(self):
        return "called from mixin"

class Caller(Mixin):
    pass

object1 = Caller()
print(object1.some_method())
