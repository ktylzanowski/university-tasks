#include <stdio.h>
#include <GL/glew.h>
#include <GL/freeglut.h>
#include <stdlib.h>
#include <time.h>
#include "utilities.hpp"

GLuint idProgram;
GLuint idVAO;
GLuint idVBO_coord;
GLuint idVBO_color;
#define N 100

GLfloat vertices[N * 2 * 6];

GLfloat colors[N * 3 * 6];

void DisplayScene()
{
	glClear(GL_COLOR_BUFFER_BIT);

	glUseProgram(idProgram);

	glBindVertexArray(idVAO);
	glDrawArrays(GL_TRIANGLES, 0, 6 * N);
	glBindVertexArray(0);

	glUseProgram(0);

	glutSwapBuffers();
}

void Initialize()
{
    glGenVertexArrays(1, &idVAO);
    glBindVertexArray(idVAO);

 
    glGenBuffers(1, &idVBO_coord);
    glBindBuffer(GL_ARRAY_BUFFER, idVBO_coord);

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

    glBufferData(GL_ARRAY_BUFFER, sizeof(vertices), vertices, GL_STATIC_DRAW);
    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 0, NULL);
    glEnableVertexAttribArray(0);

    glGenBuffers(1, &idVBO_color);
    glBindBuffer(GL_ARRAY_BUFFER, idVBO_color);

    int c = 0;
    for (int k = 0; k < N; ++k)
    {
        float r = (float)rand() / (float)RAND_MAX;
        float g = (float)rand() / (float)RAND_MAX;
        float b = (float)rand() / (float)RAND_MAX;

        for (int j = 0; j < 6; ++j)
        {
            colors[c++] = r;
            colors[c++] = g;
            colors[c++] = b;
        }
    }

    glBufferData(GL_ARRAY_BUFFER, sizeof(colors), colors, GL_STATIC_DRAW);
    glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 0, NULL);
    glEnableVertexAttribArray(1);

    glBindVertexArray(0);

    idProgram = glCreateProgram();
    glAttachShader(idProgram, LoadShader(GL_VERTEX_SHADER, "vertex.glsl"));
    glAttachShader(idProgram, LoadShader(GL_FRAGMENT_SHADER, "fragment.glsl"));
    LinkAndValidateProgram(idProgram);

    glClearColor(0.9f, 0.9f, 0.9f, 1.0f);
}

void Reshape(int width, int height)
{
	glViewport(0, 0, width, height);
}

void Keyboard(unsigned char key, int x, int y)
{
	switch (key)
	{
	case 27:
		glutLeaveMainLoop();
		break;

	case ' ':
		printf("SPACE!\n");
		glutPostRedisplay();
		break;

	case 'x':
		glutLeaveMainLoop();
		break;
	}
}

int main(int argc, char *argv[])
{
	srand(time(NULL));
	glutInit(&argc, argv);
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
	glutInitContextVersion(3, 3);
	glutInitContextProfile(GLUT_CORE_PROFILE);
	glutInitWindowSize(500, 500);
	glutCreateWindow("Szablon programu w OpenGL");
	glutDisplayFunc(DisplayScene);
	glutReshapeFunc(Reshape);
	glutKeyboardFunc(Keyboard);

	glewExperimental = GL_TRUE;
	GLenum err = glewInit();
	if (GLEW_OK != err)
	{
		printf("GLEW Error\n");
		exit(1);
	}

	if (!GLEW_VERSION_3_3)
	{
		printf("Brak OpenGL 3.3!\n");
		exit(1);
	}

	Initialize();

	glutMainLoop();

	glDeleteProgram(idProgram);
	glDeleteVertexArrays(1, &idVBO_coord);
	glDeleteVertexArrays(1, &idVAO);

	return 0;
}
