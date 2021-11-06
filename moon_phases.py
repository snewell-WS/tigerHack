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

print('{0:.1f}'.format(phase))
if(phase==0):
    print("Its a new moon")
if(phase>0 and phase<90):
    print("The moon is a waxing cresent")
if(phase==90):
    print("its a first quarter moon")
if(phase>90 and phase<180):
    print("the moon is a waxing gibbus")
if(phase==180):
    print("the moon is full")
if(phase>180 and phase<270):
    print("the moon is a waning gibbus")
if(phase==270):
    print("its a third quarter moon")
if(phase>270):
    print("the moon is a waning cressent")
