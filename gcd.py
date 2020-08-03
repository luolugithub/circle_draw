# -*- coding: utf-8 -*-
# @Time    : 2020/8/3 上午9:04
# @Author  : Luo Lu
# @Email   : argluolu@gmail.com
# @File    : gcd.py
# @Software: PyCharm


# Python Program to find GCD of Two Numbers

# a = float(input(" Please Enter the First Value a: "))
# b = float(input(" Please Enter the Second Value b: "))

a = 912
b = 1101

i = 1
while (i <= a and i <= b):
    if (a % i == 0 and b % i == 0):
        gcd = i
    i = i + 1

print("\n HCF of {0} and {1} = {2}".format(a, b, gcd))