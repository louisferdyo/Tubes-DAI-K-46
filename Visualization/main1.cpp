#include <cmath>
#include <string.h> 
#include <GL/glut.h>
#include <GL/gl.h>
#include <GL/glu.h> 
#include <stdio.h> 

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

float angleX = 0.0f;
float angleY = 0.0f;
int lastX, lastY;     

void Init() {
    glClearColor(0, 0, 0, 1);
    glEnable(GL_DEPTH_TEST);

    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    gluPerspective(45.0, 1.0, 1.0, 100.0); 
    glMatrixMode(GL_MODELVIEW);
}

void Face(GLfloat A[], GLfloat B[], GLfloat C[], GLfloat D[]){
    glBegin(GL_POLYGON);
        glVertex3fv(A);
        glVertex3fv(B);
        glVertex3fv(C);
        glVertex3fv(D);
    glEnd();
}

void Cube(GLfloat V0[], GLfloat V1[], GLfloat V2[], GLfloat V3[], GLfloat V4[], GLfloat V5[], GLfloat V6[], GLfloat V7[]){
    glColor3f(1,0,0); 
    Face(V0, V1, V2, V3);

    glColor3f(0,1,0); 
    Face(V4, V5, V6, V7);

    glColor3f(1,0,1); 
    Face(V1, V2, V6, V5);

    glColor3f(0,0,1); 
    Face(V0, V3, V7, V4);

    glColor3f(1,1,0); 
    Face(V0, V1, V5, V4);

    glColor3f(0,1,1); 
    Face(V3, V2, V6, V7);
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

    float camX = 5.0f * cos(angleX * M_PI / 180.0f) * sin(angleY * M_PI / 180.0f); 
    float camY = 5.0f * sin(angleX * M_PI / 180.0f);
    float camZ = 5.0f * cos(angleX * M_PI / 180.0f) * cos(angleY * M_PI / 180.0f);

    gluLookAt(camX, camY, camZ, 0.0f, 0.0f, 0.0f, 0.0f, 1.0f, 0.0f);
    Cube(V[0], V[1], V[2], V[3], V[4], V[5], V[6], V[7]);
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

    glutCreateWindow("Magic Cubes's");
    Init();
    glutDisplayFunc(Draw);
    glutMouseFunc(mousePress);
    glutMotionFunc(mouseMotion);

    glutMainLoop();
    return 0;
}
