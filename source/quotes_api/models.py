from django.contrib.auth import get_user_model
from django.db import models


User = get_user_model()

CHOICES = [('new', 'Новая'), ('moderated', 'После модерации')]


class Quote(models.Model):
    text = models.CharField(max_length=1000, blank=True, null=True, verbose_name='Текст')
    name = models.CharField(max_length=100, blank=True, null=True, verbose_name='название')
    email = models.EmailField(max_length=100, blank=False, null=False, verbose_name='Email')
    ranking = models.IntegerField(default=0, verbose_name='Рейтинг')
    status = models.TextField(default=CHOICES[0][0], choices=CHOICES, null=False, blank=False, verbose_name='Статус')
    date_created = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    def __str__(self):
        return f"{self.pk}. {self.name} {self.email}  {self.status} {self.date_created}"

    class Meta:
        db_table = "цитата"
        verbose_name = "Цитата"
        verbose_name_plural = "Цитаты"
