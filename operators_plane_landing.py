#1/usr/bin/env python3

#data

	#current parameters of plane

plane_altitude = 500 #meters
plane_speed = 300 #km/hours
fuel_volume = 67 #perсent
technical_difficulites = False


	#weather

wind_speed = 60  #km/hours
fair_wind = False

	#other conditions

runway_clear = True






#logic
optimal_altitude = 700  > plane_altitude >= 100
optimal_speed    = 500 >   plane_speed   >= 200 


can_land = tehnical_difficulites = True and fuel_volume < 1



#view

#print("Can the plane land?", can_land)
