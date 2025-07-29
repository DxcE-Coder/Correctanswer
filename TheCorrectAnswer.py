import turtle as t
import random
f =t.Turtle()
p =t.Turtle()
w =t.Turtle()
s =t.Screen()
#window
s.setup(600,600)
s.title("the correct answer")
s.cv._rootwindow.resizable(False, False)
#player
t.speed(0)
t.up()
t.bk(200)
t.speed(1)
#walls
w.speed(0)
w.up()
w.bk(250)
w.down()
w.lt(90)
w.pensize(3)
w.fd(250)
w.rt(90)
w.fd(500)
w.rt(90)
w.fd(500)
w.rt(90)
w.fd(500)
w.rt(90)
w.fd(250)
w.hideturtle()

#pen
p.up()
p.speed(0)
p.lt(90)
p.fd(150)
p.hideturtle()
#finish
f.up()
f.speed(0)
f.fd(200)
f.shape("circle")
f.fillcolor("white")
f.pencolor("black")
#others

for i in range(10):
    op =random.choice(["*","+","-"])
    ab =random.randint(1,10)
    ad =random.randint(1,10)
    p.clear()
    p.write(f"{ab} {op} {ad}", align="center", font=("arial", 26, "bold"))
    cc = float(s.textinput("Question", "write the answer:"))



    if op =="+":
        an = ab+ad
    elif op =="-":
        an = ab-ad
    elif op =="*":
        an = ab*ad
    if an == cc:
        t.fd(40)
    if an != cc:
        p.clear()
        p.write("Loser!",align="center",font=("arial",26,"bold"))
        break
    if t.xcor() >= f.xcor():
        p.clear()
        p.write("winner!", align="center", font=("arial", 26, "bold"))
    



    
    

