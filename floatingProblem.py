# from decimal import Decimal
# if Decimal('1.2') - Decimal('1.0') == Decimal('0.2'):
#      print("sawa")
# else:
#      print("not sawa")

# from math import fabs
# """ the tolerance is a measure os how much difference is allowed between two values"""
#
# tolerance = 1e-6
# print(1.2-1.0)
#
# if abs(1.2 - 1.0 - 0.2) < tolerance:
#     print("sawa")
# else:
#     print("not sawa")

# from math import isclose
#
#
# tolerance = 1e-6
#
# if isclose(1.2 -1.0, 0.2, rel_tol= tolerance, abs_tol= tolerance):
#     print("sawa")
# else:
#     print("not sawa")
#
# from decimal import Decimal
#
# if Decimal('1.2') - Decimal('1.0') == Decimal('0.2'):
#     print('sawa')
#
# else:
#     print('not sawa')
#
from math import fabs

tolerance = 1e-6
if abs( 1.2 - 1.0 - 0.2) < tolerance:
    print('sawa',abs( 1.2 - 1.0 - 0.2))
else:
    print('not sawa')
#
# #
# if 1.2 - 1.0 == 0.2:
#     print('sawa')
# else:
#     print('not sawa')