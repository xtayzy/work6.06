from django.contrib import admin

# Register your models here.

from post.models import Category, Product, Store


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


class StoreAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Store, StoreAdmin)
