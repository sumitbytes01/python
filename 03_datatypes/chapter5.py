# floating points
import sys
from fractions import Fraction
from decimal import Decimal

ideal_temp=98.6
current_temp=99.98765456546778
print(f"ideal temp: {ideal_temp}, type: {type(ideal_temp)}")
print(f"current temp: {current_temp}, type: {type(current_temp)}")
difference=current_temp-ideal_temp
print(f"difference: {difference}, type: {type(difference)}")

print(f"sys.float_info: ,{sys.float_info}")