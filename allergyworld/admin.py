from django.contrib import admin
from allergyworld.models import Restaurant

class RestaurantAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields':['name']}),
		(None, {'fields':['address']}),
	]
	list_display = ('name','address')


admin.site.register(Restaurant, RestaurantAdmin)
