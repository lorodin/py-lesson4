# 7. Реализовать генератор с помощью функции с ключевым словом yield, создающим очередное значение.
# При вызове функции должен создаваться объект-генератор.
# Функция должна вызываться следующим образом: for el in fact(n).
# Функция отвечает за получение факториала числа, а в цикле необходимо выводить только первые n чисел,
# начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например, факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.

import inputs


def fact(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
        yield result


if __name__ == "__main__":
    n = inputs.i(
        'number',
        validate_cb = lambda v: v > 0,
        error_message = "Must be positive integer number")

    for index, item in enumerate(fact(n), 1):
        print(f'{ index } != { item }')
