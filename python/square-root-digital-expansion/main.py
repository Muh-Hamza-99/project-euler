import decimal 
import math

decimal.getcontext().prec = 102
result = 0
for num in range(100 + 1):
    if not math.sqrt(num).is_integer():
        result += sum(decimal.Decimal(num).sqrt().as_tuple()[1][:100])
print(result)