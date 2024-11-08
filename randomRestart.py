#include <stdio.h>
#include <string.h>
import random
import copy
import time
import matplotlib.pyplot as plt
def makeCube():
    cube = [[[0 for i in range(5)] for j in range(5)] for k in range(5)]
    num = 1
    for i in range(5):
        for j in range(5):
            for k in range(5):
                cube[i][j][k] = num
                num += 1
    return cube
    
def printCube(cube) :
    print("Sisi ke sumbu x")
    for i in range(5) :
        print()
        print()
        print("----- Sisi ke-", i+1,"------")
        for j in range (5) :
            print()
            for k in range (5) :
                print(cube[i][j][k], "|" , end="")

    print()
    print()
    print("-----------------------------------------------")
    print("Sisi ke sumbu y")            
    for k in range(5) :
        print()
        print()
        print("----- Sisi ke-", k+1,"------")
        for i in range (5) :
            print()
            for j in range (5) :
                print(cube[i][j][k], "|" , end="")

    print()
    print()
    print("-----------------------------------------------")
    print("Sisi ke sumbu z")            
    for j in range(5) :
        print()
        print()
        print("----- Sisi ke-", j+1,"------")
        for k in range (5) :
            print()
            for i in range (5) :
                print(cube[i][j][k], "|" , end="")
    return 0

def objectiveFunction(cube) :
    #Menghitung jumlah selisih jumlah setiap row tiang diagonal dengan 315
    errorSum = 0
    magicNumber = 315
    xSum = 0
    ySum = 0
    zSum = 0
    diagonalXSum = 0
    contDiagonalXSum = 0
    diagonalYSum = 0
    contDiagonalYSum = 0
    diagonalZSum = 0
    contDiagonalZSum = 0
    spaceDiaSum_a = 0
    spaceDiaSum_b = 0
    spaceDiaSum_c = 0
    spaceDiaSum_d = 0
    # menghitung ke sumbu x (baris)
    for j in range(5) :
        for k in range (5) :
            xSum = 0
            for i in range (5) :
                xSum += cube[i][j][k]
            errorSum += abs(xSum - magicNumber)
            
    # menghitung ke sumbu y (kolom) 
    for k in range(5) :
        for i in range (5) :
            ySum = 0
            for j in range (5) :
                ySum += cube[i][j][k]
            errorSum += abs(ySum - magicNumber)
    # Menghitung ke sumbu z
    for i in range(5) :
        for j in range(5) :
            zSum = 0
            for k in range(5) :
                zSum += cube[i][j][k]
            errorSum += abs(zSum - magicNumber)
    # print("e1 saat ini : ", errorSum)
    # menghitung diagonal sisi ke sumbu x
    for i in range(5) :
        diagonalXSum = 0
        contDiagonalXSum = 0
        for x in range(5) :
            diagonalXSum += cube[i][x][x]
            
            contDiagonalXSum += cube[i][4-x][x]
        errorSum += abs(contDiagonalXSum - magicNumber)
        errorSum += abs(diagonalXSum - magicNumber)
    # menghitung diagonal sisi ke sumbu y
    for j in range(5) :
        diagonalYSum = 0
        contDiagonalYSum = 0
        for y in range(5) :
            diagonalYSum += cube[y][j][y]
       
            contDiagonalYSum += cube[y][j][4-y]
        errorSum += abs(contDiagonalYSum - magicNumber)
        errorSum += abs(diagonalYSum - magicNumber)
     # menghitung diagonal sisi ke sumbu z
    for k in range(5) :
        diagonalZSum = 0
        contDiagonalZSum = 0
        for z in range(5) :
            diagonalZSum += cube[z][z][k]
            
            contDiagonalZSum += cube[z][4-z][k]
        errorSum += abs(diagonalZSum - magicNumber)
        errorSum += abs(contDiagonalZSum - magicNumber)
    # menghitung diagonal ruang hitung dari atas
    for a in range (5) :
        spaceDiaSum_a += cube[a][4-a][a]
    errorSum += abs(spaceDiaSum_a - magicNumber)

    for b in range (5) :
        spaceDiaSum_b += cube[4-b][4-b][b]
    errorSum += abs(spaceDiaSum_b - magicNumber)

    for c in range (5) :
        spaceDiaSum_c += cube[4-c][4-c][4-c]
    errorSum += abs(spaceDiaSum_c - magicNumber)

    for d in range (5) :
        spaceDiaSum_d += cube[d][4-d][4-d]
    errorSum += abs(spaceDiaSum_d - magicNumber)
    
    return errorSum

def initialStateRandom(cube) :
    arrayAngka = []
    for i in range(5):
        for j in range(5):
            for k in range(5):
                found = False
                while found == False :
                    angkaAcak = random.randint(1,125)
                    if(angkaAcak not in arrayAngka) :
                        arrayAngka.append(angkaAcak)
                        cube[i][j][k] = angkaAcak
                        found = True            
    return cube

def findBestNeighbor(cube) :
    bestCube = copy.deepcopy(cube)
    bestValue = objectiveFunction(cube)

    for i in range(5):
        for j in range(5):
            for k in range(5):
                for l in range(5):
                    for m in range(5):
                        for n in range(5):
                            if (i, j, k) != (l, m, n):
                                # Ubah posisi
                                cube[i][j][k], cube[l][m][n] = cube[l][m][n], cube[i][j][k]
                                # Cari nilai objektif dari pertukaran tersebut
                                value = objectiveFunction(cube)
                                # jika nilai error atau value lebih kecil, lakukan pertukaran
                                if value < bestValue:
                                    bestCube = copy.deepcopy(cube)
                                    bestValue = value
                                # Ubah kemabali ke cube asal
                                cube[i][j][k], cube[l][m][n] = cube[l][m][n], cube[i][j][k]

    return bestCube

def randomRestart(cube, maxIteration) :
    startTime = time.time()
    i = 0
    restartCount = 0
    iterationSum = []
    objectiveValues = []
    condition = True
    while condition == True :
        currentValue = objectiveFunction(cube)
        objectiveValues.append(currentValue)
        neigborCube = findBestNeighbor(cube)
        neigborValue = objectiveFunction(neigborCube)
        if(neigborValue < currentValue) :
            cube = neigborCube
            i += 1 
        elif (restartCount < maxIteration and neigborValue >= currentValue) :
            cube = initialStateRandom(cube)
            restartCount += 1
            iterationSum.append(i)
            i = 0
        else :
            condition = False
    endTime = time.time()
    duration = endTime - startTime  
    plotObjectiveFunction(objectiveValues)
    return cube, restartCount, iterationSum, duration

def plotObjectiveFunction(objectiveValues):
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, len(objectiveValues) + 1), objectiveValues, marker='o', label='Nilai Objective Function')
    plt.xlabel('Iterasi')
    plt.ylabel('Nilai Objective Function')
    plt.title('Plot Nilai Objective Function terhadap Jumlah Iterasi')
    plt.legend()
    plt.grid(True)
    plt.show()

#----------------------------------------------------------------------------------------

# Main

#----------------------------------------------------------------------------------------

cube = makeCube()
printCube(cube)

print("\n\n\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n\n")

initialStateRandom(cube)
printCube(cube)

p1 = objectiveFunction(cube)
print("\nobjective function awal = ", p1)


finalCube, restartCount, iterationPerRestart, duration = randomRestart(cube, 10)


p2 = objectiveFunction(finalCube)
print("\nobjective function akhir = ", p2)
print("waktu = ", duration)
print(f"Cube di restart sebanyak {restartCount}")
print(f"Iterasi setiap restart adalah sebagai berikut {iterationPerRestart}")