from django.contrib import admin
from .models import (
    Question,
    ServiceType,
    Service,
    NewsPost,
    Order,
    Person,
    Banner,
    BannerRotationInterval,
    Voucher,
)


# Register your models here.
class ServiceTypeAdmin(admin.ModelAdmin):
    list_display = ("id", "title")
    list_display_links = ("id", "title")
    search_fields = ("id", "title")


class ServiceAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "price")
    list_display_links = ("id", "title")
    search_fields = ("id", "title")
    prepopulated_fields = {"slug": ("title",)}


class BannerAdmin(admin.ModelAdmin):
    list_display = ("title", "link", "image")
    prepopulated_fields = {"link": ("title",)}


class BannerRotationIntervalAdmin(admin.ModelAdmin):
    list_display = ("interval_seconds",)


class VoucherAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "code",
        "discount",
        "start_date",
        "end_date",
        "max_usages",
        "usage_count",
    )


admin.site.register(Question)
admin.site.register(ServiceType, ServiceTypeAdmin)
admin.site.register(Service, ServiceAdmin)
admin.site.register(NewsPost)
admin.site.register(Person)
admin.site.register(Order)
admin.site.register(Banner, BannerAdmin)
admin.site.register(BannerRotationInterval, BannerRotationIntervalAdmin)
admin.site.register(Voucher, VoucherAdmin)
