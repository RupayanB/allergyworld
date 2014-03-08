from django.contrib import admin
from allergyworld.models import Restaurant

class RestaurantAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields':['name']}),
		(None, {'fields':['address']}),
		(None, {'fields':['website']}),
	]
	list_display = ('name','address','website')


admin.site.register(Restaurant, RestaurantAdmin)
