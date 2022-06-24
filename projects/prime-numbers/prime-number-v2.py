import math

def keysFromList(lst, predicate):
  result = []
  for i in range(0, len(lst)):
    if predicate(i):
      result.append(i)
    else:
      result.append(None)
  return list(filter(lambda n: n is not None, result));

def sieveOfEratosphenes(n):
    sieve = [False] * 2 +  [True] * (n - 2)
    for i in range(2, math.ceil(math.sqrt(n))):
      if sieve[i] is True:
        j_range = []
        for k, _ in enumerate(range(i, n)): 
          value = i*i + k*i
          if value >= n:
            break
          j_range.append(value)
        # I cannot write this list comprehension, I give up
        #for j in (n for n in [(i*i + (n * i))) for n range(i, n)]]:
        for j in j_range:
          sieve[j] = False
    sieve = list(map(lambda cell: cell is True, sieve))
    return keysFromList(sieve, lambda idx: sieve[idx] is True)


CORRECT_ANSWER = 24133

def getSumOfFirst100Numbers():
    primes = sieveOfEratosphenes(546)
    print("primes = ", primes)
    print("sum = ", sum(primes))
    return sum(primes)

def main():
    assert getSumOfFirst100Numbers() == CORRECT_ANSWER
    print("All assertions passed")
main()