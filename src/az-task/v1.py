from random import randint


def prepareArray():
  result = [x for x in range(1, 100 + 1)] # + 1 since the last number is excluded: https://docs.python.org/3/library/stdtypes.html#ranges
  answerIdx = randint(0, len(result) - 1)
  answer = result[answerIdx]
  result.pop(answerIdx)
  return (result, answer,)

def findMissingNumber(a) -> int:
  hundredRange = list(range(1, 100 + 1))
  for i in hundredRange:
    if i not in a:
      return i

ASSERTIONS_COUNT = 1000000

def main():
  for i in range(1, ASSERTIONS_COUNT + 1):
    arr, answer = prepareArray()
    assert findMissingNumber(arr) == answer
  print(f"{ASSERTIONS_COUNT} assertions passed.")
if __name__ == "__main__":
  main()