from django.contrib import admin
from .models import Post, Neighborhood, Occupant, Business, Tag

admin.site.register(Post)
admin.site.register(Neighborhood)
admin.site.register(Occupant)
admin.site.register(Business)
admin.site.register(Tag)
