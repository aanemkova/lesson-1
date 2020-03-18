# print ('Hello world!')
# print(5 + 5)
# print(2 * 5)
# print(12 % 5)

# name = "Ivan"
# sum_papers = 10
# print(not 5 > 1)
# name = input('Ты кто? ')
# print('Привет', name)
# age = int(input('Сколько лет? '))
# # print(age > 18)
# if age >= 18:
#     print('Доступ разрешен')
# else:
#     print('В доступе отказано')
# print ('qwe')

# color = 'black'
# if color == 'red':
#     print('Красный')
# elif color  == 'blue':
#     print('Синий')
# elif color == 'black':
#     print('Черный')
# else:
#     print('Не распознано')

# num_1 = int(input())
# num_2 = int(input())
#
# if num_1 != num_2:
#     print('не равны')
#     if num_2 > num_1:
#         print ('второе больше')
#     else:
#         print('Первое больше')
# else:
#     print('равны')
#
# num = int(input('Введите число от 0 до 10  '))
#
# while num <= 10:
#     num = num + 1
#     if num == 5:
#         continue
#     if num == 8:
#         break
#     print(num)
# print('end program')

name = input('Имя: ')
surname = input('Фамилия: ')
age = int(input('Возраст: '))
money = float(input('Деньги: '))

print('Привет,', name, surname, '. Тебе', age, 'лет. У тебя:', money)
print('Привет, %s %s. Тебе %i лет. У тебя: %f' %(name, surname, age, money))
print('Привет, {} {}. Тебе {} лет. У тебя: {}' .format(name, surname, age, money))
print(f'Привет, {name} {surname}. Тебе {age} лет. У тебя: {round(money, 2)}')