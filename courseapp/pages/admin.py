from django.contrib import admin
from .models import Slider

class SliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_at')
    list_filter = ('is_active',)

admin.site.register(Slider, SliderAdmin)