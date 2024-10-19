# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 15:49:39 2024

@author: Admin
"""

#bai 2 - slide 59
ds = [('Tiền Giang', 63), ('Long An', 62), ('Vĩnh Long', 64), ('Bình Dương ', 60)]
#print(sorted(ds))
print(sorted(ds, key=lambda x:x[1]))

