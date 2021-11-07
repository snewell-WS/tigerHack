from skyfield.api import load
from skyfield.framelib import ecliptic_frame
#For use in Determining MoonPhase
def MoonPhase():
    #using skyfield
    ts = load.timescale()
    t = ts.now()
    eph = load('de421.bsp')
    sun, moon, earth = eph['sun'], eph['moon'], eph['earth']

    e = earth.at(t)
    _, slon, _ = e.observe(sun).apparent().frame_latlon(ecliptic_frame)
    _, mlon, _ = e.observe(moon).apparent().frame_latlon(ecliptic_frame)
    phase = (mlon.degrees - slon.degrees) % 360.0
    return phase


def determinePhase(phase):
    phaseOfMoon = "none"
    if(phase==0):
        #phaseOfMoon = "NewMoon"
        x = 1
        return  x
    if(phase>0 and phase<90):                 
        #phaseOfMoon = "WaxingCrescent"
        x = 2
        return  x
    if(phase==90):        
        x = 3
        #phaseOfMoon = "FirstQuarter", x
        return x
    if(phase>90 and phase<180): 
        x = 4      
        #phaseOfMoon = "WaxingGibbus"
        return  x
    if(phase==180):  
        x = 5      
        #phaseOfMoon = "FullMoon" 
        return  x
    if(phase>180 and phase<270):   
        x = 6     
        #phaseOfMoon = "WaningGibbus"
        return  x
    if(phase==270):      
        x = 7
        #phaseOfMoon = "ThirdQuarter"
        return  x
    if(phase>270):        
        x = 8
        #phaseOfMoon = "WaningCrescent"
        return  x
