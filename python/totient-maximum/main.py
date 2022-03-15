import eulerlib
import fractions

totients = eulerlib.list_totients(10**6)
answer = max(range(2, len(totients)), key=(lambda number: fractions.Fraction(number, totients[number])))
print(answer)