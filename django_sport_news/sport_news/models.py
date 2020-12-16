from django.db import models

# Create your models here.

class News(models.Model):
    """Новости"""
    idAuthor = models.ForeignKey(
        'Users',
        on_delete=models.CASCADE,
    )
    body = models.TextField("Новость")
    dateAdd = models.DateField(auto_now=True, auto_now_add=False)
    categories = models.ForeignKey(
        'CategoriesNews',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.body

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

class Sports(models.Model):
    """Виды спорта"""
    NameSport = models.TextField("Вид спорта")
    category_participants = models.ManyToManyField(
        'CategoryParticipants'
    )
    def __str__(self):
        return self.NameSport

    class Meta:
        verbose_name = "Вид спорта"
        verbose_name_plural = "Виды спорта"

class CategoriesNews(models.Model):
    """Категории новостей"""
    CategoryNew = models.CharField("Категория новостей",max_length=200)

    def __str__(self):
        return self.CategoryNew

    class Meta:
        verbose_name = "Категория новости"
        verbose_name_plural = "Категории новости"

class Comments(models.Model):
    """Комментарии"""
    idUser = models.ForeignKey(
        'Users',
        on_delete=models.CASCADE,
    )
    idNew = models.ForeignKey(
        'News',
        on_delete=models.CASCADE,
    )
    text = models.TextField("Текст комментария")
    dateCommentAdd = models.DateField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

class Events(models.Model):
    """Мероприятия"""
    nameEvent = models.CharField("Мероприятие", max_length=200)
    locationEvent = models.CharField("Место проведения", max_length=200)
    dateEvent = models.DateField(auto_now=True, auto_now_add=False)
    idSport = models.ManyToManyField(
        'Sports'
    )
    idNew = models.ManyToManyField(
        'News'
    )
    

    def __str__(self):
        return self.nameEvent

    class Meta:
        verbose_name = "Мероприятие"
        verbose_name_plural = "Мероприятия"

class CategoryParticipants(models.Model):
    """Категории участников"""
    NameCategory = models.CharField("Имя категории", max_length=200)
    ageParticipant = models.IntegerField()
    weightParticipant = models.IntegerField()
    def __str__(self):
        return self.NameCategory

    class Meta:
        verbose_name = "Категория участника"
        verbose_name_plural = "Категории участников"

class Teams(models.Model):
    """Команды участников"""
    NameTeam = models.TextField("Название команды")
    idUsers = models.ManyToManyField(
        'Users'
    )
    idSport = models.ForeignKey(
        'Sports',
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.NameTeam

    class Meta:
        verbose_name = "Команда"
        verbose_name_plural = "Команды"

class Results(models.Model):
    """Результаты соревнований"""
    points = models.IntegerField()
    idEvent = models.ForeignKey(
        'Events',
        on_delete=models.CASCADE,
    )
    idTeam = models.ForeignKey(
        'Teams',
        on_delete=models.CASCADE,
    )
    def __str__(self):
        return self.points

    class Meta:
        verbose_name = "Результаты соревнований"
        verbose_name_plural = "Результаты соревнования"

class Roles(models.Model):
    """Роли пользователей"""
    NameRole = models.CharField("Название роли",max_length=200)

    def __str__(self):
        return self.NameRole

    class Meta:
        verbose_name = "Роль пользователя"
        verbose_name_plural = "Роли пользователей"

class Users(models.Model):
    """Пользователи"""
    name = models.CharField("Имя", max_length=200)
    gender = models.CharField("Пол", max_length=200)
    age = models.IntegerField()
    login = models.CharField("Логин", max_length=200)
    password = models.SlugField(max_length=50, unique=True)
    idSport = models.ForeignKey(
        'Sports',
        on_delete=models.CASCADE,
    )
    idRole = models.ForeignKey(
        'Roles',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"       
