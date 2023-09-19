from django.contrib import admin
from .models import Author, Post, Comment, Category


@admin.action(description='Повысить рейтинг на 1 пункт')
def increase_rating(model_admin, request, queryset):
    for obj in queryset:
        obj.rating += 1
        obj.save()


@admin.action(description='Понизить рейтинг на 1 пункт')
def decrease_rating(model_admin, request, queryset):
    for obj in queryset:
        obj.rating -= 1
        obj.save()


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'bio', 'rating']
    search_fields = ['last_name']
    search_help_text = 'Поиск по фамилии автора'
    actions = [increase_rating, decrease_rating]

    readonly_fields = ['rating']
    fieldsets = [
        (None, {
         'classes': ['wide'],
         'fields': ['first_name', 'last_name', 'bio'],
        }),
    ('Личные данные', {
        'classes': ['collapse'],
        'description': 'Личные данные автора',
        'fields': ['email', 'dob'],
        }),
    ('Рейтинг', {
        'description': 'Рейтинг сформирован автоматически на основе оценок читателей',
        'fields': ['rating'],
        })
    ]


class PostAdmin(admin.ModelAdmin):
    list_display = ['publish', 'title', 'category', 'author', 'publish_date', 'views']


class CommentAdmin(admin.ModelAdmin):

    def short_comment(self, obj):
        return obj.comment[:35] + '...'
    short_comment.short_description = 'Comment'
    list_display = ['short_comment', 'created_at']


admin.site.register(Author, AuthorAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)