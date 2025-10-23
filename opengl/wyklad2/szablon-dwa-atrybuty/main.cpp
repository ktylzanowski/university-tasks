#include <stdio.h>
#include <GL/glew.h>
#include <GL/freeglut.h>
#include <stdlib.h>
#include <time.h>
#include "utilities.hpp"
#include "house.h"

#define N 100
#define VERTS_PER_QUAD 6
#define VERTS_PER_TRI  3

GLuint progSquares = 0;
GLuint progHouse   = 0;

GLuint vaoSolid = 0, vaoGradient = 0;
GLuint vboCoord = 0, vboColorSolid = 0, vboColorGrad = 0;

GLuint vaoHouse = 0, vboHouse = 0;

GLint uOffsetLoc = -1, uResolutionLoc = -1, uFlipYLoc = -1, uScaleLoc = -1;

int   gScene   = 1;
int   gWinW    = 800, gWinH = 800;
float gOffsetX = 0.0f, gOffsetY = 0.0f;
float gScale   = 1.0f;
float gFlipY   = -1.0f;

GLfloat vertices[N * VERTS_PER_QUAD * 2];
GLfloat colorsSolid[N * VERTS_PER_QUAD * 3];
GLfloat colorsGrad [N * VERTS_PER_QUAD * 3];

void BuildGeometry()
{
    int v = 0;
    for (int k = 0; k < N; ++k)
    {
        float cx = -0.9f + 1.8f * (float)rand() / (float)RAND_MAX;
        float cy = -0.9f + 1.8f * (float)rand() / (float)RAND_MAX;
        float s  = 0.03f + 0.07f * (float)rand() / (float)RAND_MAX;

        float xL = cx - s, xR = cx + s;
        float yB = cy - s, yT = cy + s;

        vertices[v++] = xL; vertices[v++] = yB;
        vertices[v++] = xR; vertices[v++] = yB;
        vertices[v++] = xR; vertices[v++] = yT;

        vertices[v++] = xL; vertices[v++] = yB;
        vertices[v++] = xR; vertices[v++] = yT;
        vertices[v++] = xL; vertices[v++] = yT;
    }
}

void BuildColors()
{
    int c1 = 0;
    for (int k = 0; k < N; ++k)
    {
        float r = (float)rand() / (float)RAND_MAX;
        float g = (float)rand() / (float)RAND_MAX;
        float b = (float)rand() / (float)RAND_MAX;

        for (int j = 0; j < VERTS_PER_QUAD; ++j)
        {
            colorsSolid[c1++] = r;
            colorsSolid[c1++] = g;
            colorsSolid[c1++] = b;
        }
    }

    int c2 = 0;
    for (int i = 0; i < N * VERTS_PER_QUAD; ++i)
    {
        colorsGrad[c2++] = (float)rand() / (float)RAND_MAX;
        colorsGrad[c2++] = (float)rand() / (float)RAND_MAX;
        colorsGrad[c2++] = (float)rand() / (float)RAND_MAX;
    }
}

static void SetupVAO_Square(GLuint& vao, GLuint coordVBO, GLuint colorVBO)
{
    glGenVertexArrays(1, &vao);
    glBindVertexArray(vao);

    glBindBuffer(GL_ARRAY_BUFFER, coordVBO);
    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 0, (void*)0);
    glEnableVertexAttribArray(0);

    glBindBuffer(GL_ARRAY_BUFFER, colorVBO);
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, (void*)0);
    glEnableVertexAttribArray(1);

    glBindVertexArray(0);
}

void Initialize()
{
    srand((unsigned int)time(NULL));

    progSquares = glCreateProgram();
    glAttachShader(progSquares, LoadShader(GL_VERTEX_SHADER,   "vertex.glsl"));
    glAttachShader(progSquares, LoadShader(GL_FRAGMENT_SHADER, "fragment.glsl"));
    LinkAndValidateProgram(progSquares);

    progHouse = glCreateProgram();
    glAttachShader(progHouse, LoadShader(GL_VERTEX_SHADER,   "vertex_house.glsl"));
    glAttachShader(progHouse, LoadShader(GL_FRAGMENT_SHADER, "fragment_house.glsl"));
    LinkAndValidateProgram(progHouse);

    uOffsetLoc     = glGetUniformLocation(progHouse, "uOffset");
    uResolutionLoc = glGetUniformLocation(progHouse, "uResolution");
    uFlipYLoc      = glGetUniformLocation(progHouse, "uFlipY");
    uScaleLoc      = glGetUniformLocation(progHouse, "uScale");

    BuildGeometry();
    BuildColors();

    glGenBuffers(1, &vboCoord);
    glBindBuffer(GL_ARRAY_BUFFER, vboCoord);
    glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);

    glGenBuffers(1, &vboColorSolid);
    glBindBuffer(GL_ARRAY_BUFFER, vboColorSolid);
    glBufferData(GL_ARRAY_BUFFER, sizeof(colorsSolid), colorsSolid, GL_STATIC_DRAW);

    glGenBuffers(1, &vboColorGrad);
    glBindBuffer(GL_ARRAY_BUFFER, vboColorGrad);
    glBufferData(GL_ARRAY_BUFFER, sizeof(colorsGrad), colorsGrad, GL_STATIC_DRAW);

    SetupVAO_Square(vaoSolid,    vboCoord, vboColorSolid);
    SetupVAO_Square(vaoGradient, vboCoord, vboColorGrad);

    glGenVertexArrays(1, &vaoHouse);
    glBindVertexArray(vaoHouse);

    glGenBuffers(1, &vboHouse);
    glBindBuffer(GL_ARRAY_BUFFER, vboHouse);
    glBufferData(GL_ARRAY_BUFFER,
                 sizeof(float) * NUMBER_OF_VERTICES * 2,
                 (const void*)Mesh_Vertices,
                 GL_STATIC_DRAW);

    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 0, (void*)0);
    glEnableVertexAttribArray(0);

    glBindVertexArray(0);

    glClearColor(0.92f, 0.92f, 0.95f, 1.0f);
}

void DrawSceneSolid()
{
    glUseProgram(progSquares);
    glBindVertexArray(vaoSolid);
    glDrawArrays(GL_TRIANGLES, 0, N * VERTS_PER_QUAD);
    glBindVertexArray(0);
    glUseProgram(0);
}

void DrawSceneGradient()
{
    glUseProgram(progSquares);
    glBindVertexArray(vaoGradient);
    glDrawArrays(GL_TRIANGLES, 0, N * VERTS_PER_QUAD);
    glBindVertexArray(0);
    glUseProgram(0);
}

void DrawSceneHouse()
{
    glUseProgram(progHouse);

    glUniform2f(uOffsetLoc, gOffsetX, gOffsetY);
    glUniform2f(uResolutionLoc, (float)gWinW, (float)gWinH);
    glUniform1f(uFlipYLoc, gFlipY);
    glUniform1f(uScaleLoc, gScale);

    glBindVertexArray(vaoHouse);
    glDrawArrays(GL_TRIANGLES, 0, NUMBER_OF_VERTICES);
    glBindVertexArray(0);

    glUseProgram(0);
}

void DisplayScene()
{
    glClear(GL_COLOR_BUFFER_BIT);

    switch (gScene)
    {
        case 1: DrawSceneSolid();    break;
        case 2: DrawSceneGradient(); break;
        case 3: DrawSceneHouse();    break;
    }

    glutSwapBuffers();
}

void Reshape(int width, int height)
{
    gWinW = width  > 0 ? width  : 1;
    gWinH = height > 0 ? height : 1;
    glViewport(0, 0, gWinW, gWinH);
    glutPostRedisplay();
}

void Keyboard(unsigned char key, int, int)
{
    const float step = 0.05f;

    switch (key)
    {
        case 27:
        case 'x':
            glutLeaveMainLoop();
            break;

        case ' ':
            gScene = (gScene % 3) + 1;
            printf("Scene: %d\n", gScene);
            glutPostRedisplay();
            break;

        case 'w': case 'W':
            if (gScene == 3) { gOffsetY += step; glutPostRedisplay(); }
            break;
        case 's': case 'S':
            if (gScene == 3) { gOffsetY -= step; glutPostRedisplay(); }
            break;
        case 'a': case 'A':
            if (gScene == 3) { gOffsetX -= step; glutPostRedisplay(); }
            break;
        case 'd': case 'D':
            if (gScene == 3) { gOffsetX += step; glutPostRedisplay(); }
            break;

        case 'f': case 'F':
            if (gScene == 3) { gFlipY = (gFlipY > 0.0f) ? -1.0f : 1.0f; glutPostRedisplay(); }
            break;

        case 'r': case 'R':
            if (gScene == 3) { gOffsetX = gOffsetY = 0.0f; gScale = 1.0f; glutPostRedisplay(); }
            break;

        case '+':
            if (gScene == 3) { gScale *= 1.1f; glutPostRedisplay(); }
            break;
        case '-':
            if (gScene == 3) { gScale /= 1.1f; glutPostRedisplay(); }
            break;
    }
}

int main(int argc, char *argv[])
{
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
    glutInitContextVersion(3, 3);
    glutInitContextProfile(GLUT_CORE_PROFILE);
    glutInitWindowSize(800, 800);
    glutCreateWindow("Sceny: 1-solid, 2-gradient, 3-domek (WSAD)");

    glutDisplayFunc(DisplayScene);
    glutReshapeFunc(Reshape);
    glutKeyboardFunc(Keyboard);

    glewExperimental = GL_TRUE;
    GLenum err = glewInit();
    if (GLEW_OK != err) { printf("GLEW Error\n"); return 1; }
    if (!GLEW_VERSION_3_3) { printf("Brak OpenGL 3.3!\n"); return 1; }

    Initialize();
    glutMainLoop();

    glDeleteVertexArrays(1, &vaoSolid);
    glDeleteVertexArrays(1, &vaoGradient);
    glDeleteBuffers(1, &vboCoord);
    glDeleteBuffers(1, &vboColorSolid);
    glDeleteBuffers(1, &vboColorGrad);

    glDeleteVertexArrays(1, &vaoHouse);
    glDeleteBuffers(1, &vboHouse);

    glDeleteProgram(progSquares);
    glDeleteProgram(progHouse);

    return 0;
}
