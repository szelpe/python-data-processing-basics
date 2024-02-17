from decimal import *
from datetime import *

# number_str = '$5,000.5'
# number_str = number_str.strip('$')
# number_str = number_str.replace(',', '')
# number = float(number_str)
#
# num1 = Decimal('0.1')
# num2 = Decimal('0.2')
#
# print(number)

# date = datetime.now()
# date_str = '2023-11-03'
# date2 = datetime.strptime(date_str, '%Y-%m-%d')
#
# # print(type(date))
# delta = date - date2
#
#
# print(date.strftime('%Y.%m.%d.'))

values = [ '5.5   ', '6', '7.8', None, '   ' ]


def is_blank():
    return not value or not value.strip()


for value in values:
    if is_blank():
        continue

    value = value.strip()
    print(float(value))
