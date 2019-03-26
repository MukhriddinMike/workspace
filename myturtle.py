import turtle
import tkinter
turtle.shape('classic')
# turtle.forward(100)
# turtle.left(90)
# turtle.back(150)
# turtle.right(40)
# turtle.forward(100)
###### triangle
# turtle.forward(100)
# turtle.left(90)
# turtle.forward(100)
# turtle.left(135)
# turtle.forward(141)
############romb
"""
count = 0
while count < 2:
    turtle.forward(300)
    turtle.left(90)
    turtle.forward(150)
    turtle.left(90)
    count += 1

turtle.done()
#tkinter.mainloop()
"""
"""
ctr = 0
while ctr < 360:
    turtle.forward(2)
    turtle.left(1)
    ctr += 1
turtle.done()
print("finished")
"""

# ctr,length, ctr2 = 0,100,0
# turtle.color('red', 'yellow')
# turtle.begin_fill()
# while True:
#     turtle.forward(200)
#     turtle.left(160)
#
#
# turtle.done()
snq = 0
# while snq < 5:
"""
turtle.forward(400)
turtle.left(140)
turtle.forward(400)
turtle.left(140)
turtle.forward(400)
turtle.left(140)
turtle.forward(400)
turtle.left(150)
turtle.forward(400)
"""
""""""
# while snq < 5:
#     turtle.forward(400)
#     turtle.left(144)
#     snq += 1
#### drawing star
# turtle.done()
"""
while snq < 360:
    turtle.forward(2)
    turtle.left(1)
    snq += 1

# drawing circle
turtle.done()

"""
"""
# just fucked shape

import turtle
big_line = 100
little_line = 50
angle = 90
turtle.left(angle)
turtle.forward(big_line)
count = 0
while count < 4:
    turtle.right(angle//2)
    if count != 3:
        turtle.forward(little_line)
    else:
        turtle.forward(big_line)
    count = count + 1
turtle.right(90)
turtle.forward(130)

turtle.done()
"""
import math

trtl = turtle.Turtle()
trtl.speed(500)

window = turtle.Screen()
window.bgcolor("#000000")
trtl.color("yellow")

zoom = 20

trtl.left(90)
trtl.penup()
trtl.goto(-7 * zoom, 0)
trtl.pendown()

for xz in range(-7 * zoom, -3 * zoom, 1):
    x = xz / zoom
    absx = math.fabs(x)
    y = 1.5 * math.sqrt((-math.fabs(absx - 1)) * math.fabs(3 - absx) / ((absx - 1) * (3 - absx))) * (
                1 + math.fabs(absx - 3) / (absx - 3)) * math.sqrt(1 - (x / 7) ** 2) + (
                    4.5 + 0.75 * (math.fabs(x - 0.5) + math.fabs(x + 0.5)) - 2.75 * (
                        math.fabs(x - 0.75) + math.fabs(x + 0.75))) * (1 + math.fabs(1 - absx) / (1 - absx))
    trtl.goto(xz, y * zoom)

for xz in range(-3 * zoom, -1 * zoom - 1, 1):
    x = xz / zoom
    absx = math.fabs(x)
    y = (2.71052 + 1.5 - 0.5 * absx - 1.35526 * math.sqrt(4 - (absx - 1) ** 2)) * math.sqrt(
        math.fabs(absx - 1) / (absx - 1))
    trtl.goto(xz, y * zoom)

trtl.goto(-1 * zoom, 3 * zoom)
trtl.goto(int(-0.5 * zoom), int(2.2 * zoom))
trtl.goto(int(0.5 * zoom), int(2.2 * zoom))
trtl.goto(1 * zoom, 3 * zoom)

for xz in range(1 * zoom + 1, 3 * zoom + 1, 1):
    x = xz / zoom
    absx = math.fabs(x)
    y = (2.71052 + 1.5 - 0.5 * absx - 1.35526 * math.sqrt(4 - (absx - 1) ** 2)) * math.sqrt(
        math.fabs(absx - 1) / (absx - 1))
    trtl.goto(xz, y * zoom)

for xz in range(3 * zoom + 1, 7 * zoom + 1, 1):
    x = xz / zoom
    absx = math.fabs(x)
    y = 1.5 * math.sqrt((-math.fabs(absx - 1)) * math.fabs(3 - absx) / ((absx - 1) * (3 - absx))) * (
                1 + math.fabs(absx - 3) / (absx - 3)) * math.sqrt(1 - (x / 7) ** 2) + (
                    4.5 + 0.75 * (math.fabs(x - 0.5) + math.fabs(x + 0.5)) - 2.75 * (
                        math.fabs(x - 0.75) + math.fabs(x + 0.75))) * (1 + math.fabs(1 - absx) / (1 - absx))
    trtl.goto(xz, y * zoom)

for xz in range(7 * zoom, 4 * zoom, -1):
    x = xz / zoom
    absx = math.fabs(x)
    y = (-3) * math.sqrt(1 - (x / 7) ** 2) * math.sqrt(math.fabs(absx - 4) / (absx - 4))
    trtl.goto(xz, y * zoom)

for xz in range(4 * zoom, -4 * zoom, -1):
    x = xz / zoom
    absx = math.fabs(x)
    y = math.fabs(x / 2) - 0.0913722 * x ** 2 - 3 + math.sqrt(1 - (math.fabs(absx - 2) - 1) ** 2)
    trtl.goto(xz, y * zoom)

for xz in range(-4 * zoom - 1, -7 * zoom - 1, -1):
    x = xz / zoom
    absx = math.fabs(x)
    y = (-3) * math.sqrt(1 - (x / 7) ** 2) * math.sqrt(math.fabs(absx - 4) / (absx - 4))
    trtl.goto(xz, y * zoom)

trtl.penup()
trtl.goto(300, 300)
turtle.done()