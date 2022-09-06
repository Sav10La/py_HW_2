# # Задание 4 Задайте список из N элементов, заполненных числами из
# # промежутка [-N, N].
# # Найдите произведение элементов на позициях a и b.
# # Значения N, a и b вводит пользователь с клавиатуры.

def input_number(input_text):
    while True:
        n = input('Введите n: ')
        a = input('Введите a: ')
        b = input('Введите b: ')
        try:
            val_n = int(n)
            val_a = int(a)
            val_b = int(b)
            if val_a > val_n * 2 + 1 or val_b > val_n * 2 + 1:
                print("Введеное позиция вне диапазона, попробуйте снова!")
                continue
            break
        except ValueError:
            print("Это не целое число!")     
        # else all is good
    return val_n, val_a, val_b

def fill_list(n):
    list = [i for i in range(-n, n + 1)]
    return list

def print_list(n):
    list = [i for i in range(-n, n + 1)]
    print(list)
    
def multiply_elements(list, a, b):
    while a - 1 < len(list) and b - 1 < len(list):
        return list[a - 1] * list[b - 1]

n, a, b = input_number('')

list = fill_list(n)
print_list(n)

print(f'Произведение элементов на позициях {a} и {b} равно {multiply_elements(list, a, b)}')