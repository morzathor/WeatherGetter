import requests as rq
from datetime import datetime

###### Constants ######
BASE_URL = f'https://api.open-meteo.com/v1/forecast'
DEFAULT_PARAMETERS = {
          'latitude':'37.566',
          'longitude':'126.9784',
          'daily':'temperature_2m_max,temperature_2m_min',
          'hourly':'temperature_2m,showers,rain',
          'current':'temperature_2m',
          'timezone':'Asia/Seoul',
          'forecast_days':1}

###### Main function ######
def main():
    while True:
        print("\nWelcome to weather forecasting app!!")
        choice = int(input("""
                        1.Show current forecast
                        2.Show daily forecast
                        3.Show hourly forecast
                        4.Set location (Given location will be valid until next start)
                        5.Exit
                        Choose what to do: """))

        if choice == 1:
            current_forecast()
            input("\nPress enter to continue...\n")
            continue
        elif choice == 2:
            user_input = int(input("Enter forecast days: "))
            if user_input <=16:
                DEFAULT_PARAMETERS['forecast_days'] =  user_input
            else:
                print("\n ***** Limit is 16! *****")
                input("\nPress enter to continue...\n")
                continue
            daily_forecast()
            input("\nPress enter to continue...\n")
            continue
        elif choice == 3:
            user_input = int(input("Enter forecast days: "))
            if user_input <=16:
                DEFAULT_PARAMETERS['forecast_days'] =  user_input
            else:
                print("\n ***** Limit is 16! *****")
                input("\nPress enter to continue...\n")
                continue
            hourly_forecast()
            input("\nPress enter to continue...\n")
            continue
        
        elif choice == 4:
            ###### Change parameters based on user's location ######
            DEFAULT_PARAMETERS['latitude'] = input("Enter latitude: ")
            DEFAULT_PARAMETERS['longitude'] = input("Enter longitude: ")
            continue
        elif choice == 5:
            break
###### Retrieve and show hourly forecast ######
def hourly_forecast():
    the_req = rq.get(BASE_URL,params=DEFAULT_PARAMETERS)
    the_response = the_req.json()

    timestamps = the_response['hourly']['time']

    fix_date = [datetime.fromisoformat(ts).strftime("%Y-%m-%d %H:%M") for ts in timestamps]
    count_one = 0
    for i in fix_date:
        print(f"{i}: {the_response['hourly']['temperature_2m'][count_one]}")
        count_one += 1

###### Retrieve and show daily forecast ######
def daily_forecast():
    the_req = rq.get(BASE_URL,params=DEFAULT_PARAMETERS)
    the_response = the_req.json()

    timestamps = the_response['daily']['time']
    fix_date = [datetime.fromisoformat(ts).strftime("%Y-%m-%d") for ts in timestamps]
    e = 0
    for i in fix_date:
        print(f"{i}: maximum: {the_response['daily']['temperature_2m_max'][e]} -- minimum: {the_response['daily']['temperature_2m_min'][e]}")
        e += 1

###### Retrieve and show current forecast ######
def current_forecast():
    the_req = rq.get(BASE_URL,params=DEFAULT_PARAMETERS)
    the_response = the_req.json()

    timestamps = the_response['current']['time']
    fix_date = datetime.fromisoformat(timestamps).strftime("%Y-%m-%d %H:%M")
    
    print(f"{fix_date}: current temp: {the_response['current']['temperature_2m']}")

main()