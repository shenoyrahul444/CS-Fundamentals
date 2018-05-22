# Fibonacci Series can be done programmed using 2 ways:
# 1> Iterative approach
# 2> Recursive
#      i> Memoization (Using LRU Cache)

def fib_rec(n):
    if n <= 1:
        return n

    return fib_rec(n-1) + fib_rec(n-2)

print(fib_rec(10))