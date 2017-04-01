#!/usr/bin/python3

from unittest import main, TestCase


def isprime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True


# generator function
# by using 'yield'
def primes(n=1):
    while(True):
        if isprime(n):
            yield n
        n += 1


for n in primes():
    if n > 100:
        break
    print(n)


class prime_test (TestCase):
    def test_1(self):
        print(primes())
        print(primes())
        print(primes())
        # assert primes(1) == 2

if __name__ == "__main__":
    main()
