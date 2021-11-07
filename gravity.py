import turtle
import math
import time

earth = turtle.Turtle()
earth.shape("circle")
earth.color("blue", "lightblue")
earth.shapesize(2, 2)
moon = turtle.Turtle()
moon.shape("circle")
moon.color("lightgray", "gray")
moon.penup()
turtle.tracer(0)

G = 6.674_30e-11 # m³ kg⁻¹ s⁻²
m_earth = 5.97237e24 # kg
m_moon = 7.342e22 # kg 

moon_x = 380_000_000 # m
moon_y = 0
moon_vx = 0
moon_vy = 500

scale = 1/1500000 # m to px
dt = 3600 # s

while True:
    r = math.sqrt(moon_x**2 + moon_y**2)
    F = G*m_earth*m_moon/(r**2)
    a = F/m_moon

    ax = -a*moon_x/r
    ay = -a*moon_y/r

    moon_vx += ax*dt
    moon_vy += ay*dt

    moon_x += moon_vx*dt
    moon_y += moon_vy*dt

    moon.goto(moon_x*scale, moon_y*scale)
    moon.pendown()

    #print(moon_x, moon_y)

    turtle.update()

    time.sleep(1/60)


