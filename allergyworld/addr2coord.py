"""
Script to convert restaurant addresses into coordinates.
Reads csv file with entries in 'name, website, address' format.
Writes new csv file with extra coords column added to the end.
"""
import urllib2, math
from json import loads

#convert street address to coords using Google Geocode api
def convert(addr):
	address = addr.replace(" ","+")
	#my google api key
	key = "AIzaSyAmtzKMmQcC0mcXxvuUDcXYpocqMZiBAFg"
	url = "https://maps.googleapis.com/maps/api/geocode/json?key="+key+"&sensor=false&address="+address+"&components=country:US|locality:NY"
	try:
		#send http request
		req = urllib2.Request(url)
		#get response
		response = urllib2.urlopen(req)
		#get json content from results
		content = loads(response.read())
		#print str(content)
		result = content['results'][0]['geometry']['location']
		lat = result["lat"]
		lng = result["lng"]
	except Exception as inst:
		print inst
		print "address: " + addr
		print "json: " + str(content)
		exit(1)
	return str(lat)+","+str(lng)

#helper method to get distance between two coords
#source from: http://www.johndcook.com/python_longitude_latitude.html  
def distance(lat1, long1, lat2, long2):

    # Convert latitude and longitude to 
    # spherical coordinates in radians.
    degrees_to_radians = math.pi/180.0
        
    # phi = 90 - latitude
    phi1 = (90.0 - lat1)*degrees_to_radians
    phi2 = (90.0 - lat2)*degrees_to_radians
        
    # theta = longitude
    theta1 = long1*degrees_to_radians
    theta2 = long2*degrees_to_radians
        
    # Compute spherical distance from spherical coordinates.
        
    # For two locations in spherical coordinates 
    # (1, theta, phi) and (1, theta, phi)
    # cosine( arc length ) = 
    #    sin phi sin phi' cos(theta-theta') + cos phi cos phi'
    # distance = rho * arc length
    
    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + 
           math.cos(phi1)*math.cos(phi2))
    arc = math.acos( cos )

    # Remember to multiply arc by the radius of the earth 
    # in your favorite set of units to get length.
    return arc * 3960

if __name__ == "__main__":
	# fin = open('../restaurants.csv','r')
	# fout = open('../restaurants_coord.csv','w')
	# for line in fin:
	# 	line = line.strip()
	# 	if line.find('name,website,address') != -1:
	# 		continue
	# 	address = line.split(',\"')[1].strip("\"")
	# 	coords = convert(address)
	# 	line = line + "," + coords + "\n"
	# 	fout.write(line)
	# fin.close()
	# fout.close()
	test1 = convert("morningside heights")
	lat1, lng1 = [float(x) for x in test1.split(",")]
	test2 = convert ("broadway")
	lat2, lng2 = [float(x) for x in test2.split(",")]
	print str(distance(lat1, lng1, lat2, lng2))

