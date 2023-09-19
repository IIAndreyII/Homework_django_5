from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(default='Тема затрагивает ...', blank=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField()
    dob = models.DateField()
    rating = models.DecimalField(default=5.0, max_digits=3, decimal_places=2)

    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Post(models.Model):
    title = models.CharField(max_length=200)
    post = models.TextField(max_length=1000)
    publish_date = models.DateField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    views = models.IntegerField(default=0)
    publish = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.title}, автор: {self.author}'


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, verbose_name='Статья')
    comment = models.TextField(verbose_name='Комментарий')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    def __str__(self):
        return f'Комментарий к статье {self.post}'
