# Урок 1. Ввод-Вывод, операторы ветвления


# 1.Найдите сумму цифр трехзначного числа
# n = input("Введите трехзначное число: ")
# summ = 0
# for i in n:
#     summ += int(i)
# print(summ)



# 2. Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# s = int(input("Сколько было журавликов: "))
# print(f"Сегей сделал {int(s / 3 / 2)} журавликов, Катя сделала {int(s / 3 * 2)} журавликов, Петя сделал {int(s / 3 / 2)} журавликов!")


# 3. Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
#  Вам требуется написать программу, которая проверяет счастливость билета.

# num = input("Номер билета: ")
# sum_1 = 0
# sum_2 = 0
# for i in range(0, 3):
#     sum_1 += int(num[i])
# for i in range(3, 6):
#     sum_2 += int(num[i])
# if sum_1 == sum_2:
#     print('yes')
# else:
#     print('no')


# 4.Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, 
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).

# n, m, k = int(input('Ширина: ')), int(input('Длина: ')), int(input('сколько оттделить: '))
# if n * m > k:
#     if k % n == 0 or k % m == 0:
#         print('YES')
#     else:
#         print('NO')
# else:
#     print('NO')