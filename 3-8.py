import math

def track_projectile(m, v0, theta, t):
    g = 9.8
    x = y = 0.
    x = v0*math.cos(theta)*t

    y = v0*math.sin(theta)*t - 1/2*g*t**2
    return x, y
