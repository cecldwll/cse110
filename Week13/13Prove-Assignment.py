# Wind Chill Calculations

def calculate_windchill():
    for x in range (0, 60, 5 ):
        x += 5  
        if temperature == "C":
            converted_temp = (temp * 9 / 5) + 32
            wind_chill = 35.74 + (0.6215 * converted_temp) - 35.75 * (x ** 0.16) + (0.4275 * converted_temp * (x ** 0.16))
            print (f"At temperature {converted_temp}F, and wind speed {x} mph, the windchill is: {wind_chill:.2f}F")
        elif temperature == "F":
            wind_chill = 35.74 + (0.6215 * temp) - (35.75 * (x ** 0.16)) + (0.4275 * temp * (x ** 0.16))
            print (f"At temperature {temp}F, and wind speed {x} mph, the windchill is: {wind_chill:.2f}F")
    

    
temp = float(input("\nWhat is the temperature? "))
temperature = input ("Fahrenheit or Celsius (F/C)? ").upper()
print()
calculate_windchill()