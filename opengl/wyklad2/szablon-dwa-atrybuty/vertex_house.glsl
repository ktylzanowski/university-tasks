#version 330 core
layout(location=0) in vec2 inPos;

uniform vec2  uOffset;
uniform float uFlipY;
uniform float uScale;

flat out int vPrimID;

void main()
{
    vec2 p = inPos;

    float x = p.x;
    p.x = -p.y;  // -Y -> X
    p.y =  x;    // X -> Y
    p.y *= uFlipY;
    p *= uScale;
    p += uOffset;

    gl_Position = vec4(p, 0.0, 1.0);
    vPrimID = gl_VertexID / 3;
}
