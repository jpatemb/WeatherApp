from datetime import datetime
import os
import requests


weather = input(str("Would you like to know the weather? (y for yes, n for no):"))
while weather!= ('y', 'n'):
    if weather in ('y'):
        user_api = os.environ['current_weather_data']
        location = input(str("Enter a City name: "))
        complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+user_api
        api_link = requests.get(complete_api_link)
        api_data = api_link.json()
        if api_data['cod'] == '404':
            print("Hmm, never heard of that City, and believe me, I've been around. Maybe another City? (Invalid City: '{}'. Please check your City name):".format(location))
            continue
        else:
            temp_city = ((api_data['main']['temp']) - 273.15)
            weather_desc = api_data['weather'][0]['description']
            hmdt = api_data['main']['humidity']
            wind_spd = api_data['wind']['speed']
            w_date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

        #print(api_data)
        print("----------------------------------------------------------------------")
        print("Ok then! Here is the current weather for {} || {}:".format(location.upper(), w_date_time))
        print("----------------------------------------------------------------------")

        print("Temperature: {:.2f} deg C".format(temp_city))
        print("Description: ", weather_desc)
        print("Humidity: ", hmdt, '%')
        print("Wind Speed: ", wind_spd, 'kmph')
        break
    elif weather in ('n'):
        print("Alright then, nevermind.\n")
        break
    else:
        print("Come again?")
        weather = input(str("(y for yes, n for no):"))
        continue
