from datetime import datetime
from colorama import Fore, Style

from application import *
from application.db import *
from main import *

if __name__ == '__dirty_main__':
    print('\n')
    date_reveal()
    print(datetime.now())
    print('\n')
    calculate_salary()
    print('\n')
    get_employees()
