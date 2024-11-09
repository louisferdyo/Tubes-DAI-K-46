#include <iostream>
#include <vector>
#include <algorithm>
#include <ctime>
#include <cstdlib>
#include <cmath>
#include <climits> 
#include <array>

using namespace std;
using Cube = array<array<array<int, 5>, 5>, 5>;

Cube makeCube() {
    Cube cube;
    int num = 1;
    for (int i = 0; i < 5; ++i) {
        for (int j = 0; j < 5; ++j) {
            for (int k = 0; k < 5; ++k) {
                cube[i][j][k] = num++;
            }
        }
    }
    return cube;
}

void printCube(const Cube &cube) {
    cout << "Sisi ke sumbu x\n";
    for (int i = 0; i < 5; ++i) {
        cout << "\n\n----- Sisi ke-" << i + 1 << "------\n";
        for (int j = 0; j < 5; ++j) {
            cout << "\n";
            for (int k = 0; k < 5; ++k) {
                cout << cube[i][j][k] << " | ";
            }
        }
    }

    cout << "\n\n-----------------------------------------------\n";
    cout << "Sisi ke sumbu y\n";
    for (int j = 0; j < 5; ++j) {
        cout << "\n\n----- Sisi ke-" << j + 1 << "------\n";
        for (int k = 0; k < 5; ++k) {
            cout << "\n";
            for (int i = 0; i < 5; ++i) {
                cout << cube[i][j][k] << " | ";
            }
        }
    }

    cout << "\n\n-----------------------------------------------\n";
    cout << "Sisi ke sumbu z\n";
    for (int k = 0; k < 5; ++k) {
        cout << "\n\n----- Sisi ke-" << k + 1 << "------\n";
        for (int i = 0; i < 5; ++i) {
            cout << "\n";
            for (int j = 0; j < 5; ++j) {
                cout << cube[i][j][k] << " | ";
            }
        }
    }
    cout << "\n";
}

int objectiveFunction(const Cube &cube) {
    int errorSum = 0;
    const int magicNumber = 315;
    int xSum, ySum, zSum;
    int diagonalXSum, contDiagonalXSum;
    int diagonalYSum, contDiagonalYSum;
    int diagonalZSum, contDiagonalZSum;
    int spaceDiaSum_a = 0, spaceDiaSum_b = 0, spaceDiaSum_c = 0, spaceDiaSum_d = 0;
    for (int j = 0; j < 5; ++j) {
        for (int k = 0; k < 5; ++k) {
            xSum = 0;
            for (int i = 0; i < 5; ++i)
                xSum += cube[i][j][k];
            errorSum += abs(xSum - magicNumber);
        }
    }

    for (int k = 0; k < 5; ++k) {
        for (int i = 0; i < 5; ++i) {
            ySum = 0;
            for (int j = 0; j < 5; ++j)
                ySum += cube[i][j][k];
            errorSum += abs(ySum - magicNumber);
        }
    }

    for (int i = 0; i < 5; ++i) {
        for (int j = 0; j < 5; ++j) {
            zSum = 0;
            for (int k = 0; k < 5; ++k)
                zSum += cube[i][j][k];
            errorSum += abs(zSum - magicNumber);
        }
    }

    for (int i = 0; i < 5; ++i) {
        diagonalXSum = contDiagonalXSum = 0;
        for (int x = 0; x < 5; ++x) {
            diagonalXSum += cube[i][x][x];
            contDiagonalXSum += cube[i][4 - x][x];
        }
        errorSum += abs(diagonalXSum - magicNumber) + abs(contDiagonalXSum - magicNumber);
    }

    for (int j = 0; j < 5; ++j) {
        diagonalYSum = contDiagonalYSum = 0;
        for (int y = 0; y < 5; ++y) {
            diagonalYSum += cube[y][j][y];
            contDiagonalYSum += cube[y][j][4 - y];
        }
        errorSum += abs(diagonalYSum - magicNumber) + abs(contDiagonalYSum - magicNumber);
    }

    for (int k = 0; k < 5; ++k) {
        diagonalZSum = contDiagonalZSum = 0;
        for (int z = 0; z < 5; ++z) {
            diagonalZSum += cube[z][z][k];
            contDiagonalZSum += cube[z][4 - z][k];
        }
        errorSum += abs(diagonalZSum - magicNumber) + abs(contDiagonalZSum - magicNumber);
    }

    for (int a = 0; a < 5; ++a) spaceDiaSum_a += cube[a][4 - a][a];
    errorSum += abs(spaceDiaSum_a - magicNumber);

    for (int b = 0; b < 5; ++b) spaceDiaSum_b += cube[4 - b][4 - b][b];
    errorSum += abs(spaceDiaSum_b - magicNumber);

    for (int c = 0; c < 5; ++c) spaceDiaSum_c += cube[4 - c][4 - c][4 - c];
    errorSum += abs(spaceDiaSum_c - magicNumber);

    for (int d = 0; d < 5; ++d) spaceDiaSum_d += cube[d][4 - d][4 - d];
    errorSum += abs(spaceDiaSum_d - magicNumber);

    return errorSum;
}

void initialStateRandom(Cube &cube) {
    vector<int> arrayAngka;
    arrayAngka.reserve(125);
    for (int i = 1; i <= 125; ++i) arrayAngka.push_back(i);
    srand(time(0));
    random_shuffle(arrayAngka.begin(), arrayAngka.end());
    int index = 0;
    for (int i = 0; i < 5; ++i) {
        for (int j = 0; j < 5; ++j) {
            for (int k = 0; k < 5; ++k) {
                cube[i][j][k] = arrayAngka[index++];
            }
        }
    }
}

Cube findBestNeighbor(Cube cube) {
    Cube bestCube = cube;
    int bestValue = objectiveFunction(cube);
    for (int i = 0; i < 5; ++i) {
        for (int j = 0; j < 5; ++j) {
            for (int k = 0; k < 5; ++k) {
                for (int l = 0; l < 5; ++l) {
                    for (int m = 0; m < 5; ++m) {
                        for (int n = 0; n < 5; ++n) {
                            if (i == l && j == m && k == n) continue;
                            swap(cube[i][j][k], cube[l][m][n]);
                            int value = objectiveFunction(cube);
                            if (value < bestValue) {
                                bestCube = cube;
                                bestValue = value;
                            }
                            swap(cube[i][j][k], cube[l][m][n]);
                        }
                    }
                }
            }
        }
    }
    return bestCube;
}

Cube steepestAscent(Cube cube) {
    bool condition = true;
    while (condition) {
        int currentValue = objectiveFunction(cube);
        Cube neighborCube = findBestNeighbor(cube);
        int neighborValue = objectiveFunction(neighborCube);
        if (neighborValue < currentValue) {
            cube = neighborCube;
        } else {
            condition = false;
        }
    }
    return cube;
}

int main() {
    Cube cube = makeCube();
    printCube(cube);
    cout << "\n\n\nXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX\n\n";
    initialStateRandom(cube);
    printCube(cube);
    int initialObjective = objectiveFunction(cube);
    cout << "\nObjective function awal = " << initialObjective << "\n";
    clock_t startTime = clock();
    Cube finalCube = steepestAscent(cube);
    clock_t endTime = clock();
    int finalObjective = objectiveFunction(finalCube);
    cout << "\nObjective function akhir = " << finalObjective << "\n";
    cout << "Waktu = " << double(endTime - startTime) / CLOCKS_PER_SEC << " seconds\n";

    return 0;
}
