# 3 algorithms using dynamic programming, all of which return n-th fibonacci number

# 1: Top Down fibonacci
def fib_td(n: int, memo: list=None) -> int:
    if not memo:
        memo = [-1 for _ in range(n + 1)]
    if n <= 1:
        memo[n] = n
    if memo[n] == -1:
        memo[n] = fib_td(n - 1, memo) + fib_td(n - 2, memo)
    return memo[n]


# 2: Bottom Up fibonacci
def fib_bu(n: int, memo: list=None) -> int:
    if not memo:
        memo = [0 for _ in range(n + 1)]
        if len(memo) > 1:
            memo[1] = 1
    for i in range(2, n + 1):
        memo[i] = memo[i - 1] + memo[i - 2]
    return memo[n]


# 2A: Bottom Up fibonacci, but here we don't use additional memory
def fib_bu_upgraded(n: int) -> int:
    if n <= 1:
        return n
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


for _ in range(10):
    print(fib_td(_), fib_bu(_), fib_bu_upgraded(_))