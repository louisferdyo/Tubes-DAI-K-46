import random
import math
import copy
import time
import numpy as np
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
    for j in range(5) :
        print()
        print()
        print("----- Sisi ke-", j+1,"------")
        for k in range (5) :
            print()
            for i in range (5) :
                print(cube[i][j][k], "|" , end="")
   

    print()
    print()
    print("-----------------------------------------------")
    print("Sisi ke sumbu z")            
    for k in range(5) :
        print()
        print()
        print("----- Sisi ke-", k+1,"------")
        for i in range (5) :
            print()
            for j in range (5) :
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

def generateRandomPopulation(populationSize) : 
    population = []
    for i in range(populationSize) :
        individu = list(range(1, 126))
        random.shuffle(individu) 
        population.append(individu)
    return population

def geneticAlgorithm(cube, populationSize, maxIteration) :
    startTime = time.time()
    lowestObjective = 9999
    indeks = 0
    population = []
    population = generateRandomPopulation(populationSize)
    minObjectivePerIteration = []
    averageObjectivePerIteration = []
    while(indeks < maxIteration and lowestObjective > 0) :
        fitnessScore = []
        fitnessSum = 0
        fitnessPercentage = []
        wheelRange = []
        newPopulation = []
        objectives = []
        sumPercentage = 0
        currentObjectives = []
        for i in range (populationSize) :
            individu2 = convertTo3D(population[i])
            objective = objectiveFunction(individu2)
            objectives.append(objective)
            fitness = 1 / (1 + objective)
            fitnessScore.append(fitness)
            fitnessSum += fitness
        # print(f"\nPada iterasi ke {indeks+1}, Nilai Objective dari populasi awal adalah: {objectives}\n")
        for i in range (len(fitnessScore)) :
            fitnessPercent = (fitnessScore[i] / fitnessSum) * 100
            sumPercentage += fitnessPercent
            wheelRange.append(sumPercentage)
            fitnessPercentage.append(fitnessPercent)
        # print(wheelRange)
        parent = spinWheelSelection(population, wheelRange)
        # for i in range (populationSize) :
        #     parents = convertTo3D(parent[i])
        #     p = objectiveFunction(parents)
        #     print(f"obj {i+1} = {p}")

        for i in range (populationSize) :
            child = crossOver(populationSize, parent)
            if(child != None) :
                newPopulation.append(child)
        for i in range (len(newPopulation)) :
            newPopulation[i] = mutate(newPopulation[i], 0.1)
            individu2 = convertTo3D(newPopulation[i])
            currentObjective = objectiveFunction(individu2)
            currentObjectives.append(currentObjective)
            if(currentObjective < lowestObjective) :
                bestCube = copy.deepcopy(cube)
                lowestObjective = currentObjective
        print(f"\nPada iterasi ke {indeks+1}, Nilai Objective dari child adalah: {currentObjectives}")
        print(f"\nPada iterasi ke {indeks+1}, Best Objective : {lowestObjective}")
        minObjectivePerIteration.append(min(currentObjectives))
        averageObjectivePerIteration.append(sum(currentObjectives) / populationSize)
        indeks += 1
        
        population = newPopulation
        

    endTime = time.time()
    duration = endTime - startTime
    plotObjectiveFunction(minObjectivePerIteration, averageObjectivePerIteration)
    lastMinElement = minObjectivePerIteration[-1]
    lastAvgElement = averageObjectivePerIteration[-1]
    return cube, lowestObjective, indeks, duration, bestCube, lastMinElement, lastAvgElement

def mutate(individu, mutationRate) :
    indexTochange = 0
    if(random.random() < mutationRate) :
        # print("\nMutasi Dilakukan\n")
        mutationIndex = random.randint(0, len(individu) - 1)
        
        newValue = random.randint(1, 125)
        for i in range(125) :
            if(individu[i] == newValue) :
                indexTochange = i
                break
        temp = individu[mutationIndex] # melakukan pertukaran secara acak pada indeks yang acak
        individu[mutationIndex] = newValue
        individu[indexTochange] = temp
        # print(f"indeks yang berubah yaitu {mutationIndex} dan indeks yang terdampak yaitu {indexTochange}")
        # print(f"Nilai yang diubah menjadi {newValue} dan nilai yang berubah yaitu {temp}")
    # else :
    #     # print("\nMutasi Gagal Dilakukan\n")

    return individu

def spinWheelSelection(population, wheelRange) :
    parent = []
    totalPopulation = len(population)
    for i in range(totalPopulation) : 
        randomValue = random.uniform(0,100)
        for j in range(totalPopulation) :
            if(j == 0) :
                if(randomValue >=0 and randomValue <= wheelRange[j]) :
                    parent.append(population[j])
                    break
            else :
                if(randomValue >= wheelRange[j-1] and randomValue < wheelRange[j]) :
                    parent.append(population[j])
                    break
    return parent

def crossOver(populationSize, population) :
    x = random.randint(0,populationSize-1)
    y = random.randint(0,populationSize-1)
    if(populationSize == 1) :
        print("Populasi haya satu, tidak bisa crossover")
        return None
    else :
        while(x == y) :
            y = random.randint(0,populationSize-1)
            # print(f"y: {y}")
    
        length = len(population[x])
        crossoverPoint = random.randint(1, length - 1)  # Titik crossover acak dimula dari 1 untuk menghindari crossover seluruh array

        # Buat child dengan melakukan crossover
        child = population[x][:crossoverPoint] + population[y][crossoverPoint:]
            
        return child

def printPopulationDefault(population):
    for i in range(len(population)) :
        print("Populasi ke - " + str(i+1) + " : ")
        individu = convertTo3D(population[i])
        print(individu)
        print("\n")
        # print(len(population[i]))

def printIndividuDefault(individu):
    individu1 = convertTo3D(individu)
    printCube(individu1)

def printPopulation(population) :
    for idx, individu in enumerate(population, 1):
        print(f"\nIndividu ke - {idx}:")
        printIndividuAsCube(individu)
        print("----------------------------------")
        print()
        
def convertTo3D(individu):
    return np.reshape(individu, (5, 5, 5))     

def printIndividuAsCube(individu):
        # Representasi pada sumbu x
        print("\nSisi ke sumbu x")
        for i in range(5):
            print(f"\n\n----- Sisi ke-{i + 1} ------")
            for j in range(5):
                print()
                for k in range(5):
                    # Kalkulasi indeks untuk array 1D
                    index = i * 25 + j * 5 + k
                    print(f"{individu[index]:3}", "|", end="")
        
        # Representasi pada sumbu y
        print("\n\n-----------------------------------------------")
        print("Sisi ke sumbu y")
        for k in range(5):
            print(f"\n\n----- Sisi ke-{k + 1} ------")
            for i in range(5):
                print()
                for j in range(5):
                    index = i * 25 + j * 5 + k
                    print(f"{individu[index]:3}", "|", end="")

        # Representasi pada sumbu z
        print("\n\n-----------------------------------------------")
        print("Sisi ke sumbu z")
        for j in range(5):
            print(f"\n\n----- Sisi ke-{j + 1} ------")
            for k in range(5):
                print()
                for i in range(5):
                    index = i * 25 + j * 5 + k
                    print(f"{individu[index]:3}", "|", end="")
        print("\n" + "-" * 50)

def plotObjectiveFunction(minObjective, averageObjective):
    plt.figure(figsize=(10, 6))
    plt.plot(range(1, len(minObjective) + 1), minObjective, label='Minimum Objective Function')
    plt.plot(range(1, len(averageObjective) + 1), averageObjective, label='Rata-rata Objective Function')
    plt.xlabel('Iterasi')
    plt.ylabel('Nilai Objective Function')
    plt.title('Plot Nilai Objective Function terhadap Jumlah Iterasi')
    plt.legend()
    plt.grid(True)
    plt.show()  
# # Main

# cube = makeCube()
# initialStateRandom(cube)

# objectiveBefore = objectiveFunction(cube)

# finalCube, objectiveAfter, iterationSum, duration, bestCube, lastMin, lastAvg = geneticAlgorithm(cube, 3, 10)
# print("\n\nKeterangan : ")
# print(f"\n-) objective function terendah dari populasi terakhir adalah {lastMin}\n")
# print(f"-) ojective function rata-rata dari populasi terakhir adalah {lastAvg}\n")
# print(f"-) objective function terbaik dari seluruh populasi adalah {objectiveAfter}\n")
# print(f"-) jumlah iterasi yang dilakukan adalah {iterationSum}\n")
# print("-) waktu =", duration)


# print("-------------------------------------------------------------------------------")
# print("State cube terakhir")
# printCube(finalCube)

# print(f" \n\nobjective function sebelum yaitu {objectiveBefore}")
# print(f"\njumlah iterasi yang dilakukan adalah {iterationSum} \n")
# print(f"\nobjective function terbaik adalah {objectiveAfter} \n")
# print(f"\nState Cube yang terbaik yaitu \n")
# printCube(bestCube)
# print("\nwaktu = ", duration)




# population = []
# populationSize = 5
# population = generateRandomPopulation(populationSize)
# fitnessScore = []
# fitnessSum = 0
# fitnessPercentage = []
# sumPercentage = 0
# wheelRange = []
# for i in range (populationSize) :
#         individu2 = convertTo3D(population[i])
#         fitness = 1 / (1 + objectiveFunction(individu2))
#         fitnessScore.append(fitness)
#         fitnessSum += fitness
       
# for i in range (len(fitnessScore)) :
#     fitnessPercent = (fitnessScore[i] / fitnessSum) * 100
#     fitnessPercentage.append(fitnessPercent)
#     sumPercentage += fitnessPercent
#     wheelRange.append(sumPercentage)
# print(" fitness score = ")
# print(fitnessScore)
# print(" fitness percen = ")
# print(fitnessPercentage)
# print(wheelRange)

# parent = spinWheelSelection(population, wheelRange)
# # print(" Parent yang terpilih adalah : ")
# # print(parent)
# print("Child yang terpilih : ")
# child = []
# for i in range (populationSize) :
#         child = crossOver(populationSize, population)
#         if(child != None) :
#             child.append(child)
# printPopulationDefault(child)
# for i in range (len(child)) :
#     child[i] = mutate(child[i], 0.3)
# printPopulationDefault(child)


#--------------------------------------------

# individu = []
# individu = list(range(1, 126))
# print("sebelum")
# printIndividuAsCube(individu)
# print()

# individu2 = convertTo3D(individu)
# print("setlah reshape")
# printCube(individu2)

#--------------------------------------------


# population = []
# population = generateRandomPopulation(5)
# printPopulation(population)

# population = generateRandomPopulation(3)
# printPopulationAsCube(population)
# printIndividuAsCube(individu)
# print
# print("##############################################")
# print()
# cube = makeCube()
# printCube(cube)
# numbers = list(range(1, 126))    
# print(numbers)
# print("___________________________________")
# print("Urutan angka acak dari 1 hingga 125:")
# random.shuffle(numbers)
# print(numbers)    