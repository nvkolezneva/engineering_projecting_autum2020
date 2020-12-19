from django.contrib import admin

from .models import News, CategoriesNews, Comments, Events, CategoryParticipants, Teams, Sports, Results, Roles, Users

class CommentsInline(admin.TabularInline):
    """Отзывы на странице новости"""
    model = Comments
    extra = 1

class NewsAdmin(admin.ModelAdmin):
    """Новости"""
    list_display = ("id", "Author", "body", "dateAdd", "categories", "PublishedOrNot")
    list_display_links = ("body",)
    list_filter = ("Author",)
    search_fields = ("Author__name",)
    inlines=[CommentsInline]
    save_on_top = True
    save_as = True
    list_editable= ("categories","PublishedOrNot")
    actions = ["published", "unpublished"]

    def unpublished(self, request,queryset):
        """Снять с публикации"""
        row_update = queryset.update(PublishedOrNot=False)
        if row_update =='1':
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request,f"{row_update}")

    def published(self, request,queryset):
        """Опубликовать"""
        row_update = queryset.update(PublishedOrNot=True)
        if row_update =='1':
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request,f"{row_update}")

    published.short_description = "Опубликовать"
    published.allowed_permissions = ('change',)

    unpublished.short_description = "Снять с публикации"
    unpublished.allowed_permissions = ('change',)

class CategoriesNewsAdmin(admin.ModelAdmin):
    """Категории новостей"""
    list_display = ("id", "CategoryNew")
    list_display_links = ("CategoryNew",)
    search_fields = ("CategoryNew",)


class CommentsAdmin(admin.ModelAdmin):
    """Комментарии"""
    list_display = ("id", "User","New","text","dateCommentAdd")
    list_display_links = ("text",)
    list_filter = ("User",)
    search_fields = ("User__name",)

class EventsAdmin(admin.ModelAdmin):
    """Мероприятия"""
    list_display = ("id", "nameEvent","locationEvent","dateEvent", "DoneOrNot")
    list_display_links = ("nameEvent",)
    list_filter = ("nameEvent",)
    search_fields = ("nameEvent",)
    actions = ["notdone", "done"]

    def notdone(self, request,queryset):
        """Отметка о непроведении мероприятия"""
        row_update = queryset.update(DoneOrNot=False)
        if row_update =='1':
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request,f"{row_update}")

    def done(self, request,queryset):
        """Отметка о проведении мероприятия"""
        row_update = queryset.update(DoneOrNot=True)
        if row_update =='1':
            message_bit = "1 запись была обновлена"
        else:
            message_bit = f"{row_update} записей были обновлены"
        self.message_user(request,f"{row_update}")

    done.short_description = "Провести мероприятие"
    done.allowed_permissions = ('change',)

    notdone.short_description = "Не проводить мероприятие"
    notdone.allowed_permissions = ('change',)
    

class CategoryParticipantsAdmin(admin.ModelAdmin):
    """Категории участников"""
    list_display = ("id", "NameCategory","ageParticipant","weightParticipant")
    list_display_links = ("NameCategory",)
    list_filter = ("NameCategory",)
    search_fields = ("NameCategory",)

class TeamsAdmin(admin.ModelAdmin):
    """Команды"""
    list_display = ("id", "NameTeam","Sport")
    list_display_links = ("NameTeam",)
    list_filter = ("NameTeam",)
    search_fields = ("NameTeam",)

class SportsAdmin(admin.ModelAdmin):
    """Виды спорта"""
    list_display = ("id", "NameSport")
    list_display_links = ("NameSport",)
    search_fields = ("NameSport",)

class ResultsAdmin(admin.ModelAdmin):
    """Результаты"""
    list_display = ("id", "nameResult","points","Event", "Team")
    list_display_links = ("nameResult",)
    list_filter = ("nameResult",)
    search_fields = ("points",)

class RolesAdmin(admin.ModelAdmin):
    """Роли пользователей"""
    list_display = ("id", "NameRole")
    list_display_links = ("NameRole",)
    search_fields = ("NameRole",)


class UsersAdmin(admin.ModelAdmin):
    """Пользователи"""
    list_display = ("id", "name", "gender", "age", "login", "Sport", "Role" )
    list_display_links = ("name",)
    list_filter = ("age",)
    search_fields = ("name",)
    readonly_fields = ("login","password")
admin.site.register(News, NewsAdmin)
admin.site.register(CategoriesNews, CategoriesNewsAdmin)
admin.site.register(Comments,CommentsAdmin)
admin.site.register(Events, EventsAdmin)
admin.site.register(CategoryParticipants, CategoryParticipantsAdmin)
admin.site.register(Teams, TeamsAdmin)
admin.site.register(Sports, SportsAdmin)
admin.site.register(Results, ResultsAdmin)
admin.site.register(Roles, RolesAdmin)
admin.site.register(Users, UsersAdmin)
# Register your models here.
