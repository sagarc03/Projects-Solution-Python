collatz = {1: 0}

def collatzConjeture(n):

  if n < 1:
    return 0

  if n not in collatz:
    if n % 2 == 0:
      collatz[n] = 1 + collatzConjeture(n//2)
    else:
      collatz[n] = 1 + collatzConjeture(n * 3 + 1)
  
  return collatz[n]


print(collatzConjeture(50))
print(collatz)