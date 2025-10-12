#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

#include <GL/glew.h>
#include <GL/freeglut.h>

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

GLuint vao, vbo;
GLuint progGradient, progRed;
int gWidth = 500, gHeight = 500;

void DisplayScene();
void Initialize();
void Reshape(int width, int height);

static const char* VS_POS_PASS =
"#version 330 core\n"
"layout(location=0) in vec2 inPosition;\n"
"out vec2 vPos;\n"
"void main(){\n"
"  vPos = inPosition;\n"
"  gl_Position = vec4(inPosition, 0.0, 1.0);\n"
"}\n";

static const char* FS_RADIAL_RED =
"#version 330 core\n"
"in vec2 vPos;\n"
"out vec4 outColor;\n"
"uniform float uRadius;\n"
"uniform float uAspect;\n"
"void main(){\n"
"  vec2 p = vec2(vPos.x * uAspect, vPos.y);\n"
"  float d = length(p);\n"
"  float t = clamp(d / uRadius, 0.0, 1.0);\n"
"  float r = 1.0 - t;\n"
"  outColor = vec4(r, 0.0, 0.0, 1.0);\n"
"}\n";

static const char* FS_SOLID_RED =
"#version 330 core\n"
"out vec4 outColor;\n"
"void main(){ outColor = vec4(1.0, 0.0, 0.0, 1.0); }\n";

static GLuint compileShader(GLenum type, const char* src) {
    GLuint s = glCreateShader(type);
    glShaderSource(s, 1, &src, NULL);
    glCompileShader(s);
    GLint ok;
    glGetShaderiv(s, GL_COMPILE_STATUS, &ok);
    if (!ok) {
        char log[1024];
        glGetShaderInfoLog(s, 1024, NULL, log);
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
    GLint ok;
    glGetProgramiv(p, GL_LINK_STATUS, &ok);
    if (!ok) {
        char log[1024];
        glGetProgramInfoLog(p, 1024, NULL, log);
        printf("Link error:\n%s\n", log);
        exit(1);
    }
    glDeleteShader(vs);
    glDeleteShader(fs);
    return p;
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
    glutInitContextVersion(3, 3);
    glutInitContextProfile(GLUT_CORE_PROFILE);
    glutInitWindowSize(gWidth, gHeight);
    glutCreateWindow("OPENGL");

    glutDisplayFunc(DisplayScene);
    glutReshapeFunc(Reshape);

    glewExperimental = GL_TRUE;
    if (glewInit() != GLEW_OK) {
        printf("GLEW Error\n");
        return 1;
    }

    Initialize();
    glutMainLoop();

    glDeleteProgram(progGradient);
    glDeleteProgram(progRed);
    glDeleteBuffers(1, &vbo);
    glDeleteVertexArrays(1, &vao);
    return 0;
}

void Initialize() {
    const float R = 0.6f;  
    const int   K = 8;    

    float verts[(1 + K + 1) * 2];

    verts[0] = 0.0f;
    verts[1] = 0.0f;

    for (int i = 0; i < K; ++i) {
        float ang = (float)i * (2.0f * (float)M_PI / (float)K);
        float x = R * cosf(ang);
        float y = R * sinf(ang);
        verts[(1 + i) * 2 + 0] = x;
        verts[(1 + i) * 2 + 1] = y;
    }

    verts[(1 + K) * 2 + 0] = verts[2];
    verts[(1 + K) * 2 + 1] = verts[3];

    glGenVertexArrays(1, &vao);
    glBindVertexArray(vao);

    glGenBuffers(1, &vbo);
    glBindBuffer(GL_ARRAY_BUFFER, vbo);
    glBufferData(GL_ARRAY_BUFFER, sizeof(verts), verts, GL_STATIC_DRAW);

    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 0, (void*)0);
    glEnableVertexAttribArray(0);

    glBindVertexArray(0);

    progGradient = makeProgram(VS_POS_PASS, FS_RADIAL_RED);
    progRed      = makeProgram(VS_POS_PASS, FS_SOLID_RED);

    glClearColor(1.f, 1.f, 1.f, 1.f);
    glLineWidth(3.0f);

    glUseProgram(progGradient);
    GLint locRad = glGetUniformLocation(progGradient, "uRadius");
    GLint locAsp = glGetUniformLocation(progGradient, "uAspect");
    glUniform1f(locRad, R);
    glUniform1f(locAsp, (float)gWidth / (float)gHeight);
    glUseProgram(0);
}

void DisplayScene() {
    glClear(GL_COLOR_BUFFER_BIT);
    glBindVertexArray(vao);

    const int K = 8;

    glUseProgram(progGradient);
    glDrawArrays(GL_TRIANGLE_FAN, 0, 1 + K + 1);

    glUseProgram(progRed);
    glDrawArrays(GL_LINE_LOOP, 1, K);

    glUseProgram(0);
    glBindVertexArray(0);
    glutSwapBuffers();
}

void Reshape(int width, int height) {
    gWidth = width;
    gHeight = height;
    glViewport(0, 0, width, height);
    glUseProgram(progGradient);
    GLint locAsp = glGetUniformLocation(progGradient, "uAspect");
    if (locAsp >= 0) {
        float aspect = (float)width / (float)height;
        glUniform1f(locAsp, aspect);
    }
    glUseProgram(0);

    glutPostRedisplay();
}
