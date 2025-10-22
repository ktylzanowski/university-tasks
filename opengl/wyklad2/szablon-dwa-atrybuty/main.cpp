#include <stdio.h>
#include <GL/glew.h>
#include <GL/freeglut.h>
#include <stdlib.h>
#include <time.h>
#include "utilities.hpp"

#define N 100
#define VERTS_PER_QUAD 6

GLuint gProgram = 0;
GLuint vaoSolid = 0, vaoGradient = 0;
GLuint vboCoord = 0, vboColorSolid = 0, vboColorGrad = 0;

int gScene = 1;

GLfloat vertices[N * VERTS_PER_QUAD * 2];
GLfloat colorsSolid[N * VERTS_PER_QUAD * 3];
GLfloat colorsGrad[N * VERTS_PER_QUAD * 3];

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

static void SetupVAO(GLuint& vao, GLuint coordVBO, GLuint colorVBO)
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

    BuildGeometry();
    BuildColors();

    gProgram = glCreateProgram();
    glAttachShader(gProgram, LoadShader(GL_VERTEX_SHADER,   "vertex.glsl"));
    glAttachShader(gProgram, LoadShader(GL_FRAGMENT_SHADER, "fragment.glsl"));
    LinkAndValidateProgram(gProgram);

    glGenBuffers(1, &vboCoord);
    glBindBuffer(GL_ARRAY_BUFFER, vboCoord);
    glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);

    glGenBuffers(1, &vboColorSolid);
    glBindBuffer(GL_ARRAY_BUFFER, vboColorSolid);
    glBufferData(GL_ARRAY_BUFFER, sizeof(colorsSolid), colorsSolid, GL_STATIC_DRAW);

    glGenBuffers(1, &vboColorGrad);
    glBindBuffer(GL_ARRAY_BUFFER, vboColorGrad);
    glBufferData(GL_ARRAY_BUFFER, sizeof(colorsGrad), colorsGrad, GL_STATIC_DRAW);

    SetupVAO(vaoSolid,    vboCoord, vboColorSolid);
    SetupVAO(vaoGradient, vboCoord, vboColorGrad);

    glClearColor(0.92f, 0.92f, 0.95f, 1.0f);
}

void DrawSceneSolid()
{
    glUseProgram(gProgram);
    glBindVertexArray(vaoSolid);
    glDrawArrays(GL_TRIANGLES, 0, N * VERTS_PER_QUAD);
    glBindVertexArray(0);
    glUseProgram(0);
}

void DrawSceneGradient()
{
    glUseProgram(gProgram);
    glBindVertexArray(vaoGradient);
    glDrawArrays(GL_TRIANGLES, 0, N * VERTS_PER_QUAD);
    glBindVertexArray(0);
    glUseProgram(0);
}

void DisplayScene()
{
    glClear(GL_COLOR_BUFFER_BIT);

    switch (gScene)
    {
        case 1:
            DrawSceneSolid();
            break;
        case 2:
        case 3:
            DrawSceneGradient();
            break;
    }

    glutSwapBuffers();
}

void Reshape(int width, int height)
{
    glViewport(0, 0, width, height);
}

void Keyboard(unsigned char key, int, int)
{
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
    }
}

int main(int argc, char *argv[])
{
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
    glutInitContextVersion(3, 3);
    glutInitContextProfile(GLUT_CORE_PROFILE);
    glutInitWindowSize(800, 800);
    glutCreateWindow("Kwadraty: pelny kolor / gradient / gradient2");

    glutDisplayFunc(DisplayScene);
    glutReshapeFunc(Reshape);
    glutKeyboardFunc(Keyboard);

    glewExperimental = GL_TRUE;
    GLenum err = glewInit();
    if (GLEW_OK != err)
    {
        printf("GLEW Error\n");
        return 1;
    }

    if (!GLEW_VERSION_3_3)
    {
        printf("Brak OpenGL 3.3!\n");
        return 1;
    }

    Initialize();
    glutMainLoop();

    glDeleteVertexArrays(1, &vaoSolid);
    glDeleteVertexArrays(1, &vaoGradient);
    glDeleteBuffers(1, &vboCoord);
    glDeleteBuffers(1, &vboColorSolid);
    glDeleteBuffers(1, &vboColorGrad);
    glDeleteProgram(gProgram);

    return 0;
}
