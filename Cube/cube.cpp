#include"cube.hpp"

// Buat Cube
void makeCube(int cube[cubeSize][cubeSize][cubeSize]){
    int num = 1;
    for(int x=0; x<cubeSize;++x){
        for(int y=0; y<cubeSize;++y){
            for(int z=0;z<cubeSize;++z){
                cube[x][y][z] = num++;
            }
        }
    }
}

// Cetak Cube
void printCube(int cube[cubeSize][cubeSize][cubeSize]){
    for(int x=0;x<cubeSize;++x){
        cout<<endl<<endl;
        cout<< "----- Sisi ke-" << x+1 << " ------" << endl;
        for(int y=0;y<cubeSize;++y){
            for(int z=0;z<cubeSize;++z){
                cout<<cube[x][y][z]<<"\t";
            }
            cout<<endl;
        }
    }
}

// Random State untuk Cube
void initiateRandomState(int cube[cubeSize][cubeSize][cubeSize]){
    int terpakai[125] = {0};
    int random;

    srand(time(NULL));
    for (int x=0;x<cubeSize;++x) {
        for (int y= 0;y<cubeSize;++y) {
            for (int z=0;z<cubeSize;++z) {
                do {
                    random = rand() % 125 + 1;
                } while (terpakai[random - 1] == 1);
                terpakai[random - 1] = 1;
                cube[x][y][z] = random;
            }
        }
    }    
}

// Menghitung Deviasi
int objectiveFunction(int cube[cubeSize][cubeSize][cubeSize]){
    int dev_total = 0;
    int dev_x, dev_y, dev_z;
    int dev_diag_1, dev_diag_2;
    int dev_diag_ruang_1, dev_diag_ruang_2, dev_diag_ruang_3, dev_diag_ruang_4;

    // Sumbu-X
    for(int y = 0; y < cubeSize; ++y){
        for(int z = 0; z < cubeSize; ++z){
            dev_x = 0;
            for(int x = 0; x < cubeSize; ++x){
                dev_x += cube[x][y][z];
            }
            dev_total += abs(dev_x - magicNumber);
        }
    }
    cout<<endl;

    // Sumbu-Y
    for (int x = 0; x < cubeSize; ++x) {
        for (int z = 0; z < cubeSize; ++z) {
            dev_y = 0;
            for (int y = 0; y < cubeSize; ++y) {
                dev_y += cube[x][y][z];
            }
            dev_total += abs(dev_y - magicNumber);
        }
    }
    cout<<endl;

    // Sumbu-Z
    for (int x = 0; x < cubeSize; ++x) {
        for (int y = 0; y < cubeSize; ++y) {
            dev_z = 0;
            for (int z = 0; z < cubeSize; ++z) {
                dev_z += cube[x][y][z];
            }
            dev_total += abs(dev_z - magicNumber);
        }
    }
    cout<<endl;

    // Diagonal X-Y
    for (int z = 0; z < cubeSize; ++z) {
        dev_diag_1 = 0;
        dev_diag_2 = 0;
        for (int i = 0; i < cubeSize; ++i) {
            dev_diag_1 += cube[i][i][z];  
        }
        dev_total += abs(dev_diag_1-magicNumber);
        for (int i = 0; i < cubeSize; ++i) {
            dev_diag_2 += cube[i][cubeSize-1-i][z];  
        }
        dev_total += abs(dev_diag_2-magicNumber);
    }

    // Diagonal Y-Z
    for (int x = 0; x < cubeSize; ++x) {
        dev_diag_1 = 0;
        dev_diag_2 = 0;
        for (int i = 0; i < cubeSize; ++i) {
            dev_diag_1 += cube[x][i][i];
        }
        dev_total += abs(dev_diag_1-magicNumber);
        for (int i = 0; i < cubeSize; ++i) {
            dev_diag_2 += cube[x][i][cubeSize-1-i];
        }
        dev_total += abs(dev_diag_2-magicNumber);
    }

    // Diagonal X-Z
    for (int y = 0; y < cubeSize; ++y) {
        dev_diag_1 = 0;
        dev_diag_2 = 0;
        for (int i = 0; i < cubeSize; ++i) {
            dev_diag_1 += cube[i][y][i];
        }
        dev_total += abs(dev_diag_1-magicNumber);
        for (int i = 0; i < cubeSize; ++i) {
            dev_diag_2 += cube[i][y][cubeSize-1-i];
        }
        dev_total += abs(dev_diag_2-magicNumber);
    }

    // diagonal ruang
    dev_diag_ruang_1 = 0;
    for (int i = 0; i < cubeSize; ++i) {
        dev_diag_ruang_1 += cube[i][i][i]; 
    }
    dev_total += abs(dev_diag_ruang_1 - magicNumber);

    dev_diag_ruang_2 = 0;
    for (int i = 0; i < cubeSize; ++i) {
        dev_diag_ruang_2 += cube[i][cubeSize-1-i][i];
    }
    dev_total += abs(dev_diag_ruang_2 - magicNumber);

    dev_diag_ruang_3 = 0;
    for (int i = 0; i < cubeSize; ++i) {
        dev_diag_ruang_3 += cube[cubeSize-1-i][i][i];
    }
    dev_total += abs(dev_diag_ruang_3 - magicNumber);

    dev_diag_ruang_4 = 0;
    for (int i = 0; i < cubeSize; ++i) {
        dev_diag_ruang_4 += cube[cubeSize-1-i][cubeSize-1-i][i];
    }
    dev_total += abs(dev_diag_ruang_4 - magicNumber);

    return dev_total;
}

