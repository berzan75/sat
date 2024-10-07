import pgzrun
from random import randint
from time import time

WIDTH=900
HEIGHT=700

satellites=[]
lines=[]
start_time=0
end_time=0
total_time=0

number_of_satellites=9

next_satellite=0

def create_satellite():
    global start_time
    for i in range(number_of_satellites):
        sa=Actor("satilite")
        sa.pos=randint(40 ,(WIDTH-40)),randint(40, (HEIGHT -40))
        satellites.append(sa)
    start_time=time()




pgzrun.go()
