from django.contrib import admin

from models import Category, Product, StaticPage

class CategoryAdmin(admin.ModelAdmin):
    date_hierarchy = 'created'
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('visible', 'title', 'amazon_node_id', 'created', 'modified')
    list_display_links = ('title',)
    list_editable = ('visible',)
    list_filter = ('title', 'created', 'modified')
    search_fields = ['title', 'description', 'amazon_node_id']

class ProductAdmin(admin.ModelAdmin):
    list_display = ('category', 'title', 'asin', 'price', 'popularity')
    list_display_links = ('title',)
    list_filter = ('category',)
    search_fields = ['title', 'description', 'asin']

class StaticAdmin(admin.ModelAdmin):
    list_display = ('visible', 'title', 'slug')
    list_display_links = ('title',)
    list_editable = ('visible',)
    prepopulated_fields = {'slug': ('title',)}
    search_fields = ['title', 'text']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(StaticPage, StaticAdmin)