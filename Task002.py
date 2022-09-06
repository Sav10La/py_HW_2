# Задание 2 Напишите программу, которая принимает на вход число N и
# выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def input_number(input_text):
    while True:
        number = input(f"{input_text}")
        try:
            val = int(number)
            break
        except ValueError:
            print("Это не целое число!")     
        # else all is good
    return val

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)

n = input_number("Enter number: ")

list = [factorial(i) for i in range(1, n + 1)] #list comprehension

print(list)