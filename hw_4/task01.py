"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.
"""
output_per_hour = input('Введите выработку в часах: ')
rate_per_hours = input('Введите ставку в час: ')
premium = input('Введите размер премии: ')
def salary (output_per_hour, rate_per_hours,premium):
    return int(output_per_hour) * int(rate_per_hours) + int(premium)
print(salary(output_per_hour=output_per_hour,rate_per_hours=rate_per_hours, premium=premium))