# admin.py
from django.contrib import admin
from .models import Notification

class NotificationAdmin(admin.ModelAdmin):
    list_display = ('message', 'user', 'read', 'timestamp')
    list_filter = ('read',)
    search_fields = ('message', 'user__username')

admin.site.register(Notification, NotificationAdmin)