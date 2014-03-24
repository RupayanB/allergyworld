"""
Script to convert restaurant addresses into coordinates.
Reads csv file with entries in 'name, website, address' format.
Writes new csv file with extra coords column added to the end.
"""
import urllib2
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


if __name__ == "__main__":
	fin = open('./restaurants.csv','r')
	fout = open('./restaurants_coord.csv','w')
	for line in fin:
		line = line.strip()
		if line.find('name,website,address') != -1:
			continue
		address = line.split(',\"')[1].strip("\"")
		coords = convert(address)
		line = line + "," + coords + "\n"
		fout.write(line)
	fin.close()
	fout.close()
	# test = convert("234 W. 42nd St., New York, NY 10036")
	# print test

