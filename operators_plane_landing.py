#1/usr/bin/env python3

#data

	#current parameters of plane

plane_altitude = 1000 #meters
plane_speed = 300 #km/hours
fuel_volume = 10 #perсent
technical_difficulites = False


	#weather

wind_speed = 60  #km/hours
fair_wind = False

	#other conditions

runway_clear = True


#logic

optimal_altitude = 700  > plane_altitude >= 100
optimal_speed    = 500 >   plane_speed   >= 200 

emergency_landing = technical_difficulites\
                    or\
                    fuel_volume < 1


can_land = emergency_landing\
           or\
           (optimal_speed\
           and\
           optimal_altitude\
           and\
           wind_speed < 100\
           and\
           runway_clear)
#view

print("Aircraft flight parameters:")
print('-'* 27)
print("Plane altitude = ", plane_altitude, "km")
print("Plane speed    = ", plane_speed, "km/hours")
print("Fuel level     = ", fuel_volume, ' %')
print("Wind speed     = ", wind_speed, "km/hours")
#print("Wind direction = ", fair_wind)
print("."*27)
print("Technical difficulites: ", technical_difficulites)
print()
print("Can plane land?", can_land)
