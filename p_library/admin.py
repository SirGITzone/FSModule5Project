from django.contrib import admin

# Register your models here.

from p_library.models import PublishingHouse, Book, Author, Inspiration


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title',)
    # fields = ('ISBN', 'title', 'description', 'year_release', 'authors', 'price', 'publishing_house') #Перечислили все поля, которые разрешено редактировать (не указали copy_count)
    exclude = ('ISBN',)  #Так можно исключать конкретное поле из отображения в панели администратора
# @admin.register(Book)                        #Такой вариант позволяет не переопределять метод str в models.py
# class BookAdmin(admin.ModelAdmin):
    
#     @staticmethod
#     def author_full_name(obj):
#         return obj.author.full_name

#     list_display = ('title', 'author_full_name',)
#     fields = ('ISBN', 'title', 'description', 'year_release', 'author', 'price')




@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass

@admin.register(PublishingHouse)
class PublishingHouseAdmin(admin.ModelAdmin):
    pass


@admin.register(Inspiration)
class InspirationAdmin(admin.ModelAdmin):
    pass


    