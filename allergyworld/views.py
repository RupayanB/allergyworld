from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from allergyworld.models import Restaurant, User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import addr2coord
import re

def search_formA(request):
    return render(request, 'allergyworld/search_formA.html')

def search_formB(request):
    return render(request, 'allergyworld/search_formB.html')

def search(request):
    key = 'AIzaSyAmtzKMmQcC0mcXxvuUDcXYpocqMZiBAFg'
    if 'location' in request.GET and request.GET['location']:
        q = request.GET['location']
        q_coord = addr2coord.convert(key, q)
        qlat, qlng = [float(x) for x in q_coord.split(',')]
        rlist = list()
        max_dist = 1
        find_more = True

        while (find_more):
            for restaurant in Restaurant.objects.all():
                rlat = float(restaurant.lat)
                rlng = float(restaurant.lng)
                dist = addr2coord.distance(qlat,qlng, rlat,rlng)
                if dist <= max_dist:
                    dist = "%.2f" % dist
                    rlist.append((restaurant,dist))
                if len(rlist) != 0 or max_dist >= 5:
                    find_more = False
            max_dist += 1

        #sort
        rlist.sort(key=lambda x:x[1])  
        total_num = len(rlist)

        #for pagination
        paginator = Paginator(rlist, 7)
        page = request.GET.get('page')
        try:
            results = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page
            results = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            results = paginator.page(paginator.num_pages)
        
        # restaurants = Restaurant.objects.filter(address__icontains=q)
        return render(request, 'allergyworld/search_results.html',
        	{'results':results, 'query':q, 'request':request, 'total_num':total_num, 'usrlat':qlat, 'usrlng':qlng})

    else:
    	return render(request, 'allergyworld/search_formA.html', {})

def signup(request):
    name = request.GET['signUpName']
    email = request.GET['signUpEmail']
    allergy = request.GET['signUpAllergy']
    User.objects.create_user(name,allergy,email)
    return render(request, 'allergyworld/search_formA.html', {})

def details(request, r_id):
    r = get_object_or_404(Restaurant, pk=r_id);
    return render(request, 'allergyworld/details.html', {'restaurant':r})


