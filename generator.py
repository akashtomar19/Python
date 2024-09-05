def fibon(n):
    a = b = 1
    for i in range(n):
        yield a
        a, b = b, a + b


# lazy evaluation can be seen here
a = fibon(10)
next(a)
next(a)
print(next(a))

# using for loop 

for num in a:
    print(num)
