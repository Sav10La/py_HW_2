# Задание 6 Напишите программу, в которой пользователь будет задавать
# две строки, а программа - определять количество вхождений одной строки
# в другой.
# Пример
# -Для "abababb" и "aba" -> 2

# Method 1
# def CountOccurrences(string, substring):
#     count = 0
#     start = 0
#     while start < len(string):
#         pos = string.find(substring, start)
#         if pos != -1:
#             start = pos + 1
#             count += 1
#         else:
#             break
#     return count
  
# string = "abababa"
# substring = "aba"
# print(CountOccurrences(string, substring))

# Method 2
# s = "abababa"
# sub = "aba"
# print(sum(sub == s[i:i + len(sub)] for i in range(len(s) - (len(sub) - 1))))

def CountOccurrences(string_a, string_b):
    count = 0
    len_a = len(string_a)
    len_b = len(string_b)
    if len_a >= len_b:
        for i in range(len_a):
            if string_b == string_a[i:i + len_b]:
                count += 1
        return count
    else:
        for i in range(len_b):
            if string_a == string_b[i:i + len_a]:
                count += 1
        return count
        
string_a = input('Введите первую строку: ')
string_b = input('Введите вторую строку: ')
print(CountOccurrences(string_a, string_b))