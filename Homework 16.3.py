def power(x, n):
    return (1 if n == 0 else
    x if n == 1 else
    power(x * x, n // 2) if n % 2 == 0 else
           x * power(x, n - 1))

print(power(2, 3) == 8)
True