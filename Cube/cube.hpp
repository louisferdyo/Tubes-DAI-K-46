#ifndef CUBE_HPP
#define CUBE_HPP

#include<iostream>
#include<string>
using namespace std;

#define cubeSize 5
#define magicNumber (cubeSize*(cubeSize*cubeSize*cubeSize+1))/2

void makeCube(int cube[cubeSize][cubeSize][cubeSize]);
void printCube(int cube[cubeSize][cubeSize][cubeSize]);
void initiateRandomState(int cube[cubeSize][cubeSize][cubeSize]);
int objectiveFunction(int cube[cubeSize][cubeSize][cubeSize]);

#endif