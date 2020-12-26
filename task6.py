# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.
#
# Подсказка: использовать функцию count() и cycle() модуля itertools.
#
# Обратите внимание, что создаваемый цикл не должен быть бесконечным.
# Необходимо предусмотреть условие его завершения.
# Например, в первом задании выводим целые числа, начиная с 3, а при достижении числа 10 завершаем цикл.
# Во втором также необходимо предусмотреть условие, при котором повторение элементов списка будет прекращено.


import inputs
from itertools import count, cycle


def task_6_1(start_item, iter_size = 10):
    last_item = start_item + iter_size
    for item in count(start, 1):
        if item >= last_item:
            break
        yield item


def task_6_2(list_items, repeat_count = 10):
    length = repeat_count * len(list_items)
    for item in cycle(list_items):
        if length <= 0:
            return
        length -= 1
        yield item


start = inputs.i(
    "start item"
)

size = inputs.i(
    "list size",
    positive_only = True
)

repeats = inputs.i(
    'repeat list count',
    positive_only = True
)

data = [item for item in task_6_1(start, size)]

print(f"List: {data}")
print(f"List repeat: {[item for item in task_6_2(data, repeats)]}")
