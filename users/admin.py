from django.contrib import admin

from users.models import Practicing


@admin.register(Practicing)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'phone_number')

# Register your models here.
