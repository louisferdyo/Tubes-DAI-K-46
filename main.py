from steepestAscent import steepestAscent, makeCube, objectiveFunction, printCube, initialStateRandom
from simulatedAnealing import simulatedAnnealing
from geneticAlgorithm import geneticAlgorithm
from randomRestart import randomRestart
from stochastic import stochastic
from sidewaysMove import sidewaysMove


cube = makeCube()


print("Pilih State Awal Cube : ")
print("1: Berurutan")
print("2: Random")

stateAwal = int(input("Masukkan Kondisi State Awal : "))
if stateAwal == 2:
    initialStateRandom(cube)


printCube(cube)
p1 = objectiveFunction(cube)
print("\n\nObjective function awal =", p1)


print("\n\nPilih algoritma yang ingin dicoba : ")
print("1: Hill Climbing")
print("2: Simulated Annealing")
print("3: Genetic Algorithm")
pilihan = int(input("Masukkan pilihan: "))


if pilihan == 1:
    print("Pilih algoritma hill climbing:")
    print("1: Stepest Ascent Hill Climbing")
    print("2: Sideways Move Hill Climbing")
    print("3: Random Restart Hill Climbing")
    print("4: Stochastic Hill Climbing")

    h = int(input("Masukkan pilihan: "))

    if h == 1:
        finalCube, iterationSum, duration = steepestAscent(cube)
        printCube(finalCube)
        p2 = objectiveFunction(finalCube)
        print("\n\nKeterangan : ")
        print("\n-) objective function akhir =", p2)
        print("\n-) banyaknya iterasi yang dilakukan =", iterationSum)
        print("\n-) waktu =", duration)
        
    elif h == 2:
        maxSide = int(input("\n Masukkan jumlah ideways Move maksimal : "))
        finalCube, iterationSum, duration, sidewaysSum = sidewaysMove(cube, maxSide)
        printCube(finalCube)
        p2 = objectiveFunction(finalCube)
        print("\n\nKeterangan : ")
        print("\n-) objective function akhir =", p2)
        print("\n-) banyaknya iterasi yang dilakukan =", iterationSum)
        print("\n-) banyaknya sideways move yang dilakukan =", sidewaysSum)
        print("\n-) waktu =", duration)
        
    elif h == 3:
        maxRes = int(input("\n Masukkan jumlah restart maksimal : "))
        finalCube, restartCount, iterationPerRestart, duration = randomRestart(cube, maxRes)
        printCube(finalCube)
        p2 = objectiveFunction(finalCube)
        print("\n\nKeterangan : ")
        print("\n-) objective function akhir =", p2)
        print(f"\n-) Cube di restart sebanyak {restartCount}")
        print(f"\n-) Iterasi setiap restart adalah sebagai berikut {iterationPerRestart}")
        print("\n-) waktu =", duration)
        
    elif h == 4:
        maxIterate = int(input("\n Masukkan jumlah iterai maksimal : "))
        finalCube, duration, iterationSum = stochastic(cube, maxIterate)
        printCube(finalCube)
        p2 = objectiveFunction(finalCube)
        print("\n\nKeterangan : ")
        print("\n-) objective function akhir =", p2)
        print("\n-) banyaknya iterasi yang dilakukan =", iterationSum)
        print("\n-) waktu =", duration)

elif pilihan == 2:
    temp = int(input("\n Masukkan Temperature awal : "))
    coolRate = int(input("\n Masukkan koefisien penurunan temperatur : "))
    thres = int(input("\n Masukkan batas probabilitas (parameter pertukaran state pada perhitungan deltaE / T) : "))
    finalCube, stuck, duration = simulatedAnnealing(cube, temp, coolRate, thres)
    printCube(finalCube)
    p2 = objectiveFunction(finalCube)
    print(f"\n\nKeterangan : ")
    print("\n-) objective function akhir =", p2)
    print("\n-) frekuensi terkena stuck yaitu =", stuck)
    print("\n-) waktu =", duration)

elif pilihan == 3:
    populasi = int(input("\n Masukkan jumlah populasi : "))
    maxIterasi = int(input("\n Masukkan jumlah iterasi maksimal: "))
    finalCube, objectiveAfter, iterationSum, duration, bestCube, lastMin, lastAvg = geneticAlgorithm(cube, populasi, maxIterasi)
    print("\n\nState cube terakhir")
    printCube(finalCube)

    print("\n\n\nBest State cube")
    printCube(bestCube)

    print("\n\nKeterangan : ")
    print(f"\n-) objective function terendah dari populasi terakhir adalah {lastMin}\n")
    print(f"-) ojective function rata-rata dari populasi terakhir adalah {lastAvg}\n")
    print(f"-) objective function terbaik dari seluruh populasi adalah {objectiveAfter}\n")
    print(f"-) jumlah iterasi yang dilakukan adalah {iterationSum}\n")
    print("-) waktu =", duration)

else:
    print("Input Invalid")
