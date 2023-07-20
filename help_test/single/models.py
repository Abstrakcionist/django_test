from django.db import models


class Inputs(models.Model):
    username = models.CharField('Имя', max_length=15)
    date_of_birth = models.DateField('Дата рождения')
    info = models.TextField('Описание')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username
