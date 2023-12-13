from django.contrib import admin
from django.template.response import TemplateResponse
from django.urls import path
from .models import Account


# Register your models here.
class QuanLyAppAdminSite(admin.AdminSite):
    site_header = 'San Thuong Mai Dien Tu'

    def get_urls(self):
        return [
            path('QuanlyApp-stats/', self.stats_view)
        ] + super().get_urls()

    def stats_view(self, request):
        return TemplateResponse(request, 'admin/stats.html')


admin_site = QuanLyAppAdminSite(name='app')


admin_site.register(Account)
