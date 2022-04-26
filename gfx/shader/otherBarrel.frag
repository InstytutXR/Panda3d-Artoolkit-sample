#version 120
//precision mediump float;
//fragcolor

uniform vec2 LensCenter;
uniform vec2 ScreenCenter;
uniform vec2 Scale;
uniform vec2 ScaleIn;
uniform vec4 BarrelPower;
uniform sampler2D p3d_Texture0;
varying vec2 texcoord0; 

vec2 HmdWarp(vec2 p)
{
    float theta  = atan(p.y, p.x);
    float radius = length(p);
    radius = pow(radius, BarrelPower);
    p.x = radius * cos(theta);
    p.y = radius * sin(theta);
    return 0.5 * (p + 1.0);
}

void main()
{
  vec2 tc = HmdWarp(texcoord0);
  if (!all(equal(clamp(tc, ScreenCenter-vec2(0.25, 0.5), ScreenCenter+vec2(0.25, 0.5)), tc)))
    gl_FragColor = vec4(0);
  else
    gl_FragColor = texture2D(p3d_Texture0, tc);
    
}