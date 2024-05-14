from django.contrib import admin
from .models import LostItem

@admin.register(LostItem)
class LostItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'color', 'lost_date', 'location', 'image')
    list_filter = ('category', 'color', 'lost_date')
    search_fields = ('name', 'category', 'location')
