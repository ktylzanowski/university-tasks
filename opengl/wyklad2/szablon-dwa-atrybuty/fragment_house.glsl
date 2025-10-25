#version 330 core
uniform vec2 uResolution;

flat in int vPrimID;
out vec4 fragColor;

vec3 colorFromPrimID(int id)
{
    float h = fract(float(id) * 0.137);
    float s = 0.75;
    float v = 0.95;

    float c = v * s;
    float hp = h * 6.0;
    float x = c * (1.0 - abs(mod(hp, 2.0) - 1.0));

    vec3 rgb;
    if      (hp < 1.0) rgb = vec3(c, x, 0.0);
    else if (hp < 2.0) rgb = vec3(x, c, 0.0);
    else if (hp < 3.0) rgb = vec3(0.0, c, x);
    else if (hp < 4.0) rgb = vec3(0.0, x, c);
    else if (hp < 5.0) rgb = vec3(x, 0.0, c);
    else               rgb = vec3(c, 0.0, x);

    float m = v - c;
    return rgb + vec3(m);
}

void main()
{
    vec3 base = colorFromPrimID(vPrimID);
    vec2 uv = gl_FragCoord.xy / uResolution;   // 0..1
    float g = smoothstep(0.0, 1.0, uv.y);

    vec3 tint = mix(vec3(0.95, 0.96, 1.00), vec3(1.00, 0.96, 0.95), g);
    float rim = pow(1.0 - abs(uv.x - 0.5) * 2.0, 2.0) * 0.12;

    vec3 color = mix(base, base * tint, 0.35) + rim;
    fragColor = vec4(color, 1.0);
}
