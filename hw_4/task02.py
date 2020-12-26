"""
2. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для формирования списка использовать генератор.
Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
Результат: [12, 44, 4, 10, 78, 123].
"""

n = int(input('Введите число элементов исходного списка: '))
import random as rd
init_list = [rd.randint(x,200) for x in range(n)]
rd.shuffle(init_list)
print("Изсходный список: ", init_list)
print("Новый список (элементы исходного списка, значения которых больше предыдущего элемента): ", [init_list[i] for i in range(1,len(init_list)) if init_list[i] > init_list[i-1]])