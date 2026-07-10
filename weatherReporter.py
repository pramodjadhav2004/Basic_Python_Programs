#to check and return the weather report using function
def get_weather_report(temperature):
    if temperature < 22:
        print("Cold")
    elif temperature >= 22 and temperature < 35 :
        print("Warm")
    elif temperature >= 35:
        print("Hot")

temperature = int(input("Enter the temperature: "))
get_weather_report(temperature)