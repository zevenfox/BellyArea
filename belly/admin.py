from django.contrib import admin
from .models import Menu, TopPick
# Register your models here.
admin.site.site_header = "BellyArea Admin"
admin.site.site_title = "Admin Area"
admin.site.index_title = "Welcome to the BellyArea Admin Area"

admin.site.register(Menu)
admin.site.register(TopPick)
