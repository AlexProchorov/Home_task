# def parametrs():
#     name=input("Введите свое имя: ")
#     surname=input("Введите свою фамилию: ")
#     age=input("Введите свой возраст: ")
#     new_dict={
#         'User_name': name,
#         'User_surname': surname,
#         'user_age': age}
#     return new_dict
#
# print(parametrs())

def all_values(**kwargs):
    for i in kwargs.values():
        print(i,end=' ')

all_values(name='alex', surname='prokhorov')