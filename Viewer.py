import turtle

lines = []
colors = []
pixels = []

screen = turtle.Screen()
tur = turtle.Turtle()

pixelSize = 10
lineIndex = 0

tur.penup()
tur.goto(
    -300, 300
)
tur.pendown()

tur.hideturtle()

def DrawPixel(t, size, color, newline, lineIndex = 0):
    tur.speed(0)
    tur.pensize(3)
    tur.penup()
    if not newline:
        if color == "black":
            tur.end_fill()
            t.forward(size)
            print("A background pixel has been drawn")
        else:

            tur.begin_fill()

            for index in range(4):
                tur.pendown()
                t.forward(size)
                t.left(90)
            t.forward(size)

            tur.end_fill()

            print("a pixel has been drawn")
    else:
        tur.goto(
        -300, 300 - lineIndex * 0.65
    )


with open ("Smiley.simpix", "r") as file:
    height = int(file.readline().strip())
    width = int(file.readline().strip())
    fillcolor = file.readline().strip()
    manual_spacing = bool(file.readline().strip())
    print(f"{height},{width},{fillcolor},{manual_spacing}")

    tur.fillcolor(fillcolor)


    for y in range(height):
        row = file.readline().strip()


        for x in range(width):
            print(row[x])
            pixels.append(row[x])

        if not manual_spacing:
            pixels.append('9')

    for character in pixels:
        if character == '0':
            colors.append('black')
        elif character == '1':
            colors.append('blue')
        elif character == '9':
            colors.append('newline')

    print(pixels)
    print(colors) # Now we know what colored pixels we need to draw
    for color in colors:
        lineIndex+=1

        if not color == 'newline':
            DrawPixel(tur, pixelSize, color, False)
        else:
            DrawPixel(tur, pixelSize, color, True, lineIndex)
    turtle.done()