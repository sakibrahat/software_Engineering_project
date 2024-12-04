from django.contrib import admin
from .models import PetAdd


#new code:


@admin.register(PetAdd)
class PetAddAdmin(admin.ModelAdmin):
    list_display = ('name', 'species','breed' ,'price', 'available', 'display_image')
    list_filter = ('species', 'available')
    search_fields = ('name', 'species')
    actions = ['mark_as_sold', 'mark_as_available']

    def mark_as_sold(self, request, queryset):
        queryset.update(available=False)

    def mark_as_available(self, request, queryset):
        queryset.update(available=True)

    def display_image(self, obj):
        return obj.image.url if obj.image else None
    display_image.short_description = 'Image' 

admin.site.site_header = 'El petrio Administration'
admin.site.site_title = 'El petrio Admin'
admin.site.index_title = 'Welcome El Petrio Admin Panel'
