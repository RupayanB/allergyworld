from django.contrib import admin
from allergyworld.models import Restaurant

class RestaurantAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields':['name']}),
		(None, {'fields':['address']}),
		(None, {'fields':['website']}),
		(None, {'fields':['lat']}),
		(None, {'fields':['lng']}),
	]
	list_display = ('name','address','website','lat','lng')


admin.site.register(Restaurant, RestaurantAdmin)
