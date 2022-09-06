# Задание 3 Задайте список из n чисел последовательности (1+1/n)^n и
# выведите на экран их сумму,
# округлённую до трёх знаков после точки.
# Пример:
# Для n = 6 -> 14.072

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

def sum_seq(n):
    sum = 0
    for i in range(1, n + 1):
        sum += round((1 + 1 / i) ** i, 3)
    return sum

n = input_number("Enter number: ")
print(sum_seq(n))