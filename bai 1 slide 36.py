# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 13:10:34 2024

@author: Admin
"""
#bai_1 cach 1
#def tinhtong_(*args, **kwargs):
#    tong = 0
#    for i in args:
#        tong += i
 #   return tong
#bai_1 cach 2
def tinhtong(*args, **kwargs):
    return sum(args)
def tinhtich(*args, **kwargs):
    tich = 1
    for i in args:
        tich *= i
    return tich
#
if __name__=="__main__":
    ds=[1,2,3,4,5]
    print(tinhtong(*ds))
    print(tinhtich(*ds))