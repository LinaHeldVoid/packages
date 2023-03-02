from datetime import datetime
from colorama import Fore, Style
f
from application.salary import calculate_salary
from application.db.people import get_employees


def date_reveal():
    print(Fore.BLUE + Style.BRIGHT + 'ДАТА')
    print(Style.RESET_ALL)


if __name__ == '__main__':
    print('\n')
    date_reveal()
    print(datetime.now())
    print('\n')
    calculate_salary()
    print('\n')
    get_employees()
