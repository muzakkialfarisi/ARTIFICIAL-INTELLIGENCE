import csv

arrfile = []

def readfile():
    csvid, csvfol, csveng= [], [], []
    csvini = []
    # pembacaan data
    with open('influencers.csv') as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            csvid.append(row[0])
            csvfol.append(row[1])
            csveng.append(row[2])
    csvini.append(csvid)
    csvini.append(csvfol)
    csvini.append(csveng)
    return csvini

def fuzzifikasi(a):
    temp, arrf, arre, arrfuzi = [[]for i in range(3)], [[]for i in range(3)], [[]for i in range(3)], []
    fmin1, fmin2, fmid1, fmid2, fmid3, fmid4, fmax1, fmax2 = 15000, 39999, 15001, 40000, 50000, 69999, 50001, 70000
    emin1, emin2, emid1, emid2, emid3, emid4, emax1, emax2 = 1, 2.9, 1.1, 3, 5, 5.9, 5.1, 6

    # convert string to interger and float
    j = 1
    while j < len(a[0]):
        temp[0].append(int(a[0][j]))
        temp[1].append(int(a[1][j]))
        temp[2].append(float(a[2][j]))
        j += 1
    
    # pengecekan data pada kolom followerCount
    j = 0
    while (j < len(temp[0])):
        if (temp[1][j] <= fmin1):
            arrf[0].append(1)
            arrf[1].append(0)
            arrf[2].append(0)
        elif (temp[1][j] >= fmax2):
            arrf[0].append(0)
            arrf[1].append(0)
            arrf[2].append(1)
        elif (fmid2 <= temp[1][j] <= fmid3):
            arrf[0].append(0)
            arrf[1].append(1)
            arrf[2].append(0)
        elif (fmid1 <= temp[1][j] <= fmin2):
            arrf[0].append( (fmin2-temp[1][j]) / (fmin2-fmin1) )
            arrf[1].append( (temp[1][j]-fmid1) / (fmid2-fmid1) )
            arrf[2].append(0)
        elif (fmax1 <= temp[1][j] <= fmid4):
            arrf[0].append(0)
            arrf[1].append( (fmid4-temp[1][j]) / (fmid4-fmid3) )
            arrf[2].append( (temp[1][j]-fmax1) / (fmax2-fmax1) )
        j += 1

    # pengecekan data pada kolom engagementRate
    j = 0
    while (j < len(temp[2])):
        if (temp[2][j] <= emin1):
            arre[0].append(1)
            arre[1].append(0)
            arre[2].append(0)
        elif (temp[2][j] >= emax2):
            arre[0].append(0)
            arre[1].append(0)
            arre[2].append(1)
        elif (emid2 <= temp[2][j] <= emid3):
            arre[0].append(0)
            arre[1].append(1)
            arre[2].append(0)
        elif (emid1 <= temp[2][j] <= emin2):
            arre[0].append( float((emin2-temp[2][j]) / (emin2-emin1)) )
            arre[1].append( float((temp[2][j]-emid1) / (emid2-emid1)) )
            arre[2].append(0)
        elif (emax1 <= temp[2][j] <= emid4):
            arre[0].append(0)
            arre[1].append( float((emid4-temp[2][j]) / (emid4-emid3)) )
            arre[2].append( float((temp[2][j]-emax1) / (emax2-emax1)) )
        j += 1

    arrfuzi.append(arrf)
    arrfuzi.append(arre)
    return arrfuzi

def inference(b):
    temp = [[]for i in range(3)]

    for i in range(len(b[0][0])):
        for j in range(len(b[0])):
            # perbandingan minimum followerCount Low dengan engagementRate
            if (b[0][0][i] <= b[1][j][i]):
                temp[0].append(b[0][0][i])
            else:
                temp[0].append(b[1][j][i])
            # perbandingan minimum followerCount Average dengan engagementRate
            if (b[0][1][i] <= b[1][j][i]):
                temp[1].append(b[0][1][i])
            else:
                temp[1].append(b[1][j][i])
            # perbandingan minimum followerCount High dengan engagementRate
            if (b[0][2][i] <= b[1][j][i]):
                temp[2].append(b[0][2][i])
            else:
                temp[2].append(b[1][j][i])
 
    tempinf = [[]for i in range(100)]
    # mengurutkan low, average, high sesuai id
    k = 0
    for i in range(len(b[0][0])):
        for j in range(3):
            tempinf[i].append(temp[j][k])
            tempinf[i].append(temp[j][k+1])
            tempinf[i].append(temp[j][k+2])
        k += 3
    
    inference = [[]for i in range(100)]
    for i in range(len(b[0][0])):
        # mencari nilai max dari accepted
        acc = 0
        if(tempinf[i][0] >= acc):
            acc = tempinf[i][0]
        if(tempinf[i][1] >= acc):
            acc = tempinf[i][1]
        if(tempinf[i][3] >= acc):
            acc = tempinf[i][3]
        inference[i].append(acc)
        # mencari nilai max dari considert
        con = 0
        if(tempinf[i][2] >= con):
            con = tempinf[i][2]
        if(tempinf[i][4] >= con):
            con = tempinf[i][4]
        if(tempinf[i][5] >= con):
            con = tempinf[i][5]
        if(tempinf[i][6] >= con):
            con = tempinf[i][6]
        inference[i].append(con)
        # mencari nilai max dari rejected
        rej = 0
        if(tempinf[i][7] >= rej):
            rej = tempinf[i][7]
        if(tempinf[i][8] >= rej):
            rej = tempinf[i][8]
        inference[i].append(rej)
    
    return inference

def defuzzi_sugeno(c):
    arr, arrid, arridbanget = [], [], []
    acc = 100
    con = 75
    rej = 50

    # rumus defuzzi-sugeno
    for i in range(len(c)):
        arr.append( round(((c[i][0]*acc) + (c[i][1]*con) + (c[i][2]*rej)) / (c[i][0]+c[i][1]+c[i][2]),2) )

    # sorting descending
    max = 0
    for j in range(len(arr)):
        if max <= arr[j]:
            cek = 0
            for k in range(len(arrid)):
                if ( j == arrid[k]):
                    cek += 1
            if cek == 0:
                max = arr[j]
                arrid.append(j)
    
    # mengambil 20 data terbaik
    for i in range(20):
        arridbanget.append(arrid[i])

    return arridbanget


def main():
    arrfile = defuzzi_sugeno(inference(fuzzifikasi(readfile())))
    print(arrfile)

    # output via chosen.csv
    with open('chosen.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Chosen ID"])
        for i in range(len(arrfile)):
            a = arrfile[i]
            writer.writerow([a])

if __name__== "__main__":
    main()