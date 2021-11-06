# import the module
import python_weather
import asyncio

def GetLocation():
    print("Please enter your City and State/Country")
    x=input()
    return x
async def getweather():
    
    # declare the client. format defaults to the metric system (celcius, km/h, etc.)
    client = python_weather.Client(format=python_weather.IMPERIAL)

    # fetch a weather forecast from a city
    weather = await client.find(GetLocation())

    # returns the current day's forecast temperature (int)
    print(weather.current.temperature)

    # get the weather forecast for a few days
    for forecast in weather.forecasts:
        print( forecast.sky_text)
        if(forecast.sky_text=="Clear" or forecast.sky_text=="Sunny"):
            x=1
        else:
        
            x=0
        if(x==1):
         print("Conditions are Optimal")
        else:
         print("Conditions are not optimal")
    # close the wrapper once done
    await client.close()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(getweather())

