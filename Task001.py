# Задание 1 Напишите программу, которая принимает на вход вещественное
# число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

def input_number(input_text):
    while True:
        number = input(f"{input_text}")
        try:
            val = float(number)
            break
        except ValueError:
            print("Это не число!")     
        # else all is good, val is >=  0 and an integer
    return val

def digit_sum(n):
    sum = 0
    for i in str(n): 
        if i != ".":
            sum += int(i)
    return sum
   
n = input_number("Enter number: ")
print(digit_sum(n))