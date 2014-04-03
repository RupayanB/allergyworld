from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from allergyworld.models import Restaurant
import addr2coord
import re

def search_formA(request):
    return render(request, 'allergyworld/search_formA.html')

def search_formB(request):
    return render(request, 'allergyworld/search_formB.html')

def search(request):
    # if 'location' in request.GET:
    #     message = 'You searched for: %r' % request.GET['location']
    # else:
    #     message = 'You submitted an empty form.'
    # return HttpResponse(message)
    
    if 'location' in request.GET and request.GET['location']:
        q = request.GET['location']
        q_coord = addr2coord.convert(q)
        qlat, qlng = [float(x) for x in q_coord.split(',')]
        rlist = list()
        max_dist = 1
        find_more = True

        # while (find_more):
        for restaurant in Restaurant.objects.all():
            rlat = float(restaurant.lat)
            rlng = float(restaurant.lng)
            dist = addr2coord.distance(qlat,qlng, rlat,rlng)
            if dist <= max_dist:
                dist = "%.2f" % dist
                rlist.append((restaurant,dist))
                print restaurant.name, str(dist)
            # if len(rlist) != 0 and max_dist >= 2:
            #     find_more = False
            # max_dist += 1

        #sort
        rlist.sort(key=lambda x:x[1])    

        # restaurants = Restaurant.objects.filter(address__icontains=q)
        return render(request, 'allergyworld/search_results.html',
        	{'results':rlist, 'query':q})

    else:
    	return render(request, 'allergyworld/search_form.html', {})

def details(request, r_id):
    r = get_object_or_404(Restaurant, pk=r_id);
    addr = re.sub(r',',' ',r.address)
    addr = re.sub(r'  ',' ',addr)
    addr = re.sub(r'\s','+',addr)
    mapsrc = "http://maps.googleapis.com/maps/api/staticmap?center="+addr+"&zoom=15&size=600x300&maptype=roadmap&markers=color:blue%7Clabel:S%7C40.702147,-74.015794&markers=color:green%7Clabel:G%7C40.711614,-74.012318&markers=color:red%7Clabel:C%7C40.718217,-73.998284&sensor=false&key=AIzaSyCexiGJQdCfhi2gQHD5GCYozlbAXji9TlM"
    return render(request, 'allergyworld/details.html', {'restaurant':r,'map_src':mapsrc})