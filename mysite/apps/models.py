from django.db import models
from django.template import loader


class Title(models.Model):
    """Заголовок."""
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True,
                               related_name="parent_name")
    slug = models.SlugField(unique=True,
                            null=True,
                            blank=True,
                            verbose_name="URL")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Заголовок"
        verbose_name_plural = "Заголовки"


class SubTitle(models.Model):
    """Подзаголовок."""
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('Title',
                               on_delete=models.CASCADE,
                               null=False,
                               blank=False,
                               related_name="child_name")
    slug = models.SlugField(unique=True, verbose_name="URL")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Подзаголовок"
        verbose_name_plural = "Подзаголовки"
