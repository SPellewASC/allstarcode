
from Myro import *
init("sim")

sim = Simulation("Empty Room", 1000, 500, makeColor("green"))
sim.setup()
makeRobot("SimScribbler", sim)
#P by Shamrock

def P():
    
    turnBy(-270,"deg")
    backward(1,5)
    penDown()
    forward(1,3)
    turnBy(90,"deg")
    motors(-1,0,10)
    turnBy(-272,"deg")
    backward(1,3.2)

#A by FlyGuyEli

def A():
    penDown()
    turnBy(75,"deg")
    forward(1,4)
    turnBy(-140,"deg")
    forward(1,4)
    turnBy(180,"deg")
    forward(1,1.65)
    turnBy(65,"deg")
    forward(1,1.7)
# Darlyn Letter I
def I():
    penDown()
    turnBy(90, "deg")
    forward(1,3)
    penUp()
    forward(1,1)
    penDown()
    forward(1,.4)
    backward(1,.2)
    penUp()
    backward(1,4.2)
#L by Jeffron the GOAT
def L():
    penDown()
    turnBy(90, "deg")
    forward(1,3)
    turnBy(-180, "deg")
    forward(1, 3)
    turnBy(90)
    forward(1, 2)
P()
turnBy(180, "deg")
forward(1, 3)
turnBy(90, "deg")
forward(1, 2)
A()
turnBy(180, "deg")
forward(1, 1.65)
turnBy(-65, "deg")
forward(1, 1.65)
turnBy(65, "deg")
forward(1, 2)
I()
turnBy(-90, "deg")
forward(1, 2)
L()