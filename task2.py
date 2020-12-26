# 2. Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.

from random import randint

N = randint(10, 20)

rnd_list = [randint(0, 1000) for x in range(N)]

print(f"Init list: { rnd_list }")

result_list = [rnd_list[i] for i in range(1, len(rnd_list)) if rnd_list[i] > rnd_list[i - 1]]

print(f"Result list: { result_list }")
