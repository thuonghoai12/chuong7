# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 13:33:57 2024

@author: Admin
"""
#bai_2 - slide 36
import math
def chuvi_dt(hinh, pheptinh, *args, ** kwargs):
    if hinh == 'hinhvuong':
        canh = args[0]
        return 4*canh if pheptinh == 'chuvi' else canh ** 2
    #tach câu return
        #if pheptinh == 'chuvi'
            #return 4*canh
        #else:
            #return canh **2
    elif hinh == 'hinhchunhat':
        dai = args[0]
        rong = args[1]
        return 2*(dai+rong) if pheptinh == 'chuvi' else dai*rong
    elif hinh == 'hinhtron':
        bk =args[0]
        return (round(2*math.pi*bk),2) if pheptinh == 'chuvi' else math.pi*bk**2
    else:
        return 'hinh khong hop le'
if __name__=='__main__':
    print('chu vi hinh vuong:', chuvi_dt('hinhvuong', 'chuvi ', 4))
    print('chu vi hinh vuong:', chuvi_dt('hinhvuong', 'dientich ', 4))
   
    print('chu vi hinh tron: ', chuvi_dt('hinhtron', 'chu vi', 4))
    print('chu vi hinh tron: ', chuvi_dt('hinhtron', 'dientich', 4))
   
    print('chu vi chu nhat:', chuvi_dt('hinhchunhat', 'chu vi', 4, 3))
    print('chu vi chu nhat:', chuvi_dt('hinhchunhat', 'dientich', 4, 3))

