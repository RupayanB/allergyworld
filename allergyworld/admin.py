from django.contrib import admin
from allergyworld.models import Restaurant, User

class RestaurantAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields':['name']}),
		(None, {'fields':['address']}),
		(None, {'fields':['website']}),
		(None, {'fields':['lat']}),
		(None, {'fields':['lng']}),
	]
	list_display = ('name','address','website','lat','lng')

class UserAdmin(admin.ModelAdmin):
	fieldsets = [
		(None, {'fields':['name']}),
		(None, {'fields':['allergy']}),
		(None, {'fields':['email']}),
	]
	list_display = ('name','allergy','email')

admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(User, UserAdmin)
