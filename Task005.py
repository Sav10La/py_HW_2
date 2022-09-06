# Задание 5 Реализуйте алгоритм перемешивания списка.

import random

# Method 1
list1 = [11, 22, 33, 44, 55, 66]
print ("Начальный список: ", list1)
n = len(list1)

# use Fisher–Yates shuffle Algorithm to shuffle a list
for i in range(n - 1, 1, -1):
    # pick a random index from 0 to i
    j = random.randint(0, i + 1)
    # swap list[i] with the element at random index
    list1[i], list1[j] = list1[j], list1[i]
print ("Перемешанный список: " +  str(list1))

# Method 2
list2 = [1, 2, 3, 4, 5, 6]
print("Начальный список: ", list2)
n = len(list2)
 
for i in range(n):
    # select an index randomly
    j = random.randint(0, n - 1)
    # delete the element at that index
    element = list2.pop(j)
    # append the deleted element to the list
    list2.append(element)
print("Перемешанный список: ", list2)