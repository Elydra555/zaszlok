import turtle as t

t.colormode(255)

#gambia
#zöld

t.screensize(1080, 1920)

def gambia():
    t.fillcolor(58, 119, 40)
    t.begin_fill()

    for i in range(2):
        t.forward(150)
        t.right(90)
        t.forward(50)
        t.right(90)

    t.end_fill()


    #köz
    for i in range(2):
        t.forward(150)
        t.left(90)
        t.forward(5)
        t.left(90)
    t.left(90)
    t.forward(5)

    t.penup()

    # kék
    t.pendown()
    t.fillcolor(12, 28, 140)
    t.begin_fill()
    # t.left(90)
    for i in range(2):
        t.forward(40)
        t.right(90)
        t.forward(150)
        t.right(90)

    t.end_fill()


    #köz
    t.forward(40)
    for i in range(2):
        t.forward(5)
        t.right(90)
        t.forward(150)
        t.right(90)

    t.forward(5)

    #piros
    t.fillcolor(206, 17, 38)
    t.begin_fill()
    for i in range(2):
        t.forward(50)
        t.right(90)
        t.forward(150)
        t.right(90)
    t.end_fill()



#izland

def izland():
    t.fillcolor(0 ,56, 151)
    t.begin_fill()
    for i in range(2):
        t.forward(250)
        t.left(90)
        t.forward(180)
        t.left(90)
    t.end_fill()


    t.fillcolor("white")
    t.begin_fill()
    t.left(90)
    t.forward(75)
    t.right(90)
    t.color("white")
    t.forward(250)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(250)
    t.end_fill()

    t.penup()
    t.right(90)
    t.forward(75)
    t.right(90)
    t.forward(110)
    t.right(90)
    t.pendown()
    t.begin_fill()
    t.forward(180)
    t.right(90)
    t.forward(30)
    t.right(90)
    t.forward(180)
    t.end_fill()

    t.right(90)
    t.forward(10)
    t.right(90)
    t.color(215, 40, 40)
    t.fillcolor(215, 40, 40)
    t.begin_fill()
    t.forward(180)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(180)
    t.end_fill()

    t.fillcolor(215, 40, 40)
    t.begin_fill()
    t.penup()
    t.setpos(0, 85)
    t.pendown()
    t.right(90)
    t.forward(250)
    t.left(90)
    t.forward(10)
    t.left(90)
    t.forward(250)
    t.setpos(0, 85)
    t.end_fill()

    t.exitonclick()

def gorog():

    t.speed(50)

    t.fillcolor(13, 94, 175)
    t.begin_fill()
    for i in range(2):
        t.forward(270)
        t.right(90)
        t.forward(180)
        t.right(90)
    t.end_fill()

    t.forward(270)
    t.right(90)
    t.fillcolor("white")
    t.begin_fill()
    t.forward(20)
    t.right(90)
    t.forward(170)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(170)
    t.end_fill()

    t.right(90)
    t.forward(20)
    t.begin_fill()
    t.right(90)
    t.forward(170)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(170)
    t.end_fill()


    t.right(90)
    t.forward(20)
    t.begin_fill()
    t.right(90)
    t.forward(270)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(270)
    t.end_fill()


    t.right(90)
    t.forward(20)
    t.begin_fill()
    t.right(90)
    t.forward(270)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(270)
    t.end_fill()

    t.penup()

    t.setpos(0, 0)

    t.speed(2)

    t.pendown()
    t.begin_fill()
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.left(90)
    t.forward(20)
    t.left(90)
    t.forward(40)
    t.right(90)
    t.forward(40)
    t.end_fill()

    t.exitonclick()




def csillag(size, color):
    t.color(color)
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
        t.forward(size)
        t.left(72)
    t.end_fill()

def torok():
    t.penup()
    t.goto(-200, 100)
    t.pendown()
    t.color("red")
    t.begin_fill()
    for _ in range(2):
        t.forward(400)
        t.right(90)
        t.forward(200)
        t.right(90)
    t.end_fill()
    
    t.penup()
    t.goto(-90, -60)
    t.pendown()
    t.color("white")
    t.begin_fill()
    t.circle(60)
    t.end_fill()
    
    t.penup()
    t.goto(-80, -50)
    t.pendown()
    t.color("red")
    t.begin_fill()
    t.circle(50)
    t.end_fill()

    t.penup()
    t.goto(30, 0)
    t.setheading(-45)
    t.pendown()
    csillag(30, "white")


#gorog()
#gambia()
#izland()
torok()