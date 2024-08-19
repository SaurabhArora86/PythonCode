'''
The Fibonacci series is the sequence of numbers (also called Fibonacci numbers), where every number is the sum of the preceding two numbers, such that the first two terms are '0' and '1'. In some older versions of the series, the term '0' might be omitted. A Fibonacci series can thus be given as, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, . . . It can thus be observed that every term can be calculated by adding the two terms before it.

Given the first term, F0 and second term, F1 as '0' and '1' respectively, the third term here can be given as, F2 = 0 + 1 = 1

Similarly,

F3 = 1 + 1 = 2
F4 = 2 + 1 = 3
F5 = 2 + 3 = 5
F6 = 3 + 5 = 8
F7 = 5 + 8 = 13
and so on
Therefore, to represent any (n+1)th term in this series, we can give the expression as, Fn = Fn-1 + Fn-2. We can thus represent a Fibonacci series as shown in the image below,

Fibonacci Series is given by 0 and 1 as the first two terms and every other term is obtained by adding its previous two terms.
'''


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))


print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(7))
