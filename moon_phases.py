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
        phaseOfMoon = "NewMoon"
        return phaseOfMoon
    if(phase>0 and phase<90):                 
        phaseOfMoon = "WaxingCrescent"
        return phaseOfMoon
    if(phase==90):        
        phaseOfMoon = "FirstQuarter"
        return phaseOfMoon
    if(phase>90 and phase<180):       
        phaseOfMoon = "WaxingGibbus"
        return phaseOfMoon
    if(phase==180):        
        phaseOfMoon = "FullMoon"
        return phaseOfMoon
    if(phase>180 and phase<270):        
        phaseOfMoon = "WaningGibbus"
        return phaseOfMoon
    if(phase==270):      
        phaseOfMoon = "ThirdQuarter"
        return phaseOfMoon
    if(phase>270):        
        phaseOfMoon = "WaningCrescent"
        return phaseOfMoon
