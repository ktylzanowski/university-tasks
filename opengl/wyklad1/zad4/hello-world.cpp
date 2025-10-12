// -------------------------------------------------
// Dwa potoki OpenGL: czerwony i zielony
// -------------------------------------------------
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include <GL/glew.h>
#include <GL/freeglut.h>

#define N 100

GLuint vao, vbo;
GLuint progRed, progGreen;
int gWidth = 500, gHeight = 500;

void DisplayScene();
void Initialize();
void Reshape(int width, int height);

static const char* VS_SIMPLE =
"#version 330 core\n"
"layout(location=0) in vec2 inPosition;\n"
"void main(){\n"
"    gl_Position = vec4(inPosition, 0.0, 1.0);\n"
"}\n";

static const char* FS_RED =
"#version 330 core\n"
"out vec4 outColor;\n"
"void main(){\n"
"    outColor = vec4(1.0, 0.0, 0.0, 1.0);\n"
"}\n";

static const char* FS_GREEN =
"#version 330 core\n"
"out vec4 outColor;\n"
"void main(){\n"
"    outColor = vec4(0.0, 1.0, 0.0, 1.0);\n"
"}\n";

// -------------------------------------------------
static GLuint compileShader(GLenum type, const char* src) {
    GLuint s = glCreateShader(type);
    glShaderSource(s, 1, &src, NULL);
    glCompileShader(s);
    GLint ok; glGetShaderiv(s, GL_COMPILE_STATUS, &ok);
    if (!ok) {
        char log[512]; glGetShaderInfoLog(s, 512, NULL, log);
        printf("Shader error:\n%s\n", log);
        exit(1);
    }
    return s;
}

static GLuint makeProgram(const char* vsSrc, const char* fsSrc) {
    GLuint vs = compileShader(GL_VERTEX_SHADER, vsSrc);
    GLuint fs = compileShader(GL_FRAGMENT_SHADER, fsSrc);
    GLuint p = glCreateProgram();
    glAttachShader(p, vs);
    glAttachShader(p, fs);
    glLinkProgram(p);
    GLint ok; glGetProgramiv(p, GL_LINK_STATUS, &ok);
    if (!ok) {
        char log[512]; glGetProgramInfoLog(p, 512, NULL, log);
        printf("Link error:\n%s\n", log);
        exit(1);
    }
    glDeleteShader(vs);
    glDeleteShader(fs);
    return p;
}

// -------------------------------------------------
int main(int argc, char** argv)
{
    srand((unsigned)time(NULL));

    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
    glutInitContextVersion(3, 3);
    glutInitContextProfile(GLUT_CORE_PROFILE);
    glutInitWindowSize(gWidth, gHeight);
    glutCreateWindow("Dwa potoki: czerwony i zielony");

    glutDisplayFunc(DisplayScene);
    glutReshapeFunc(Reshape);

    glewExperimental = GL_TRUE;
    if (glewInit() != GLEW_OK) { printf("GLEW Error\n"); return 1; }

    Initialize();
    glutMainLoop();

    glDeleteProgram(progRed);
    glDeleteProgram(progGreen);
    glDeleteBuffers(1, &vbo);
    glDeleteVertexArrays(1, &vao);
    return 0;
}

void Initialize()
{
    glGenVertexArrays(1, &vao);
    glBindVertexArray(vao);

    glGenBuffers(1, &vbo);
    glBindBuffer(GL_ARRAY_BUFFER, vbo);

    GLfloat triangles[6 * N]; // 3 wierzchołki × (x,y)

    for (int i = 0; i < N; ++i) {
        float dx = (rand() % 200 - 100) / 100.0f;
        float dy = (rand() % 200 - 100) / 100.0f;
        float size = 0.05f + (rand() % 50) / 500.0f;

        triangles[i*6 + 0] = dx - size;
        triangles[i*6 + 1] = dy - size;
        triangles[i*6 + 2] = dx + size;
        triangles[i*6 + 3] = dy - size;
        triangles[i*6 + 4] = dx;
        triangles[i*6 + 5] = dy + size;
    }

    glBufferData(GL_ARRAY_BUFFER, sizeof(triangles), triangles, GL_STATIC_DRAW);

    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 0, (void*)0);
    glEnableVertexAttribArray(0);

    glBindVertexArray(0);

    progRed   = makeProgram(VS_SIMPLE, FS_RED);
    progGreen = makeProgram(VS_SIMPLE, FS_GREEN);

    glClearColor(1.f, 1.f, 1.f, 1.f);
}
void DisplayScene()
{
    glClear(GL_COLOR_BUFFER_BIT);
    glBindVertexArray(vao);

    int nRed   = N/2;
    int nGreen = N - nRed;

    glUseProgram(progRed);
    glDrawArrays(GL_TRIANGLES, 0, nRed * 3);

    glUseProgram(progGreen);
    glDrawArrays(GL_TRIANGLES, nRed * 3, nGreen * 3);

    glUseProgram(0);
    glBindVertexArray(0);
    glutSwapBuffers();
}

void Reshape(int width, int height)
{
    gWidth = width; gHeight = height;
    glViewport(0, 0, width, height);
}

