import math

def sieveOfEratosphenes(n):
    sieve = list(map(lambda n: [n, None], list(range(2, math.ceil(math.sqrt(n))))))
    sieve[0][1] = True
    resultPrimes = [sieve[0][0]]
    









    # Note: So I have fucked up a start condition
    shitList = list(
            filter(
                lambda n: (
                    # Starting condition
                    # ==================
                    # When the this `while` loop executes
                    # it has to start iterating. There is
                    # a `[2, True]` is the `sieve`
                    (
                        n[1]
                            is
                        True
                    ) 
                    # Ending condition
                    # ================
                    # The loop has to stop at some point. 
                    # The loop should and when there is
                    # no items in the `sieve` with `[_, None]`,
                    # All the items should be marked either 
                    # `False` or `True`.
                        and
                    (
                        not (
                            n[1] is  True
                                or
                            n[1] is  False
                        )
                    )),
                sieve
            )
        )
    shitLen = len(shitList)
    print("shitList =", shitList)
    print("shitLen =", shitLen)






















    while False and len(
        list(
            filter(
                lambda n: (
                    # Starting condition
                    # ==================
                    # When the this `while` loop executes
                    # it has to start iterating. There is
                    # a `[2, True]` is the `sieve`
                    (
                        n[1]
                            is
                        True
                    ) 
                    # Ending condition
                    # ================
                    # The loop has to stop at some point. 
                    # The loop should and when there is
                    # no items in the `sieve` with `[_, None]`,
                    # All the items should be marked either 
                    # `False` or `True`.
                        and
                    (
                        not (
                            n[1] is  True
                                or
                            n[1] is  False
                        )
                    )),
                sieve
            )
            )
        ) > 0:
        print(sieve)
        print("Entering while")
        p = sieve[0][0]
        while p < n:
            print('p = ', p)
            p *= 2
            if p >= len(sieve):
                continue
            print("Marking `sieve[p - 2][1]` as `False`. p = ", p);
            sieve[p - 2][1] = False
        # Mark all `None` as `False` in `sieve`
        for cell in sieve:
            if cell[1] is None:
                cell[1] = False 
        if p >= len(sieve):
            continue
        greaterThanP = list(filter(lambda n: n[0] > p and n[1] is None, sieve))
        if len(greaterThanP) == 0:
            print("pass")
            pass
            #stop??
        else:
            print(greaterThanP, len(greaterThanP))
            p = greaterThanP[p - 2]
            print("Marking `sieve[p - 2][1]` as `True`. p = ", p);
            sieve[p - 2][1] = True
            print('p = ', p)
            p = min(map(lambda n: n[0], greaterThanP))
            resultPrimes.append(p[0])

    return resultPrimes


def main():
    print(sieveOfEratosphenes(10));

main()