from steepestAscent import steepestAscent
from steepestAscent import makeCube
from steepestAscent import objectiveFunction
from steepestAscent import printCube
from steepestAscent import initialStateRandom
from simulatedAnealing import simulatedAnnealing
from geneticAlgorithm import geneticAlgorithm
from randomRestart import randomRestart
from stochastic import stochastic
from sidewaysMove import sidewaysMove


cube = makeCube()
initialStateRandom(cube)
printCube(cube)
p1 = objectiveFunction(cube)
print("\nobjective function awal = ", p1)

print("Pilih algoritma yang ingin dicoba : ")
print("1: Hill Climbing")
print("2: Simulated Annealing")
print("3: Genetic Algorithm")
pilihan = int(input("Masukan pilihan: "))


if pilihan == 1 :
    print("Pilih algoritma hill climbing:")
    print("1: Stepest Ascent Hill Climbing")
    print("2: Sideways Move Hill Climbing")
    print("3: Random Restart Hill Climbing")
    print("4: Stochastic Hill Climbing")

    h = int(input("Masukan pilihan"))

    if h == 1 :
        finalCube, iterationSum, duration = steepestAscent(cube)
        printCube(finalCube)
        p2 = objectiveFunction(finalCube)
        print("\nobjective function akhir = ", p2)
        print("\nbanyaknya iterasi yang dilakukan = ", iterationSum)
        print("waktu = ", duration)
    elif h == 2 :
        finalCube, iterationSum, duration, sidewaysSum = sidewaysMove(cube, 10)
        printCube(finalCube)
        p2 = objectiveFunction(finalCube)
        print("\nobjective function akhir = ", p2)
        print("\nbanyaknya iterasi yang dilakukan = ", iterationSum)
        print("\nbanyaknya sideways move yang dilakukan = ", sidewaysSum)
        print("waktu = ", duration)
    elif h == 3 :
        finalCube, restartCount, iterationPerRestart, duration = randomRestart(cube, 10)
        printCube(finalCube)
        p2 = objectiveFunction(finalCube)
        print("\nobjective function akhir = ", p2)
        print("waktu = ", duration)
        print(f"Cube di restart sebanyak {restartCount}")
        print(f"Iterasi setiap restart adalah sebagai berikut {iterationPerRestart}")
    elif h == 4 :
        finalCube, duration = stochastic(cube, 10)
        printCube(finalCube)
        p2 = objectiveFunction(finalCube)
        print("\nobjective function akhir = ", p2)
        print("waktu = ", duration)

elif pilihan == 2 :
    finalCube, stuck, duration = simulatedAnnealing(cube, 10, 0.5, 5)
    printCube(finalCube)
    p2 = objectiveFunction(finalCube)
    print("\nobjective function akhir = ", p2)
    print("\nfrekuensi terkena stuck yaitu = ", stuck)
    print("waktu = ", duration)

elif pilihan == 3 :
    finalCube, objectiveAfter, iterationSum, duration, bestCube = geneticAlgorithm(cube, 10, 10)
    print("State cube terakhir")
    printCube(finalCube)
    print(f"\njumlah iterasi yang dilakukan adalah {iterationSum} \n")
    print(f"\nobjective function terbaik adalah {objectiveAfter} \n")
    print(f"\nState Cube yang terbaik yaitu \n")
    printCube(bestCube)
    print("\nwaktu = ", duration)

else :
    print("Input Invalid")