"""
4. Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке. Для выполнения задания обязательно использовать генератор.
Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
Результат: [23, 1, 3, 10, 4, 11]
"""
import random as rd
i = 44
init_list = [rd.randint(x,i) for x in range(7)] + [rd.randint(x,i) for x in range(7)]
rd.shuffle(init_list)
print("Список чисел: ", init_list)
print("Элементы списка, не имеющие повторений: ", [x for x in init_list if 1 == init_list.count(x)])