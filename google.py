import googlemaps
from datetime import datetime
import csv
import pandas as pd
gmaps = googlemaps.Client(key='AIzaSyBUSrDQ58L1BJa7kt3o1YU-hBwkxubmHhI')
lat = []
lng = []
def read_file():
	
	with open('Desktop/data/data1.csv', 'r') as f:
		data = csv.reader(f)
		yourList = list(data)
		
		for ls in yourList:
			print(ls)
			
			location = gmaps.geocode(ls)	
			print(location);
			exit();	
			#print(str(location[0]['geometry']['location']['lat'])+', '+str(location[0]['geometry']['location']['lng'])) 	
			lat.append(location[0]['geometry']['location']['lat'])
			lng.append(location[0]['geometry']['location']['lng'])			
			write_csv(lat, lng)
			 


def write_csv(lat, lng):	
	#print(lat)
	#print(lng)	
	df = pd.DataFrame(data={"lat": lat, "lng":lng})	
	df.to_csv("Desktop/data/data_new_append.csv", sep=',',index=False)
	 	
	
 
read_file()

 
