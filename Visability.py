from bs4 import BeautifulSoup
import requests
from requests.models import LocationParseError
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
 
class Weather:
    location = "" #location name
    time = 0 #time accessed
    info = "" #how cloudy it will be
    weather = "" #temperature
 
def weather(city):
    city = city.replace(" ", "+")
    res = requests.get(
        f'https://www.google.com/search?q={city}&oq={city}&aqs=chrome.0.35i39l2j0l4j46j69i60.6128j1j7&sourceid=chrome&ie=UTF-8', headers=headers)
    soup = BeautifulSoup(res.text, 'html.parser')
    location = soup.select('#wob_loc')[0].getText().strip()
    time = soup.select('#wob_dts')[0].getText().strip()
    info = soup.select('#wob_dc')[0].getText().strip()
    weather = soup.select('#wob_tm')[0].getText().strip()


    #in order
    #Location
    #time accessed
    #how cloudy is it
    weatherInfo = Weather()
    weatherInfo.location = location
    weatherInfo.time = time
    weatherInfo.info = info 
    weatherInfo.weather = weather+"°F"
    
    
    return weatherInfo



