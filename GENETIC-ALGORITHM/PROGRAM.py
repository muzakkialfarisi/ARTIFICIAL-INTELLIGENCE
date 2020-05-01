import random
import math

randomx1, randomx2, arracak = [], [], []
arrx1, arrx2 = [], []
arrx1new, arrx2new = [], []
anakx1, anakx2 = [], []
arrgab = []
arrobj = []
arrfit = []
arrprob = []
arrpkom = []
arrsrw = []
arrtmp = []
arrcln = []
arrcros = []
arrmut = []
rminx1 = -3 
rmaxx1 = 3
rminx2 = -2 
rmaxx2 = 2
n = 8
N = n/2
pc = 0.5
pm = 0.5

#mencari random sekaligus chromosom x1
def arrayx1(n):
    #random x1
    for i in range(n):
        randomx1.append(random.uniform(0, 1))
    i = 0
    #chromosom x1
    while (i < n):
        arrx1.append(rminx1+((rmaxx1-rminx1)/2)*(randomx1[i]+randomx1[i+1]))
        i += 2
    return arrx1

#mencari random sekaligus chromosom x2
def arrayx2(n):
    for i in range(n):
        randomx2.append(random.uniform(0, 1))
    i = 0
    while (i < n):
        arrx2.append(rminx2+((rmaxx2-rminx2)/2)*(randomx2[i]+randomx2[i+1]))
        i += 2
    return arrx2

def funct_obj(x1, x2):
    i = 0
    while (i < n/2):
        x =  ((4-2.1*(x1[i]**2)+(x1[i]**4)/3)*(x1[i]**2)+(x1[i]*x2[i])+(-4+4*(x2[i]**2))*(x2[i]**2))
        arrobj.append(x)
        i += 1
    return arrobj

def fitnes(obj):
    i = 0
    a = 0.1
    while (i < n/2):
        arrfit.append(obj[i]*-1)
        i += 1
    return arrfit

def sumarrfit(fit):
    i = 0
    x = 0
    while (i < n/2):
        x += fit[i]
        i += 1
    return x

# def maxarrfit(fit):
#     return max(fitnes(funct_obj(arrayx1(n), arrayx2(n))))

def prob(p):
    x = 0
    x = sumarrfit(fitnes(funct_obj(arrayx1(n), arrayx2(n))))
    i = 0
    while (i < n/2):
        arrprob.append(p[i]/x)
        i += 1
    return arrprob

def probkom(k):
    i = 0
    x = 0
    while (i < n/2):
        x += k[i]
        arrpkom.append(x)
        i += 1
    return arrpkom

def srw1(r):
    i = 0
    while (i < n/2):
        acak = random.uniform(0, 1)
        j = 0
        while(True):
            if (acak < r[j]):
                arrx1new.append(r[j])
                break
            else:
                j += 1
        i += 1
    return arrx1new

def srw2(r):
    i = 0
    while (i < n/2):
        acak = random.uniform(0, 1)
        j = 0
        while(True):
            if (acak < r[j]):
                arrx2new.append(r[j])
                break
            else:
                j += 1
        i += 1
    return arrx2new

def crossov(n):
    i = 0 
    while (i < n/2/2):
        arrcros.append(random.uniform(0, 0.5))
        i += 1
    return arrcros

def mutasi(pm, n):
    x = round(pm*n)
    anakx1 = arrayx1(x)
    anakx2 = arrayx2(x)
    i = 0 
    while (i < x):
        arrmut.append(anakx1[i]+anakx2[i])
        i += 1
    return arrmut

def gabungan(x, y, z):
    i = 0
    while (i < n/2):
        arrgab.append(x[i])
        arrgab.append(y[i])
        arrgab.append(z[i])
        i += 1
    return arrgab


print('x1               : ',arrayx1(n))
print('x2               : ',arrayx2(n))
print('funct objective  : ',funct_obj(arrayx1(n), arrayx2(n)))
print('fitnes           : ',fitnes(funct_obj(arrayx1(n), arrayx2(n))))
print('sum fitnes       : ',sumarrfit(fitnes(funct_obj(arrayx1(n), arrayx2(n)))))
# print('max fitnes       : ',maxarrfit(fitnes(funct_obj(arrayx1(n), arrayx2(n)))))
print('probablitas      : ',prob(fitnes(funct_obj(arrayx1(n), arrayx2(n)))))
print('prob komulatif   : ',probkom(prob(fitnes(funct_obj(arrayx1(n), arrayx2(n))))))
print('Ortu x1          : ',srw1(probkom(prob(fitnes(funct_obj(arrayx1(n), arrayx2(n)))))))
print('Ortu x2          : ',srw2(probkom(prob(fitnes(funct_obj(arrayx1(n), arrayx2(n)))))))
print('Crossover        : ',crossov(n))
print('Mutasi           : ',mutasi(pm,n))
# print('arrgab           : ',gabungan(arrayx1(n), arrayx2(n), fitnes(funct_obj(arrayx1(n), arrayx2(n)))))

