import turtle as t
def cell(int):
	t.pendown()
	for x in range(3):
		t.forward(int)
		t.right(90)


	t.forward(int)
	t.penup()
	t.right(90)
#
#cell(100)
#t.goto(100,0)
#cell(100)
#t.goto(200,0)
#cell(100)
#t.goto(300,0)
#cell(100)
#t.goto(400,0)
#cell(100)


a=0
while a<5:
    t.goto(a*100,0)
    cell(100)
    a=a+1


a=0
while a<5:
    t.goto(a*100,100)
    cell(100)
    a=a+1


a=0
while a<5:
    t.goto(a*100,200)
    cell(100)
    a=a+1


a=0
while a<5:
    t.goto(a*100,300)
    cell(100)
    a=a+1

a=0
while a<5:
    t.goto(a*100,400)
    cell(100)
    a=a+1


a=0
