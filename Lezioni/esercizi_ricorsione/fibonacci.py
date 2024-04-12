from time import time
from functools import cache, lru_cache


class Fibonacci:
    def __init__(self):
        self.cache = {0: 0, 1: 1}

    def calcola_elemento(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.calcola_elemento(n - 1) + self.calcola_elemento(n - 2)

    def calcola_elemento_cache(self, n):
        if self.cache.get(n) is not None:
            return self.cache[n]
        else:
            self.cache[n] = (self.calcola_elemento_cache(n - 1) + self.calcola_elemento_cache(n - 2))
            return self.cache[n]

    @lru_cache(maxsize=None)
    def calcola_elemento_lru(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.calcola_elemento_lru(n - 1) + self.calcola_elemento_lru(n - 2)


if __name__ == '__main__':
    fib = Fibonacci()
    N = 40

    start_time = time()
    elemento = fib.calcola_elemento(N)
    end_time = time()
    print(f"L'elemento {N} della sequenza è {elemento}")
    print(f"Elapsed time: {end_time - start_time}")

    start_time = time()
    elemento = fib.calcola_elemento_cache(N)
    end_time = time()
    print(f"L'elemento {N} della sequenza è {elemento}")
    print(f"Elapsed time con cache scritta da noi: {end_time - start_time}")

    start_time = time()
    elemento = fib.calcola_elemento_lru(N)
    end_time = time()
    print(f"L'elemento {N} della sequenza è {elemento}")
    print(f"Elapsed time con lru: {end_time - start_time}")
