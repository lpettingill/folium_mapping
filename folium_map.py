#import packages
import pandas as pd
import folium as fo
import pdb

#from csv to pandas dataframe
surg = open("/Users/lindsaypettingill/Desktop/shoulder.csv")
df = pd.read_csv(surg)
      
#define start, zoom level, basemap
mymap = fo.Map(location=[37.7833, -122.4167], tiles='Stamen Toner',
                   zoom_start=9)
mymap.create_map(path='shoulder.html')                  

#short loop that goes through each row, grabs lat and long, adds a popup, scales circles by data value
for x in range(len(df.latitude)):
	try:
		lat=(df.latitude[x])
		long=(df.longitude[x])
		name=(df.fullname[x])
		scale=(df.diff2[x])/5.0
		if np.isnan(scale):
			continue
		mymap.circle_marker(location=[lat,long], popup=(name),radius=scale, fill_color='#f00')
	except:
		continue
	mymap.create_map(path='shoulder.html')
	
	#more infos at https://github.com/wrobstory/folium
