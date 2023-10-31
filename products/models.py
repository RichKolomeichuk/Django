from django.db import models


class Task(models.Model):
    title = models.CharField('Именование задачи', max_length=200, )
    content = models.TextField('Информация о задаче')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Именованная задача'
        verbose_name_plural = 'Задачи'
