from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from allergyworld.models import Restaurant

def search_form(request):
    return render(request, 'allergyworld/search_form.html')

def search(request):
    # if 'location' in request.GET:
    #     message = 'You searched for: %r' % request.GET['location']
    # else:
    #     message = 'You submitted an empty form.'
    # return HttpResponse(message)
    
    if 'location' in request.GET and request.GET['location']:
        q = request.GET['location']
        restaurants = Restaurant.objects.filter(address__icontains=q)
        return render(request, 'allergyworld/search_results.html',
        	{'results':restaurants, 'query':q})

    else:
    	return render(request, 'allergyworld/search_form.html', {})

def details(request, r_id):
	r = get_object_or_404(Restaurant, pk=r_id)
	return render(request, 'allergyworld/details.html', {'restaurant':r})