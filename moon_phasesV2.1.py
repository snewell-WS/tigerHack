from skyfield.api import load
from skyfield.framelib import ecliptic_frame

ts = load.timescale()
t = ts.now()
eph = load('de421.bsp')
sun, moon, earth = eph['sun'], eph['moon'], eph['earth']

e = earth.at(t)
_, slon, _ = e.observe(sun).apparent().frame_latlon(ecliptic_frame)
_, mlon, _ = e.observe(moon).apparent().frame_latlon(ecliptic_frame)
phase = (mlon.degrees - slon.degrees) % 360.0
y=0

print('{0:.1f}'.format(phase))
if(phase==0):
    print("Its a new moon")
    y=1
if(phase>0 and phase<90):
    print("The moon is a waxing cresent")
    y=2
if(phase==90):
    print("its a first quarter moon")
    y=3
if(phase>90 and phase<180):
    print("the moon is a waxing gibbus")
    y=4
if(phase==180):
    print("the moon is full")
    y=5
if(phase>180 and phase<270):
    print("the moon is a waning gibbus")
    y=6
if(phase==270):
    print("its a third quarter moon")
    y=7
if(phase>270):
    print("the moon is a waning cressent")
    y=8

 
for x in range(8):
    if(y>8):                
        y=1
    print(y)
    y=y+1