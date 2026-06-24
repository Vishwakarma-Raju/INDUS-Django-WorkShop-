from django.contrib import admin
from . models import student, Category, Product
# Register your models here.

admin.site.register(student)
admin.site.register(Category)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title','Category','price')
    list_filter = ('Category',)
    search_fields = ('tilte',)

# Customize the admin panel

admin.site.site_header = "MyProject Admin"     # Ye top-left header hai
admin.site.site_title = "MyProject Admin Portal"     # browser tab title hai
admin.site.index_title = "Welcom to MyProject Admin Dashboard"     # index page hai
