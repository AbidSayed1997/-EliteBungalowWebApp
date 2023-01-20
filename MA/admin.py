from django.contrib import admin
from . models import ContactModel,BunglowModel,DisplayLocation,Resort

# Register your models here.


# @admin.register(Location)

# class LocationAdmin(admin.ModelAdmin):

#     list_display = ['loc_name']


@admin.register(ContactModel)

class BunglowAdmin(admin.ModelAdmin):

    list_display = ['fname','lname','contact','email','requirement']
    

# @admin.register(BunglowModel)

# class MatheranAdmin(admin.ModelAdmin):
    
#     list_display = ['bunglow_name','room_size','amenites','images','location']

# admin.site.register(Location)
# admin.site.register(ContactModel)
admin.site.register(BunglowModel)
admin.site.register(DisplayLocation)



# @admin.register(DisplayLocation)

# class DisplayAdmin(admin.ModelAdmin):

#     list_display = ['location_name','text_desc','image_display']


@admin.register(Resort)

class ResortAdmin(admin.ModelAdmin):

    list_display = ['resort_name','r_image']