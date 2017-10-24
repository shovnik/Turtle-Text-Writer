import turtle
wn = turtle.Screen()
x = turtle.Turtle()


def setup():
    x.penup()
    x.backward(900)
    x.left(90)
    x.forward(125)
    x.right(90)


def loop():
    while 1 > 0:
        x.left(90)


def a1(k=0.5):
    x.forward(k*25)
    x.left(75.9637565)
    x.backward(k*103.07764064)
    x.pendown()
    x.forward(k*103.07764064/2)
    x.right(75.9637565)
    x.forward(k*25)
    x.left(104.0362435)
    x.forward(k*103.07764064/2)
    x.left(151.927513)
    x.forward(k*103.07764064/2)
    x.penup()
    x.left(104.0362435)
    x.forward(k*25)
    x.right(75.9637565)
    x.pendown()
    x.forward(k*103.07764064/2)
    x.penup()
    x.left(165.9637565)
    x.forward(k*100)
    x.right(90)
    x.forward(k*25)


def a2(k=0.5):
    x.forward(k*25)
    x.left(104.0362435)
    x.backward(k*103.07764064)
    x.pendown()
    x.forward(k*103.07764064)
    x.left(151.927513)
    x.forward(k*103.07764064)
    x.penup()
    x.right(165.9637565)
    x.forward(k*50)
    x.right(90)
    x.forward(k*12.5)
    x.pendown()
    x.forward(k*25)
    x.penup()
    x.forward(k*37.5)
    x.left(90)
    x.forward(k*50)
    x.right(90)


def b1(k=0.5):
    x.right(90)
    x.pendown()
    x.forward(k*100)
    x.left(90)
    x.forward(k*25)
    x.circle(k*25, 180)
    x.forward(k*25)
    x.penup()
    x.right(180)
    x.forward(k*20)
    x.pendown()
    x.circle(k*25, 180)
    x.forward(k*20)
    x.penup()
    x.right(180)
    x.forward(k*80)


def b2(k=0.5):
    x.right(90)
    x.pendown()
    x.forward(k*100)
    x.left(90)
    x.forward(k*20)
    x.circle(k*30, 180)
    x.forward(k*20)
    x.penup()
    x.right(180)
    x.forward(k*15)
    x.pendown()
    x.circle(k*20, 180)
    x.forward(k*15)
    x.penup()
    x.right(180)
    x.forward(k*75)


def c1(k=0.5):
    x.forward(k*50)
    x.left(90)
    x.backward(k*25)
    x.pendown()
    x.circle(k*25, 180)
    x.forward(k*50)
    x.circle(k*25, 180)
    x.penup()
    x.forward(k*75)
    x.right(90)
    x.forward(k*25)


def d1(k=0.5):
    x.right(90)
    x.pendown()
    x.forward(k*100)
    x.left(90)
    x.forward(k*25)
    x.circle(k*25, 90)
    x.forward(k*50)
    x.circle(k*25, 90)
    x.forward(k*25)
    x.penup()
    x.right(180)
    x.forward(k*75)


def e1(k=0.5):
    x.forward(k*50)
    x.pendown()
    x.backward(k*50)
    x.right(90)
    x.forward(k*50)
    x.left(90)
    x.forward(k*50)
    x.penup()
    x.backward(k*50)
    x.right(90)
    x.pendown()
    x.forward(k*50)
    x.left(90)
    x.forward(k*50)
    x.penup()
    x.left(90)
    x.forward(k*100)
    x.right(90)
    x.forward(k*25)


def e2(k=0.5):
    x.forward(k*50)
    x.pendown()
    x.backward(k*50)
    x.right(90)
    x.forward(k*50)
    x.left(90)
    x.forward(k*25)
    x.penup()
    x.backward(k*25)
    x.right(90)
    x.pendown()
    x.forward(k*50)
    x.left(90)
    x.forward(k*50)
    x.penup()
    x.left(90)
    x.forward(k*100)
    x.right(90)
    x.forward(k*25)


def f1(k=0.5):
    x.forward(k*50)
    x.pendown()
    x.backward(k*50)
    x.right(90)
    x.forward(k*50)
    x.left(90)
    x.forward(k*50)
    x.penup()
    x.backward(k*50)
    x.right(90)
    x.pendown()
    x.forward(k*50)
    x.penup()
    x.left(90)
    x.forward(k*50)
    x.left(90)
    x.forward(k*100)
    x.right(90)
    x.forward(k*25)


def f2(k=0.5):
    x.forward(k*50)
    x.pendown()
    x.backward(k*50)
    x.right(90)
    x.forward(k*50)
    x.left(90)
    x.forward(k*25)
    x.penup()
    x.backward(k*25)
    x.right(90)
    x.pendown()
    x.forward(k*50)
    x.penup()
    x.left(90)
    x.forward(k*50)
    x.left(90)
    x.forward(k*100)
    x.right(90)
    x.forward(k*25)


def g1(k=0.5):
    x.forward(k*50)
    x.left(90)
    x.backward(k*25)
    x.pendown()
    x.circle(k*25, 180)
    x.forward(k*50)
    x.circle(k*25, 180)
    x.forward(k*25)
    x.left(90)
    x.forward(k*25)
    x.penup()
    x.right(90)
    x.forward(k*50)
    x.right(90)
    x.forward(k*50)


def h1(k=0.5):
    x.right(90)
    x.pendown()
    x.forward(k*100)
    x.penup()
    x.backward(k*50)
    x.left(90)
    x.pendown()
    x.forward(k*50)
    x.left(90)
    x.forward(k*50)
    x.backward(k*100)
    x.right(90)
    x.penup()
    x.forward(k*25)
    x.left(90)
    x.forward(k*100)
    x.right(90)


def i1(k=0.5):
    x.pendown()
    x.forward(k*50)
    x.penup()
    x.backward(k*25)
    x.right(90)
    x.pendown()
    x.forward(k*100)
    x.left(90)
    x.backward(k*25)
    x.penup()
    x.forward(k*25)
    x.pendown()
    x.forward(k*25)
    x.penup()
    x.forward(k*25)
    x.left(90)
    x.forward(k*100)
    x.right(90)


def j1(k=0.5):
    x.right(90)
    x.forward(k*87.5)
    x.pendown()
    x.circle(k*12.5, 180)
    x.forward(k*87.5)
    x.penup()
    x.right(90)
    x.backward(k*25)
    x.pendown()
    x.forward(k*50)
    x.penup()
    x.forward(k*25)


def k1(k=0.5):
    x.right(90)
    x.pendown()
    x.forward(k*100)
    x.penup()
    x.backward(k*50)
    x.left(135)
    x.pendown()
    x.forward(k*70.7106781187)
    x.penup()
    x.backward(k*70.7106781187)
    x.right(90)
    x.pendown()
    x.forward(k*70.7106781187)
    x.penup()
    x.left(45)
    x.forward(k*25)
    x.left(90)
    x.forward(k*100)
    x.right(90)


def l1(k=0.5):
    x.right(90)
    x.pendown()
    x.forward(k*100)
    x.left(90)
    x.forward(k*50)
    x.penup()
    x.left(90)
    x.forward(k*100)
    x.right(90)
    x.forward(k*25)


def m1(k=0.5):
    x.left(90)
    x.backward(k*100)
    x.pendown()
    x.forward(k*100)
    x.right(165.9637565)
    x.forward(k*103.07764064)
    x.left(151.927513)
    x.forward(k*103.07764064)
    x.right(165.9637565)
    x.forward(k*100)
    x.penup()
    x.backward(k*100)
    x.left(90)
    x.forward(k*25)


def m2(k=0.5):
    x.left(90)
    x.backward(k*100)
    x.pendown()
    x.forward(k*100)
    x.right(153.4349488)
    x.forward(k*55.9016994375)
    x.left(126.8698976)
    x.forward(k*55.9016994375)
    x.right(153.4349488)
    x.forward(k*100)
    x.penup()
    x.backward(k*100)
    x.left(90)
    x.forward(k*25)


def n1(k=0.5):
    x.left(90)
    x.backward(k*100)
    x.pendown()
    x.forward(k*100)
    x.right(153.4349488)
    x.forward(k*111.803398875)
    x.left(153.4349488)
    x.forward(k*100)
    x.right(90)
    x.penup()
    x.forward(k*25)


def o1(k=0.5):
    x.forward(k*50)
    x.left(90)
    x.backward(k*25)
    x.pendown()
    x.circle(k*25, 180)
    x.forward(k*50)
    x.circle(k*25, 180)
    x.forward(k*50)
    x.penup()
    x.forward(k*25)
    x.right(90)
    x.forward(k*25)


def p1(k=0.5):
    x.right(90)
    x.pendown()
    x.forward(k*100)
    x.penup()
    x.backward(k*50)
    x.left(90)
    x.pendown()
    x.forward(k*25)
    x.circle(k*25, 180)
    x.forward(k*25)
    x.penup()
    x.right(180)
    x.forward(k*75)


def q1(k=0.5):
    x.right(90)
    x.forward(k*50)
    x.pendown()
    x.forward(k*25)
    x.circle(k*25, 180)
    x.forward(k*50)
    x.circle(k*25, 180)
    x.forward(k*25)
    x.penup()
    x.left(45)
    x.forward(k*70.7106781187/2)
    x.pendown()
    x.forward(k*70.7106781187/2)
    x.penup()
    x.left(135)
    x.forward(k*100)
    x.right(90)
    x.forward(k*25)


def r1(k=0.5):
    x.right(90)
    x.pendown()
    x.forward(k*100)
    x.penup()
    x.left(90)
    x.forward(k*50)
    x.left(135)
    x.pendown()
    x.forward(k*70.7106781187)
    x.right(135)
    x.forward(k*25)
    x.circle(k*25, 180)
    x.forward(k*25)
    x.penup()
    x.right(180)
    x.forward(k*75)


def s1(k=0.5):
    x.forward(k*50)
    x.left(90)
    x.backward(k*25)
    x.pendown()
    x.circle(k*25, 270)
    x.penup()
    x.backward(k*25)
    x.right(90)
    x.forward(k*25)
    x.pendown()
    x.circle(k*25, 270)
    x.penup()
    x.backward(k*25)
    x.right(90)
    x.forward(k*50)
    x.right(90)
    x.forward(k*25)


def t1(k=0.5):
    x.pendown()
    x.forward(k*25)
    x.penup()
    x.left(90)
    x.backward(k*100)
    x.pendown()
    x.forward(k*100)
    x.right(90)
    x.forward(k*25)
    x.penup()
    x.forward(k*25)


def u1(k=0.5):
    x.right(90)
    x.pendown()
    x.forward(k*75)
    x.circle(k*25, 180)
    x.forward(k*75)
    x.penup()
    x.right(90)
    x.forward(k*25)


def v1(k=0.5):
    x.right(75.9637565)
    x.pendown()
    x.forward(k*103.07764064)
    x.left(151.927513)
    x.forward(k*103.07764064)
    x.penup()
    x.right(75.9637565)
    x.forward(k*25)


def w1(k=0.5):
    x.right(90)
    x.pendown()
    x.forward(k*100)
    x.left(165.9637565)
    x.forward(k*103.07764064)
    x.right(151.927513)
    x.forward(k*103.07764064)
    x.left(165.9637565)
    x.forward(k*100)
    x.penup()
    x.right(90)
    x.forward(k*25)


def w2(k=0.5):
    x.right(90)
    x.pendown()
    x.forward(k*100)
    x.left(153.4349488)
    x.forward(k*55.9016994375)
    x.right(126.8698976)
    x.forward(k*55.9016994375)
    x.left(153.4349488)
    x.forward(k*100)
    x.penup()
    x.right(90)
    x.forward(k*25)


def x1(k=0.5):
    x.right(63.4349488)
    x.pendown()
    x.forward(k*111.803398875)
    x.penup()
    x.left(63.4349488)
    x.backward(k*50)
    x.left(63.4349488)
    x.pendown()
    x.forward(k*111.803398875)
    x.penup()
    x.right(63.4349488)
    x.forward(k*25)


def y1(k=0.5):
    x.right(63.4349488)
    x.pendown()
    x.forward(k*111.803398875/2)
    x.penup()
    x.left(153.4349488)
    x.backward(k*50)
    x.pendown()
    x.forward(k*50)
    x.right(26.5650512)
    x.forward(k*111.803398875/2)
    x.penup()
    x.right(63.4349488)
    x.forward(k*25)


def y2(k=0.5):
    x.right(63.4349488)
    x.pendown()
    x.forward(k*111.803398875/2)
    x.penup()
    x.left(126.8698976)
    x.backward(k*111.803398875/2)
    x.pendown()
    x.forward(k*111.803398875)
    x.penup()
    x.right(63.4349488)
    x.forward(k*25)


def z1(k=0.5):
    x.pendown()
    x.forward(k*50)
    x.right(116.5650512)
    x.forward(k*111.803398875)
    x.left(116.5650512)
    x.forward(k*50)
    x.penup()
    x.left(90)
    x.forward(k*100)
    x.right(90)
    x.forward(k*25)


def space(k=0.5):
    x.forward(k*75)


def period(k=0.5):
    x.left(90)
    x.backward(k*100)
    x.right(90)
    x.pendown()
    x.circle(k*5, 360)
    x.penup()
    x.left(90)
    x.forward(k*100)
    x.right(90)
    x.forward(k*25)


def comma(k=0.5):
    x.right(90)
    x.forward(k*110)
    x.left(90)
    x.pendown()
    x.circle(k*10, 180)
    x.circle(k*5, 360)
    x.penup()
    x.right(90)
    x.forward(k*90)
    x.right(90)
    x.forward(k*25)


def exclamation(k=0.5):
    x.left(90)
    x.backward(k*100)
    x.right(90)
    x.pendown()
    x.circle(k*5, 360)
    x.penup()
    x.left(90)
    x.forward(k*20)
    x.pendown()
    x.forward(k*80)
    x.penup()
    x.right(90)
    x.forward(k*25)


def interrogation(k=0.5):
    x.forward(k*25)
    x.left(90)
    x.backward(k*100)
    x.right(90)
    x.pendown()
    x.circle(k*5, 360)
    x.penup()
    x.left(90)
    x.forward(k*20)
    x.pendown()
    x.forward(k*30)
    x.right(90)
    x.circle(k*25, 270)
    x.penup()
    x.backward(k*25)
    x.left(90)
    x.forward(k*75)


def less(k=0.5):
    x.forward(k*50)
    x.right(90)
    x.forward(k*25)
    x.right(63.4349488)
    x.pendown()
    x.forward(k*55.9016994375)
    x.left(126.8698976)
    x.forward(k*55.9016994375)
    x.penup()
    x.left(116.5650512)
    x.forward(k*75)
    x.right(90)
    x.forward(k*25)


def greater(k=0.5):
    x.right(90)
    x.forward(k*75)
    x.left(116.5650512)
    x.pendown()
    x.forward(k*55.9016994375)
    x.left(126.8698976)
    x.forward(k*55.9016994375)
    x.penup()
    x.right(63.4349488)
    x.forward(k*25)
    x.right(90)
    x.forward(k*50)


def one(k=0.5):
    x.left(90)
    x.backward(k*25)
    x.right(45)
    x.pendown()
    x.forward(k*35.3553390593)
    x.right(135)
    x.forward(k*100)
    x.penup()
    x.left(90)
    x.backward(k*25)
    x.pendown()
    x.forward(k*50)
    x.penup()
    x.left(90)
    x.forward(k*100)
    x.right(90)
    x.forward(k*25)


def two(k=0.5):
    x.right(90)
    x.forward(k*100)
    x.right(90)
    x.backward(k*50)
    x.pendown()
    x.forward(k*50)
    x.right(123.6900675)
    x.forward(k*90.1387818866)
    x.left(33.6900675)
    x.circle(k*25, 180)
    x.penup()
    x.backward(k*25)
    x.left(90)
    x.forward(k*75)


def three(k=0.5):
    x.right(90)
    x.forward(k*75)
    x.pendown()
    x.circle(k*25, 270)
    x.right(180)
    x.circle(k*25, 270)
    x.penup()
    x.backward(k*25)
    x.left(90)
    x.forward(k*75)


def four(k=0.5):
    x.right(90)
    x.forward(k*100)
    x.left(90)
    x.forward(k*40)
    x.left(90)
    x.pendown()
    x.forward(k*100)
    x.left(146.3099325)
    x.forward(k*72.1110255093)
    x.left(123.6900675)
    x.forward(k*50)
    x.penup()
    x.left(90)
    x.forward(k*60)
    x.right(90)
    x.forward(k*25)


def five(k=0.5):
    x.right(90)
    x.forward(k*75)
    x.pendown()
    x.circle(k*25, 270)
    x.forward(k*25)
    x.right(90)
    x.forward(k*50)
    x.right(90)
    x.forward(k*50)
    x.penup()
    x.forward(k*25)


def six(k=0.5):
    x.right(90)
    x.forward(k*25)
    x.pendown()
    x.forward(k*50)
    x.circle(k*25, 360)
    x.penup()
    x.left(90)
    x.forward(k*50)
    x.left(90)
    x.forward(k*50)
    x.pendown()
    x.circle(k*25, 180)
    x.penup()
    x.backward(k*25)
    x.left(90)
    x.forward(k*75)


def seven(k=0.5):
    x.pendown()
    x.forward(k*50)
    x.right(116.5650512)
    x.forward(k*111.803398875)
    x.penup()
    x.left(116.5650512)
    x.forward(k*75)
    x.left(90)
    x.forward(k*100)
    x.right(90)


def eight(k=0.5):
    x.right(90)
    x.forward(k*50)
    x.right(90)
    x.backward(k*25)
    x.pendown()
    x.circle(k*25, 360)
    x.right(180)
    x.circle(k*25, 360)
    x.penup()
    x.forward(k*50)
    x.left(90)
    x.forward(k*50)
    x.right(90)


def nine(k=0.5):
    x.forward(k*50)
    x.left(90)
    x.backward(k*100)
    x.pendown()
    x.forward(k*75)
    x.circle(k*25, 360)
    x.penup()
    x.forward(k*25)
    x.right(90)
    x.forward(k*25)


def plus(k=0.5):
    x.right(90)
    x.forward(k*50)
    x.left(90)
    x.pendown()
    x.forward(k*25)
    x.left(90)
    x.penup()
    x.backward(k*25)
    x.pendown()
    x.forward(k*25)
    x.penup()
    x.forward(k*25)
    x.pendown()
    x.backward(k*25)
    x.right(90)
    x.forward(k*25)
    x.penup()
    x.left(90)
    x.forward(k*50)
    x.right(90)
    x.forward(k*25)


def minus(k=0.5):
    x.right(90)
    x.forward(k*50)
    x.left(90)
    x.pendown()
    x.forward(k*50)
    x.penup()
    x.left(90)
    x.forward(k * 50)
    x.right(90)
    x.forward(k * 25)


def times(k=0.5):
    x.right(90)
    x.forward(k*25)
    x.left(45)
    x.pendown()
    x.forward(k*70.7106781187)
    x.penup()
    x.right(135)
    x.forward(k*50)
    x.right(135)
    x.pendown()
    x.forward(k * 70.7106781187)
    x.penup()
    x.left(45)
    x.forward(k*25)
    x.right(90)
    x.forward(k*25)


def over(k=0.5):
    x.right(90)
    x.forward(k*50)
    x.left(90)
    x.pendown()
    x.forward(k*25)
    x.left(90)
    x.penup()
    x.backward(k*25)
    x.right(90)
    x.pendown()
    x.circle(k*5, 360)
    x.penup()
    x.left(90)
    x.forward(50*k)
    x.left(90)
    x.pendown()
    x.circle(k*5, 360)
    x.penup()
    x.left(90)
    x.forward(k*25)
    x.left(90)
    x.pendown()
    x.forward(k * 25)
    x.penup()
    x.left(90)
    x.forward(k * 50)
    x.right(90)
    x.forward(k * 25)


def apostrophe(k=0.5):
    x.left(90)
    x.backward(k*10)
    x.pendown()
    x.forward(k*10)
    x.penup()
    x.right(90)
    x.forward(k*25)