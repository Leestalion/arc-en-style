from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Informations Nécessaires',        {'fields': ['titre', 'pub_date', 'image']}),
        ("Informations Complémentaires",    {'fields': ['description', "type_image"]}),
    ]
    list_filter = ['pub_date']

admin.site.register(Post, PostAdmin)
