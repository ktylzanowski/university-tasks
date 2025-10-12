#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#include <GL/glew.h>
#include <GL/freeglut.h>

#ifndef M_PI
#define M_PI 3.14159265358979323846
#endif

#define NUMBER_OF_TRIANGLES 9
#define NUMBER_OF_VERTICES (9*3)

float Mesh_Vertices[] = {
    -0.290909f,  0.540000f,
    -0.650909f,  0.000000f,
    -0.290909f, -0.540000f,

     0.249091f, -0.540000f,
     0.309091f, -0.600000f,
     0.309091f,  0.600000f,

     0.249091f, -0.540000f,
     0.309091f,  0.600000f,
     0.249091f,  0.540000f,

    -0.350909f, -0.600000f,
    -0.290909f, -0.600000f,
    -0.290909f, -0.540000f,

    -0.290909f, -0.540000f,
     0.249091f, -0.540000f,
     0.249091f,  0.540000f,

    -0.290909f,  0.540000f,
    -0.290909f,  0.600000f,
    -0.350909f,  0.600000f,

    -0.290909f, -0.540000f,
     0.249091f,  0.540000f,
    -0.290909f,  0.540000f,

    -0.650909f,  0.000000f,
    -0.350909f, -0.600000f,
    -0.290909f, -0.540000f,

    -0.290909f,  0.540000f,
    -0.350909f,  0.600000f,
    -0.650909f,  0.000000f,
};

static GLuint vao = 0, vbo = 0;
static GLuint prog = 0;
static int gWidth = 800, gHeight = 600;

static float gFlipY = 1.0f;                    
static float gAngle = -(float)M_PI * 0.5f;    

static const char* VS_SRC =
"#version 330 core\n"
"layout(location=0) in vec2 inPos;\n"
"flat out int vPrimID;\n"
"out vec2 vPos;\n"
"uniform float uFlipY;\n"
"uniform float uAngle;\n"
"void main(){\n"
"  vPrimID = gl_VertexID / 3;              \n"
"  vec2 p = vec2(inPos.x, inPos.y * uFlipY);\n"
"  float c = cos(uAngle);\n"
"  float s = sin(uAngle);\n"
"  vec2 r = vec2(c*p.x - s*p.y, s*p.x + c*p.y);\n"
"  vPos = r;\n"
"  gl_Position = vec4(r, 0.0, 1.0);\n"
"}\n";

static const char* FS_SRC =
"#version 330 core\n"
"flat in int vPrimID;\n"
"in vec2 vPos;\n"
"out vec4 outColor;\n"
"uniform vec2 uViewport; // (width,height)\n"
"\n"
"vec3 palette(int id){\n"
"  int k = id % 6;\n"
"  if(k==0) return vec3(0.85, 0.20, 0.20);\n"
"  if(k==1) return vec3(0.20, 0.55, 0.90);\n"
"  if(k==2) return vec3(0.20, 0.75, 0.35);\n"
"  if(k==3) return vec3(0.90, 0.75, 0.20);\n"
"  if(k==4) return vec3(0.75, 0.30, 0.85);\n"
"  return vec3(0.90, 0.45, 0.20);\n"
"}\n"
"\n"
"void main(){\n"
"  vec3 base = palette(vPrimID);\n"
"  vec2 uv = gl_FragCoord.xy / uViewport;\n"
"  float band = 0.5 + 0.5 * sin( (uv.x*8.0 + uv.y*4.0) + float(vPrimID)*0.7 );\n"
"  float vign = 1.0 - 0.35 * length(vPos);\n"
"  float light = clamp(0.6*band + 0.6*vign, 0.0, 1.3);\n"
"  vec3 color = base * light;\n"
"  outColor = vec4(color, 1.0);\n"
"}\n";

static GLuint compileShader(GLenum type, const char* src) {
    GLuint s = glCreateShader(type);
    glShaderSource(s, 1, &src, NULL);
    glCompileShader(s);
    GLint ok = GL_FALSE;
    glGetShaderiv(s, GL_COMPILE_STATUS, &ok);
    if (!ok) {
        char log[1024];
        glGetShaderInfoLog(s, 1024, NULL, log);
        fprintf(stderr, "Shader compile error:\n%s\n", log);
        exit(1);
    }
    return s;
}
static GLuint makeProgram(const char* vs, const char* fs) {
    GLuint v = compileShader(GL_VERTEX_SHADER, vs);
    GLuint f = compileShader(GL_FRAGMENT_SHADER, fs);
    GLuint p = glCreateProgram();
    glAttachShader(p, v);
    glAttachShader(p, f);
    glLinkProgram(p);
    GLint ok = GL_FALSE;
    glGetProgramiv(p, GL_LINK_STATUS, &ok);
    if (!ok) {
        char log[1024];
        glGetProgramInfoLog(p, 1024, NULL, log);
        fprintf(stderr, "Program link error:\n%s\n", log);
        exit(1);
    }
    glDeleteShader(v);
    glDeleteShader(f);
    return p;
}

static void Initialize() {
    glGenVertexArrays(1, &vao);
    glBindVertexArray(vao);

    glGenBuffers(1, &vbo);
    glBindBuffer(GL_ARRAY_BUFFER, vbo);
    glBufferData(GL_ARRAY_BUFFER, sizeof(Mesh_Vertices), Mesh_Vertices, GL_STATIC_DRAW);

    glVertexAttribPointer(0, 2, GL_FLOAT, GL_FALSE, 0, (void*)0);
    glEnableVertexAttribArray(0);

    glBindVertexArray(0);

    prog = makeProgram(VS_SRC, FS_SRC);

    glClearColor(0.95f, 0.97f, 1.0f, 1.0f);
}

static void DisplayScene() {
    glClear(GL_COLOR_BUFFER_BIT);

    glUseProgram(prog);

    GLint uFlipYLoc     = glGetUniformLocation(prog, "uFlipY");
    GLint uAngleLoc     = glGetUniformLocation(prog, "uAngle");
    GLint uViewportLoc  = glGetUniformLocation(prog, "uViewport");

    if (uFlipYLoc >= 0)    glUniform1f(uFlipYLoc, gFlipY);
    if (uAngleLoc >= 0)    glUniform1f(uAngleLoc, gAngle);
    if (uViewportLoc >= 0) glUniform2f(uViewportLoc, (float)gWidth, (float)gHeight);

    glBindVertexArray(vao);
    glDrawArrays(GL_TRIANGLES, 0, NUMBER_OF_VERTICES);
    glBindVertexArray(0);

    glUseProgram(0);
    glutSwapBuffers();
}

static void Reshape(int w, int h) {
    gWidth = (w > 0) ? w : 1;
    gHeight = (h > 0) ? h : 1;
    glViewport(0, 0, gWidth, gHeight);
    glutPostRedisplay();
}
int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB);
    glutInitContextVersion(3, 3);
    glutInitContextProfile(GLUT_CORE_PROFILE);
    glutInitWindowSize(gWidth, gHeight);
    glutCreateWindow("Domek (house.h): per-triangle color + rotation");

    glutDisplayFunc(DisplayScene);
    glutReshapeFunc(Reshape);

    glewExperimental = GL_TRUE;
    if (glewInit() != GLEW_OK) {
        fprintf(stderr, "GLEW init failed\n");
        return 1;
    }

    Initialize();
    glutMainLoop();

    glDeleteProgram(prog);
    glDeleteBuffers(1, &vbo);
    glDeleteVertexArrays(1, &vao);
    return 0;
}
