# https://en.wikipedia.org/wiki/Chudnovsky_algorithm

from decimal import Decimal, getcontext

def getPI(nDigit):
  getcontext().prec = nDigit+2
  MAX_ITER = 1000
  K, M, L, X, S = 6, 1, 13591409, 1, 13591409
  for k in range(1, MAX_ITER):
    M = (K**3 - 16*K) * M // k**3 
    L += 545140134
    X *= -262537412640768000
    S += Decimal(M * L) / X
    K += 12
  pi = 426880 * Decimal(10005).sqrt() / S
  pi = Decimal(str(pi)[:nDigit+1])
  return pi


if __name__ == "__main__":
    while True:
      digits = input('Please enter a digit: ')
      if digits == 'q':
        break
      print(getPI(int(digits)))