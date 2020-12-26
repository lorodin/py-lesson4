# 1. Реализовать скрипт, в котором должна быть предусмотрена функция расчета заработной платы сотрудника.
# В расчете необходимо использовать формулу: (выработка в часах*ставка в час) + премия.
# Для выполнения расчета для конкретных значений необходимо запускать скрипт с параметрами.

import sys


def cmd_help():
    print(
        "Invalid command arguments\n"
        f"Example use:\npython {sys.argv[0].split('/')[-1]} days hourly_rate prize\n"
        "Where:\n"
        " days        (integer) - days count\n"
        " hourly_rate (float)   - salary per day \n"
        " prize       (float)"
    )


calc_salary = lambda days, hours_rate, prize: (days * hours_rate) + prize

if __name__ == "__main__":
    try:
        file, days_str, hourly_rate_str, prize_str = sys.argv
        print(f"Salary = {calc_salary(int(days_str), float(hourly_rate_str), float(prize_str))}")
    except ValueError:
        cmd_help()
        exit()
