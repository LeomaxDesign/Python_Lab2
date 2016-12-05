import pyowm
owm = pyowm.OWM('fff85453964a1692a3628cdef0492d7c')
observation = owm.weather_at_place('Rostov-on-Don,ru')
weather = observation.get_weather()
location = observation.get_location()
translate = {'Rostov-na-Donu': 'Ростов-на-Дону','RU': 'Россия'}
from datetime import datetime

def cloudiness():
    if 0 <= weather.get_clouds() <= 10:
        return 'ясная'
    if 10 < weather.get_clouds() <=30:
        return 'немного облачная'
    if 30 < weather.get_clouds() <= 70:
        return 'пасмурная'
    if 70 < weather.get_clouds() <= 100:
        return 'темная'

def temperature(string):
    f_observation = owm.daily_forecast('Rostov-on-Don, RU')
    f_weather = f_observation.get_weather_at(datetime.now())
    return str(round(f_weather.get_temperature('celsius')[string]))

def direction_wind():
    if 337.5 < weather.get_wind()['deg'] <= 22.5:
        return 'северный'
    if 157.5 < weather.get_wind()['deg'] <= 202.5:
        return 'южный'
    if 67.5 < weather.get_wind()['deg'] <= 112.5:
        return 'восточный'
    if 247.5 < weather.get_wind()['deg'] <= 292.5:
        return 'западный'
    if 22.5 < weather.get_wind()['deg'] <= 67.5:
        return 'северо-восточный'
    if 112.5 < weather.get_wind()['deg'] <= 157.5:
        return 'юго-восточный'
    if 202.5 < weather.get_wind()['deg'] <= 247.5:
        return 'юго-западный'
    if 292.5 < weather.get_wind()['deg'] <= 337.5:
        return 'северо-западный'

def status(x):
    return {
        '10d' or '10n': ', дождь',
        '09d' or '09n': ', ливень',
        '11d' or '11n': ', гроза',
        '13d' or '13n': ', снег',
        '50d' or '50n': ', туман'
    }.get(x, '')


print('Погода в городе ' + translate[location.get_name()] + '('
      +translate[location.get_country()] + ')' +'на сегодня '
      + str(datetime.now().strftime("%H:%M")) +' ' + cloudiness()
      + ', \nоблачность составляет ' + str(weather.get_clouds()) + '%, давление '
      + str(round(weather.get_pressure()['press']*0.750062)) + ' мм рт. ст.,\nтемпература '
      + str(round(weather.get_temperature('celsius')['temp'])) + ' градусов Цельция' + ', днём '
      + temperature('day') + ', ночью ' + temperature('night') + ' ветер ' + direction_wind() +  ', '
      + str(round(weather.get_wind()['speed'])) + ' м/c ' + status(weather.get_status()) + '.')
