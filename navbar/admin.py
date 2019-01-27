from django.contrib import admin

from.models import NavTitle, Anime, Announcments, Genre

# class NavTitleAdmin(admin.ModelAdmin):
#     fieldsets = [
#         (None, {'fields': ['question_text']}),
#         ('Date information', {'fields': ['pub_date']}),
#     ]

admin.site.register(NavTitle)#, NavTitleAdmin)
admin.site.register(Announcments)
admin.site.register(Anime)
admin.site.register(Genre)
