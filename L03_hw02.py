#Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
#имя, фамилия, год рождения, город проживания, email, телефон.
#Функция должна принимать параметры как именованные аргументы.
#Реализовать вывод данных о пользователе одной строкой.


def func(name, surname, year_of_birth, town, email, phone):
    print(name, surname, year_of_birth, town, email, phone)

name = "Денис"
surname = "Маврин"
year_of_birth = "14.02.1988"
town = "Мурманск"
email = "murad@mail.ru"
phone = "+7-999-456-54-55"

func(name, surname, year_of_birth, town, email, phone)


