from django.contrib import admin
from .models import Release, Artist, Genre


class ReleaseAdmin(admin.ModelAdmin):
    list_display = ("name", "year",)


class ArtistAdmin(admin.ModelAdmin):
    list_display = ("name",)


class GenreAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(Release, ReleaseAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Genre, GenreAdmin)
