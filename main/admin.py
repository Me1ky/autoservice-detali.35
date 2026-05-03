from django.contrib import admin
from .models import Service, Price, Contact, AboutSection

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon', 'order', 'is_active')
    list_editable = ('order', 'is_active')

@admin.register(Price)
class PriceAdmin(admin.ModelAdmin):
    list_display = ('service_name', 'category', 'price', 'order', 'is_active')
    list_editable = ('price', 'order', 'is_active')

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ('title', 'contact_type', 'value', 'order', 'is_active')
    list_editable = ('order', 'is_active')

@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ('title', 'section_type', 'order', 'is_active')
    list_editable = ('order', 'is_active')