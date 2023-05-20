#!/usr/bin/python3

'''minimum operations'''
import math


def minOperations(n):
    '''minimum operations to get n to 1'''
    if n <= 1:
        return 0

    operations = 0
    for i in range(2, int(math.sqrt(abs(n))) + 1):
        while n % i == 0:
            operations += i
            n //= i

    if n > 1:
        operations += n

    return operations
