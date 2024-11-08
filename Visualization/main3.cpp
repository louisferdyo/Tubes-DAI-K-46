#include <cmath>
#include <string.h> 
#include <GL/glut.h>
#include <GL/gl.h>
#include <GL/glu.h> 
#include <stdio.h> 
#include <stdlib.h>
#include <time.h>

#ifndef M_PI
#define M_PI 3.14
#endif

float angleX = 0.0f;
float angleY = 0.0f;
int lastX, lastY;

int cubeNumbers[5][5][5]; 

void shuffleNumbers() {
    int numbers[125];
    for (int i = 0; i < 125; ++i) {
        numbers[i] = i + 1;
    }

    srand(time(NULL));
    
    for (int i = 124; i > 0; --i) {
        int j = rand() % (i + 1);
        int temp = numbers[i];
        numbers[i] = numbers[j];
        numbers[j] = temp;
    }

    int idx = 0;
    for (int z = 0; z < 5; ++z) {
        for (int y = 0; y < 5; ++y) {
            for (int x = 0; x < 5; ++x) {
                cubeNumbers[z][x][y] = numbers[idx++];
            }
        }
    }
}

void Init() {
    glClearColor(0.0, 0.0, 0.0, 1.0); 
    glEnable(GL_DEPTH_TEST);      

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(45.0, 1.0, 1.0, 100.0); 
    glMatrixMode(GL_MODELVIEW);

    shuffleNumbers();
}

void Face(GLfloat A[], GLfloat B[], GLfloat C[], GLfloat D[]) {
    glBegin(GL_LINE_LOOP); 
        glVertex3fv(A);
        glVertex3fv(B);
        glVertex3fv(C);
        glVertex3fv(D);
    glEnd();
}

void Cube(GLfloat V0[], GLfloat V1[], GLfloat V2[], GLfloat V3[], GLfloat V4[], GLfloat V5[], GLfloat V6[], GLfloat V7[]) {
    Face(V0, V1, V2, V3);
    Face(V4, V5, V6, V7);
    Face(V1, V2, V6, V5);
    Face(V0, V3, V7, V4);
    Face(V0, V1, V5, V4);
    Face(V3, V2, V6, V7);
}

void renderBitmapString(float x, float y, float z, void *font, const char *string){
    int len = strlen(string);
    float offsetX = len * 0.07f; 
    glRasterPos3f(x - offsetX, y, z);
    while (*string){
        glColor3f(0.3,0.3,0.3);
        glutBitmapCharacter(font, *string);
        string++;
    }
}

void Draw() {
    GLfloat V[8][3] = {
        {-0.5, 0.5, 0.5}, 
        {0.5, 0.5, 0.5}, 
        {0.5, -0.5, 0.5}, 
        {-0.5, -0.5, 0.5},

        {-0.5, 0.5, -0.5}, 
        {0.5, 0.5, -0.5}, 
        {0.5, -0.5, -0.5}, 
        {-0.5, -0.5, -0.5}
    };

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
    glLoadIdentity();

    if (angleX > 89.0f) angleX = 89.0f;
    if (angleX < -89.0f) angleX = -89.0f;

    float camX = 23.0f * cos(angleX * M_PI / 180.0f) * sin(angleY * M_PI / 180.0f); 
    float camY = 23.0f * sin(angleX * M_PI / 180.0f);
    float camZ = 23.0f * cos(angleX * M_PI / 180.0f) * cos(angleY * M_PI / 180.0f);

    gluLookAt(camX, camY, camZ, 0.0f, 0.0f, 0.0f, 0.0f, 1.0f, 0.0f);    

    float offset = 2.0f;
    for (int x = -2; x <= 2; ++x) {
        for (int y = -2; y <= 2; ++y) {
            for (int z = -2; z <= 2; ++z) {
                GLfloat V[8][3] = {
                    {-0.5f + x * offset, 0.5f + y * offset, 0.5f + z * offset},
                    {0.5f + x * offset, 0.5f + y * offset, 0.5f + z * offset},
                    {0.5f + x * offset, -0.5f + y * offset, 0.5f + z * offset},
                    {-0.5f + x * offset, -0.5f + y * offset, 0.5f + z * offset},

                    {-0.5f + x * offset, 0.5f + y * offset, -0.5f + z * offset},
                    {0.5f + x * offset, 0.5f + y * offset, -0.5f + z * offset},
                    {0.5f + x * offset, -0.5f + y * offset, -0.5f + z * offset},
                    {-0.5f + x * offset, -0.5f + y * offset, -0.5f + z * offset}
                };

                Cube(V[0], V[1], V[2], V[3], V[4], V[5], V[6], V[7]);
                
                GLfloat centerX = (V[0][0] + V[6][0]) / 2.0f;
                GLfloat centerY = (V[0][1] + V[6][1]) / 2.0f;
                GLfloat centerZ = (V[0][2] + V[6][2]) / 2.0f;

                glPushMatrix(); 
                    glTranslatef(centerX, centerY, centerZ);
                    glRotatef(angleX, 1.0f, 0.0f, 0.0f); 
                    glRotatef(angleY, 0.0f, 1.0f, 0.0f);
                    glTranslatef(-centerX, -centerY, -centerZ);
                    
                    glColor3f(1, 0, 0);
                    char numStr[4];
                    sprintf(numStr, "%d", cubeNumbers[z + 2][x + 2][y + 2]);
                    renderBitmapString(centerX, centerY, centerZ, GLUT_BITMAP_HELVETICA_12, numStr);
                glPopMatrix();
            }
        }
    }

    glutSwapBuffers();
}

void mouseMotion(int x, int y) {
    int deltaX = x - lastX;
    int deltaY = y - lastY;
    angleY -= deltaX * 0.2f;
    angleX += deltaY * 0.2f;
    lastX = x;
    lastY = y;
    glutPostRedisplay();
}

void mousePress(int button, int state, int x, int y) {
    if (state == GLUT_DOWN) {
        lastX = x;
        lastY = y;
    }
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitWindowPosition(350, 20);
    glutInitWindowSize(600, 600);
    glutInitDisplayMode(GLUT_RGB | GLUT_DOUBLE | GLUT_DEPTH);

    glutCreateWindow("Magic Cube Visualization");
    Init();
    glutDisplayFunc(Draw);
    glutMouseFunc(mousePress);
    glutMotionFunc(mouseMotion);

    glutMainLoop();
    return 0;
}
