from django.contrib import admin

from .models import News, CategoriesNews, Comments, Events, CategoryParticipants, Teams, Sports, Results, Roles, Users
class NewsAdmin(admin.ModelAdmin):
    """Новости"""
    list_display = ("id", "idAuthor", "body", "dateAdd", "comments", "categories")
admin.site.register(News, NewsAdmin)
admin.site.register(CategoriesNews)
admin.site.register(Comments)
admin.site.register(Events)
admin.site.register(CategoryParticipants)
admin.site.register(Teams)
admin.site.register(Sports)
admin.site.register(Results)
admin.site.register(Roles)
admin.site.register(Users)
# Register your models here.
