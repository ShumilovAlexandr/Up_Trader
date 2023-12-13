from django.db import models
from django.template import loader
from django.urls import reverse


class Title(models.Model):
    """Заголовок."""
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True,
                            null=True,
                            blank=True,
                            verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('page',
                       kwargs={'page_slug': self.slug})

    class Meta:
        verbose_name = "Заголовок"
        verbose_name_plural = "Заголовки"


class SubTitle(models.Model):
    """Подзаголовок."""
    name = models.CharField(max_length=50)
    menu = models.ForeignKey(Title,
                             on_delete=models.CASCADE,
                             null=True,
                             blank=True,
                             related_name="child_name")
    parent = models.ForeignKey('self',
                               blank=True,
                               null=True,
                               related_name='childrens',
                               on_delete=models.CASCADE)
    slug = models.SlugField(unique=True,
                            verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('page',
                       kwargs={'page_slug': self.slug})

    class Meta:
        verbose_name = "Подзаголовок"
        verbose_name_plural = "Подзаголовки"
