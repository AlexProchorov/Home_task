# # my_dict={'зима': [12,1,2],
# #     'весна': [3,4,5],
# #     'лето': [6,7,8],
# #     'осень':[9,10,11]
# # }
# #
# #
# # User_answer=int(input('Введите значение месяца от 1 до 12: '))
#
# for key in my_dict.keys():
#     if User_answer in my_dict[key]:
#         print(key)

# Решение с помощью list

mounth =( 'зима', 'весна', 'лето', 'осень')

user_answer2=int(input('Введите снова число от 1 до 12: '))
while True:
    if user_answer2 <= 2 or user_answer2==12:
        print(mounth[0])
        break
    elif user_answer2 >=3 and user_answer2<=5:
        print(mounth[1])
        break
    elif user_answer2 >= 6 and user_answer2 <=8:
        print(mounth[2])
        break
    else:
        print(mounth[3])
        break


