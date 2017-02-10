fibo_lookup = {}
def fibonacci(n):
    if n not in fibo_lookup:
        if n == 1 or n == 2:
            val = 1
        else:
            val = fibonacci(n-1) + fibonacci(n-2)
        fibo_lookup[n] = val
    return fibo_lookup[n]
