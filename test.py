import numpy as np
import pandas as pd


def test_function_1(a):
    a = 100
    return a

def test_function_1_copy(a):
    a = 200
    return a
  
def test_function_2(a):
    a = 20
    return a

def test_function_2_1(a):
    a = 1023
    return a**2
  
def test_function_3(a):
    a = 100
    a /= 3
    a *= 2
    a -= 100
    a += 100
    return a

print(test_function_1(1000))

def test_function_4(a):
    print(a)
    return a


print(test_function_3(10))
