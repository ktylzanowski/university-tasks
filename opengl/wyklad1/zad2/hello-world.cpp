// -------------------------------------------------
// Programowanie grafiki 3D w OpenGL / UG
// -------------------------------------------------
// N trójkątów z kolorem zależnym od gl_PrimitiveID
// oraz gradientem zależnym od gl_FragCoord
// -------------------------------------------------
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#include <GL/glew.h>
#include <GL/freeglut.h>

#define N 100   // liczba trójkątów

GLuint idProgram;   // program (shadery)
GLuint idVBO;       // bufor wierzchołków
GLuint idVAO;       // VAO

GLint uResLoc = -1;
int gWidth = 500, gHeight = 500;

void DisplayScene();
void Initialize();
void CreateVertexShader(void);
void CreateFragmentShader(void);
void Reshape(int width, int height);

int main(int argc, char *argv[])
{
    srand((unsigned)time(NULL));

    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
    glutInitContextVersion(3, 3);
    glutInitContextProfile(GLUT_CORE_PROFILE);
    glutInitWindowSize(gWidth, gHeight);
    glutCreateWindow("N trojkatow: gl_PrimitiveID + gl_FragCoord");

    glutDisplayFunc(DisplayScene);
    glutReshapeFunc(Reshape);

    glewExperimental = GL_TRUE;
    if (glewInit() != GLEW_OK) { printf("GLEW Error\n"); return 1; }

    if (!GLEW_VERSION_3_3) { printf("Brak OpenGL 3.3!\n"); return 1; }

    Initialize();
    glutMainLoop();

    glDeleteProgram(idProgram);
    glDeleteBuffers(1, &idVBO);
    glDeleteVertexArrays(1, &idVAO);
    return 0;
}

void DisplayScene()
{
    glClear(GL_COLOR_BUFFER_BIT);

    glUseProgram(idProgram);
    glUniform2f(uResLoc, (float)gWidth, (float)gHeight);

    glBindVertexArray(idVAO);
    glDrawArrays(GL_TRIANGLES, 0, N * 3);
    glBindVertexArray(0);

    glUseProgram(0);
    glutSwapBuffers();
}

void Initialize()
{
    glGenVertexArrays(1, &idVAO);
    glBindVertexArray(idVAO);

    glGenBuffers(1, &idVBO);
    glBindBuffer(GL_ARRAY_BUFFER, idVBO);

    GLfloat triangles[6 * N];

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

    idProgram = glCreateProgram();
    CreateVertexShader();
    CreateFragmentShader();

    glLinkProgram(idProgram);
    glValidateProgram(idProgram);

    uResLoc = glGetUniformLocation(idProgram, "uResolution");

    glClearColor(1.f, 1.f, 1.f, 1.f);
}

// ---------------------------------------
void CreateVertexShader(void)
{
    GLuint shader = glCreateShader(GL_VERTEX_SHADER);
    const GLchar *code =
        "#version 330 core\n"
        "layout(location=0) in vec2 inPosition;\n"
        "void main(){\n"
        "    gl_Position = vec4(inPosition, 0.0, 1.0);\n"
        "}\n";

    glShaderSource(shader, 1, &code, NULL);
    glCompileShader(shader);

    GLint status;
    glGetShaderiv(shader, GL_COMPILE_STATUS, &status);
    if (status != GL_TRUE) { printf("Blad kompilacji vertex shadera!\n"); exit(1); }

    glAttachShader(idProgram, shader);
}

void CreateFragmentShader(void)
{
    GLuint shader = glCreateShader(GL_FRAGMENT_SHADER);
    const GLchar *code =
        "#version 330 core\n"
        "out vec4 outColor;\n"
        "uniform vec2 uResolution; // (width, height) okna w px\n"
        "\n"
        "vec3 colorFromID(int id){\n"
        "    vec3 k = vec3(0.1031, 0.11369, 0.13787);\n"
        "    return fract(k * float(id));\n"
        "}\n"
        "\n"
        "void main(){\n"
        "    vec3 base = colorFromID(gl_PrimitiveID);\n"
        "\n"
        "    vec2 uv = gl_FragCoord.xy / uResolution;       // 0..1\n"
        "    vec3 posTint = vec3(uv, 0.5*(uv.x + uv.y));\n"
        "\n"
        "    vec3 col = mix(base, posTint, 0.5);\n"
        "    outColor = vec4(col, 1.0);\n"
        "}\n";

    glShaderSource(shader, 1, &code, NULL);
    glCompileShader(shader);

    GLint status;
    glGetShaderiv(shader, GL_COMPILE_STATUS, &status);
    if (status != GL_TRUE) { printf("Blad kompilacji fragment shadera!\n"); exit(1); }

    glAttachShader(idProgram, shader);
}

void Reshape(int width, int height)
{
    gWidth = width; gHeight = height;
    glViewport(0, 0, width, height);
}
