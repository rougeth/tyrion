from django.contrib import admin
from .models import URL, Click


@admin.register(URL)
class URLAdmin(admin.ModelAdmin):
    list_display = ['short', 'url', 'created', 'updated', 'clicks']

    # Maybe there's a better way to get an annotate field
    def clicks(self, obj):
        return obj.clicks
    clicks.admin_order_field = 'clicks'


@admin.register(Click)
class ClickAdmin(admin.ModelAdmin):
    list_display = ['url', 'ip', 'date']
