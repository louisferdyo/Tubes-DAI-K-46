from steepestAscent import steepestAscent, makeCube, objectiveFunction, printCube, initialStateRandom
from simulatedAnealing import simulatedAnnealing
from geneticAlgorithm import geneticAlgorithm
from randomRestart import randomRestart
from stochastic import stochastic
from sidewaysMove import sidewaysMove
from visual import showInitiateCube, showFinalCube


cube = makeCube()


print("Pilih State Awal Cube : ")
print("1: Berurutan")
print("2: Random")

stateAwal = int(input("Masukkan Kondisi State Awal : "))
if stateAwal == 2:
    initialStateRandom(cube)

printCube(cube)
showInitiateCube(cube)
p1 = objectiveFunction(cube)
print("\n\nObjective Function Awal =", p1)


print("\n\nPilih Algoritma yang Digunakan: ")
print("1: Hill Climbing")
print("2: Simulated Annealing")
print("3: Genetic Algorithm")
pilihan = int(input("Masukkan pilihan: "))


if pilihan == 1:
    print("\n\nPilih Algoritma Hill Climbing :")
    print("1: Stepest Ascent Hill Climbing")
    print("2: Sideways Move Hill Climbing")
    print("3: Random Restart Hill Climbing")
    print("4: Stochastic Hill Climbing")

    h = int(input("Masukkan Pilihan : "))

    if h == 1:
        finalCube, iterationSum, duration = steepestAscent(cube)
        showFinalCube(finalCube)
        printCube(finalCube)
        p2 = objectiveFunction(finalCube)
        print("\n\nKeterangan : ")
        print("\n-> Objective function akhir =", p2)
        print("\n-> Banyak iterasi yang dilakukan =", iterationSum)
        print("\n-> Waktu =", duration)
        print()
        
    elif h == 2:
        maxSide = int(input("\n Masukkan Jumlah Sideways Move Maksimal : "))
        finalCube, iterationSum, duration, sidewaysSum = sidewaysMove(cube, maxSide)
        showFinalCube(finalCube)
        printCube(finalCube)
        p2 = objectiveFunction(finalCube)
        print("\n\nKeterangan : ")
        print("\n-> Objective function akhir =", p2)
        print("\n-> Banyak iterasi yang dilakukan =", iterationSum)
        print("\n-> Banyak sideways move yang dilakukan =", sidewaysSum)
        print("\n-> Waktu =", duration)
        print()
        
    elif h == 3:
        maxRes = int(input("\n Masukkan Jumlah Restart Maksimal : "))
        finalCube, restartCount, iterationPerRestart, duration = randomRestart(cube, maxRes)
        showFinalCube(finalCube)
        printCube(finalCube)
        p2 = objectiveFunction(finalCube)
        print("\n\nKeterangan : ")
        print("\n-> Objective function akhir =", p2)
        print(f"\n-> Cube di restart sebanyak {restartCount}")
        print(f"\n-> Iterasi setiap restart adalah sebagai berikut {iterationPerRestart}")
        print("\n-> Waktu =", duration)
        print()
        
    elif h == 4:
        maxIterate = int(input("\n Masukkan Jumlah Iterasi Maksimal : "))
        finalCube, duration, iterationSum = stochastic(cube, maxIterate)
        showFinalCube(finalCube)
        printCube(finalCube)
        p2 = objectiveFunction(finalCube)
        print("\n\nKeterangan : ")
        print("\n-> Objective function akhir =", p2)
        print("\n-> Banyak iterasi yang dilakukan =", iterationSum)
        print("\n-> Waktu =", duration)
        print()

elif pilihan == 2:
    temp = int(input("\n Masukkan Temperatur Awal : "))
    coolRate = float(input("\n Masukkan Koefisien Penurunan Temperatur : "))
    thres = float(input("\n Masukkan Batas Probabilitas (parameter pertukaran state pada perhitungan deltaE / T) : "))
    finalCube, stuck, duration = simulatedAnnealing(cube, temp, coolRate, thres)
    showFinalCube(finalCube)
    printCube(finalCube)
    p2 = objectiveFunction(finalCube)
    print("\n\nKeterangan : ")
    print("\n-> Objective function akhir =", p2)
    print("\n-> Frekuensi terkena stuck yaitu =", stuck)
    print("\n-> Waktu =", duration)
    print()

elif pilihan == 3:
    populasi = int(input("\n Masukkan Jumlah Populasi : "))
    maxIterasi = int(input("\n Masukkan Jumlah Iterasi Maksimal: "))
    finalCube, objectiveAfter, iterationSum, duration, bestCube, lastMin, lastAvg = geneticAlgorithm(cube, populasi, maxIterasi)
    print("\n\nState cube terakhir")
    showFinalCube(finalCube)
    printCube(finalCube)

    print("\n\n\nBest State cube")
    showFinalCube(bestCube)
    printCube(bestCube)

    print("\n\nKeterangan : ")
    print(f"\n-> Objective function terendah dari populasi terakhir adalah {lastMin}\n")
    print(f"-> Ojective function rata-rata dari populasi terakhir adalah {lastAvg}\n")
    print(f"-> Objective function terbaik dari seluruh populasi adalah {objectiveAfter}\n")
    print(f"-> Jumlah iterasi yang dilakukan adalah {iterationSum}\n")
    print("-> Waktu =", duration)
    print()


else:
    print("Input Invalid")