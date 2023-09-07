from django.contrib import admin
from .models import ServiceType, Service, Order, Person


# Register your models here.
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price')
    list_display_links = ('id', 'title')
    search_fields = ('id', 'title')
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(ServiceType, ServiceTypeAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(Person)
admin.site.register(Order)
