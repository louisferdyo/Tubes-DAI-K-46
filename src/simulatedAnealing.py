import random
import math
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
    return 0

def randomCoordinate() : 
    x = random.randint(0, 4)
    y = random.randint(0, 4)
    z  =random.randint(0, 4)
    return (x,y,z)
 
def makeRandomState(cubeTemp) :
    condition = False #kondisi untuk cari nilai
    coor1 = randomCoordinate()
    coor2 = randomCoordinate()

    while condition == False :
        if(coor1 == coor2) :
            coor1 = randomCoordinate()
            coor2 = randomCoordinate()
        else :
            condition = True
            break

    # print("\nstate 1 = \n", cube[coor1[0]][coor1[1]][coor1[2]])
    # print("\nstate 2 = \n", cube[coor2[0]][coor2[1]][coor2[2]])

    temp = cubeTemp[coor2[0]][coor2[1]][coor2[2]]
    cubeTemp[coor2[0]][coor2[1]][coor2[2]] = cubeTemp[coor1[0]][coor1[1]][coor1[2]]
    cubeTemp[coor1[0]][coor1[1]][coor1[2]] = temp
    return cubeTemp


def simulatedAnnealing(cube, T, coolingRate, threshold) : 
    startTime = time.time()
    i = 0
    stuck = 0
    objectiveValues = [] 
    deltaEValues = []
    while T > 0: 
        T -= coolingRate # penurunan temperatur dilakukan dengan dikurangi koefisien penurunan
        i += 1
        if T <= 0 :
            break
        print("\nT : ", T)
        currentValue = objectiveFunction(cube)
        objectiveValues.append(currentValue)
        cubeTemp = copy.deepcopy(cube)

        cube2 = makeRandomState(cubeTemp)
        # print("hasil tengah : ", objectiveFunction(cube))
        nextValue = objectiveFunction(cube2)
        
        print("current : " , currentValue, " next : ", nextValue)
        deltaE = nextValue - currentValue
        print("delta = ", deltaE)
        
        if(deltaE < 0) : # karena yang lebih kecil dari 0 artinya next value lebih kecil dari current yang artinya mengurangi error
            cube = cube2
            print("less than 0")
        else : 
            prob = math.exp((-1*deltaE)/ T) # karena error harus lebih kecil maka dikali -1
            deltaEValues.append(prob)
            print("prob = ", prob)
            if(prob > threshold) : 
                cube = cube2
                print("swapped")
            else :
                stuck += 1
        # print("hasil akhir : ", objectiveFunction(cube))
    endTime = time.time()
    duration = endTime - startTime
    plotObjectiveFunction(objectiveValues, deltaEValues)
    return cube, stuck, duration

def plotObjectiveFunction(objectiveValues, deltaEValues):
    plt.figure(figsize=(12, 6))
    
    # Plot untuk nilai objective function terhadap iterasi
    plt.subplot(2, 1, 1)
    plt.plot(range(1, len(objectiveValues) + 1), objectiveValues, label='Nilai Objective Function')
    plt.xlabel('Iterasi')
    plt.ylabel('Nilai Objective Function')
    plt.title('Plot Nilai Objective Function terhadap Iterasi')
    plt.legend()
    plt.grid(True)
    
    # Plot untuk exp(ΔE / T) terhadap iterasi
    plt.subplot(2, 1, 2)
    plt.plot(range(1, len(deltaEValues) + 1), deltaEValues, label='Nilai exp(ΔE / T)')
    plt.xlabel('Iterasi')
    plt.ylabel('Nilai exp(ΔE / T)')
    plt.title('Plot Nilai exp(ΔE / T) terhadap Iterasi')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

#----------------------------------------------------------------------------------------

# Main

#----------------------------------------------------------------------------------------

# coor1 = randomCoordinate()
# coor2 = randomCoordinate()
# if(coor1 == coor2) :
#     print("lol")
# else : 
#     print("output1 : ", coor1, " coor2 : ", coor2)
#     temp = coor2
#     coor2 = coor1
#     coor1 = temp
#     print("hasil : ")
#     print("output1 : ", coor1, " coor2 : ", coor2)


# cube = makeCube()

# print("\n\n\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n\n")

# initialStateRandom(cube)
# printCube(cube)

# p1 = objectiveFunction(cube)


# finalCube, stuck, duration = simulatedAnnealing(cube, 10, 0.5, 5)


# print("-------------------------------------------------------------------------------")
# printCube(finalCube)

# p2 = objectiveFunction(finalCube)

# print("\nobjective function awal = ", p1)
# print("\nobjective function akhir = ", p2)
# print("\nfrekuensi terkena stuck yaitu = ", stuck)
# print("waktu = ", duration)
