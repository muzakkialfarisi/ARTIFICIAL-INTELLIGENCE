import csv
import random

# inisialisasi
n = 10
lenchromosom = 15
arrpopulasi = [[]for i in range(n)]
pop1 = [[]for i in range(n)]
pop2 = [[]for i in range(n)] 
fit = []
orangtua = []
crosso = [[]for i in range(n)]
mutass = []


def populasi(a, n):
    arrpop = [[]for i in range(n)]
    for i in range(n):
        for j in range(a):
            arrpop[i].append(random.randint(0, 1))        
    return arrpop

def decode1(b):
    p1 = [[]for i in range(n)]
    j = 0
    i = 0
    while (i < len(b)):
        while (j <= i) and (j <= len(b)):
            if(b[i][0] == 1):
                p1[i].append("Tinggi")
            else:
                p1[i].append("")
            if(b[i][1] == 1):
                p1[i].append("Normal")
            else:
                p1[i].append("")
            if(b[i][2] == 1):
                p1[i].append("Rendah")
            else:
                p1[i].append("")
            if(b[i][3] == 1):
                p1[i].append("Pagi")
            else:
                p1[i].append("")
            if(b[i][4] == 1):
                p1[i].append("Siang")
            else:
                p1[i].append("")
            if(b[i][5] == 1):
                p1[i].append("Sore")
            else:
                p1[i].append("")
            if(b[i][6] == 1):
                p1[i].append("Malam")
            else:
                p1[i].append("")
            if(b[i][7] == 1):
                p1[i].append("Cerah")
            else:
                p1[i].append("")
            if(b[i][8] == 1):
                p1[i].append("Berawan")
            else:
                p1[i].append("")
            if(b[i][9] == 1):
                p1[i].append("Rintik")
            else:
                p1[i].append("")
            if(b[i][10] == 1):
                p1[i].append("Hujan")
            else:
                p1[i].append("")
            if(b[i][11] == 1):
                p1[i].append("Tinggi")
            else:
                p1[i].append("")
            if(b[i][12] == 1):
                p1[i].append("Normal")
            else:
                p1[i].append("")
            if(b[i][13] == 1):
                p1[i].append("Rendah")
            else:
                p1[i].append("")
            if(b[i][14] == 1):
                p1[i].append("Ya")
            else:
                p1[i].append("")
            
            j += 1

        i += 1

    return p1

def decode2(b):
    p2 = [[]for i in range(n)]
    j = 0
    i = 0
    while (i < len(b)):
        while (j <= i) and (j <= len(b)):
            if(b[i][0] == 0):
                p2[i].append("Tinggi")
            else:
                p2[i].append("")
            if(b[i][1] == 0):
                p2[i].append("Normal")
            else:
                p2[i].append("")
            if(b[i][2] == 0):
                p2[i].append("Rendah")
            else:
                p2[i].append("")
            if(b[i][3] == 0):
                p2[i].append("Pagi")
            else:
                p2[i].append("")
            if(b[i][4] == 0):
                p2[i].append("Siang")
            else:
                p2[i].append("")
            if(b[i][5] == 0):
                p2[i].append("Sore")
            else:
                p2[i].append("")
            if(b[i][6] == 0):
                p2[i].append("Malam")
            else:
                p2[i].append("")
            if(b[i][7] == 0):
                p2[i].append("Cerah")
            else:
                p2[i].append("")
            if(b[i][8] == 0):
                p2[i].append("Berawan")
            else:
                p2[i].append("")
            if(b[i][9] == 0):
                p2[i].append("Rintik")
            else:
                p2[i].append("")
            if(b[i][10] == 0):
                p2[i].append("Hujan")
            else:
                p2[i].append("")
            if(b[i][11] == 0):
                p2[i].append("Tinggi")
            else:
                p2[i].append("")
            if(b[i][12] == 0):
                p2[i].append("Normal")
            else:
                p2[i].append("")
            if(b[i][13] == 0):
                p2[i].append("Rendah")
            else:
                p2[i].append("")
            if(b[i][14] == 0):
                p2[i].append("Tidak")
            else:
                p2[i].append("")
            j += 1
        i += 1
    return p2

def fitnes(c, d):
    countfit = []
    csvsuhu, csvwaktu, csvlangit, csvlembab, csvterbang= [], [], [], [], []
    with open('datalatih.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            csvsuhu.append(row[0])
            csvwaktu.append(row[1])
            csvlangit.append(row[2])
            csvlembab.append(row[3])
            csvterbang.append(row[4])

    i = 0
    while (i < len(c)):
        count = 0
        j = 1
        while (j < len(csvsuhu)):
            if(((c[i][0]==csvsuhu[j]) or (c[i][1]==csvsuhu[j]) or (c[i][2]==csvsuhu[j]))
            and ((c[i][3]==csvwaktu[j]) or (c[i][4]==csvwaktu[j]) or (c[i][5]==csvwaktu[j]) or (c[i][6]==csvwaktu[j]))
            and ((c[i][7]==csvlangit[j]) or (c[i][8]==csvlangit[j]) or (c[i][9]==csvlangit[j]) or (c[i][10]==csvlangit[j]))
            and ((c[i][11]==csvlembab[j]) or (c[i][12]==csvlembab[j]) or (c[i][13]==csvlembab[j]))):
                if (c[i][14]==csvterbang[j]):
                    count += 1
            elif (((d[i][0]==csvsuhu[j]) or (d[i][1]==csvsuhu[j]) or (d[i][2]==csvsuhu[j]))
            and ((d[i][3]==csvwaktu[j]) or (d[i][4]==csvwaktu[j]) or (d[i][5]==csvwaktu[j]) or (d[i][6]==csvwaktu[j]))
            and ((d[i][7]==csvlangit[j]) or (d[i][8]==csvlangit[j]) or (d[i][9]==csvlangit[j]) or (d[i][10]==csvlangit[j]))
            and ((d[i][11]==csvlembab[j]) or (d[i][12]==csvlembab[j]) or (d[i][13]==csvlembab[j]))
            and (d[i][14]==csvterbang[j])):
                if (d[i][14]==csvterbang[j]):
                    count += 1
            else:
                if (c[i][14]==csvterbang[j]):
                    count += 1
            j += 1
        count = count/(len(csvsuhu)-1)
        countfit.append(count)
        i += 1
    return countfit

def ortu(e, f):
    ortufit = []
    calonortu = []

    i = 0
    while (i < len(e)):
        if (e[i] == max(e)):
            index0 = i
        i += 1

    e[index0] = -1

    i = 0
    while (i < len(e)):
        if (e[i] == max(e)):
            index1 = i
        i += 1    

    ortufit.append(index1)
    ortufit.append(index0)

    i = 0
    while (i<len(ortufit)):
        calonortu.append(f[ortufit[i]])
        i += 1
    return calonortu

def crossover(g):
    index0 = []
    p1 = []
    p2 = []
    i = 0
    while (i<2):
        index0.append(random.randint(0, 14))
        i += 1

    if (index0[0] < index0[1]):
        x1 = index0[0]
    else:
        x1 = index0[1]

    if (index0[0] >= index0[1]):
        x2 = index0[0]
    else:
        x2 = index0[1]

    i = x1
    while (i <= x2):
        p1.append(g[0][i])
        p2.append(g[1][i])
        i += 1

    i = x1
    j = 0
    while (i <= x2):
        g[0][i] = p2[j]
        g[1][i] = p1[j]
        i += 1
        j += 1
    return g

    Mutasi

def mutasi():
    x = "\n"
    return x

def main():
    print("\n")
    arrpopulasi = populasi(lenchromosom, n)
    print("Populasi   : ",arrpopulasi)
    print("\n")
    pop1 = decode1(arrpopulasi) 
    print("Dekode 1   : ",pop1)
    print("\n")
    pop2 = decode2(arrpopulasi) 
    print("Dekode 2   : ",pop2)
    print("\n")
    fit = fitnes(pop1, pop2)
    print("Fitnes     : ",fit)
    print("\n")
    orangtua = ortu(fit, arrpopulasi)
    print("Orang Tua  : ",orangtua)
    print("\n")
    crosso = crossover(orangtua)
    print("Crossover  : ",crosso)
    print(mutasi())

if __name__== "__main__":
  main()
