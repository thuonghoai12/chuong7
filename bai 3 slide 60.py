# -*- coding: utf-8 -*-
"""
Created on Sun Oct  6 15:54:10 2024

@author: Admin
"""
# bai 3 slide 60
#1/a
import random
def tao_seqA():
    n = random.randint(30, 80)
    seqA=[]
    for i in range(n+1):
        if random.randint(0, 1) == 0:
            seqA.append(round(random.uniform(-79, 39),2))
        else:
            seqA.append(random.randint(-79, 39))
    return seqA

#1/b
def ktra_dulieu(seqA):
    return [type(i).__name__ for i in seqA]
    

#1/c
def thongke(seqA):
    return len(seqA)


#1/d
def sapxep_sepB(seqA):
    return sorted(seqA)


#1/e
def trungbinh(seqA):
    return sum(seqA)/len(seqA)


#1/f
def trungbinh_seqB():
#vidu, chẵn:  [1,2,3,4] => (2+3)/2=2.5
#vidu, lẻ: [1,2,3,4] =>2
    #cách 1
    n = len(seqB)
    return (seqB[n//2-1] + seqB[n//2])/2 if n%2 == 0 else seqB[n//2]
    #cách 2
    #if n%2 ==0:
        #return seqB[n//2-1 + seqB[n//2] if n%2 == 0 
    #else:
        #return seqB[n//2]

#1/g
def khoangcach(seq):
    return max(seq)-min(seq)


#1/h
def  sosanh(seaA, seqB):
    return trungbinh(seqA), trungbinh_seqB(seqB), trungbinh(seqA) == trungbinh_seqB(seqB)

    
                

    
    
if __name__=='__main__':
    seqA = tao_seqA()
    print(seqA)
    print(ktra_dulieu(seqA))
    print(thongke(seqA))
    seqB = sapxep_sepB(seqA)
    print(seqB)
    print(trungbinh(seqA))
    print(trungbinh_seqB(seqB))
    print(khoangcach(seqA))
    print(khoangcach(seqB))
 
    trungbinh(seqA), trungbinh_seqB(seqB)
    sosanhAB = sosanh(seqA, seqB)
    print(sosanhAB)
    
    
    
    
    
 


            
    
    
