import urllib2, math
from json import loads

def get_ratings(query,loc):
	q = query.replace(" ","+")
	#my google api key
	key = "AIzaSyAmtzKMmQcC0mcXxvuUDcXYpocqMZiBAFg"
	# url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?key=AIzaSyAmtzKMmQcC0mcXxvuUDcXYpocqMZiBAFg&sensor=false&query=DairyQueen&location=40.736796,-73.9962539&radius=50'
	url = "https://maps.googleapis.com/maps/api/place/textsearch/json?key="+key+"&sensor=false&query="+q+"&location="+loc+"&radius=50"
	try:
		#send http request
		req = urllib2.Request(url)
		#get response
		response = urllib2.urlopen(req)
		#get json content from results
		content = loads(response.read())
		rating = content['results'][0]['rating']
		price_level = content['results'][0]['price_level']
		return (rating, price_level)
	except Exception as inst:
		print inst
		exit(1)

def get_ref(query,loc):
	q = query.replace(" ","+")
	#my google api key
	key = "AIzaSyAmtzKMmQcC0mcXxvuUDcXYpocqMZiBAFg"
	# url = 'https://maps.googleapis.com/maps/api/place/textsearch/json?key=AIzaSyAmtzKMmQcC0mcXxvuUDcXYpocqMZiBAFg&sensor=false&query=DairyQueen&location=40.736796,-73.9962539&radius=50'
	url = "https://maps.googleapis.com/maps/api/place/textsearch/json?key="+key+"&sensor=false&query="+q+"&location="+loc+"&radius=50"
	try:
		#send http request
		req = urllib2.Request(url)
		#get response
		response = urllib2.urlopen(req)
		#get json content from results
		content = loads(response.read())
		ref = content['results'][0]['reference']
		return ref
	except Exception as inst:
		print inst
		exit(1)


if __name__ == '__main__':
	csv = open('../restaurants_coord.csv')
	first_line = csv.readline()
	for line in csv:
		cols = line.split(',')
		lat,lng = cols[-2],cols[-1].strip()
		name = cols[0]
		loc = lat+','+lng
		print loc
		rating,price_level = get_ratings(name,loc)
		print rating, price_level
		break

