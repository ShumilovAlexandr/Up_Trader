from django.db import models


class Title(models.Model):
    """Заголовок."""
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self',
                               on_delete=models.CASCADE,
                               null=True,
                               blank=True,
                               related_name="parent_name")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Заголовок"
        verbose_name_plural = "Заголовки"


# class SubTitle(models.Model):
#     """Подзаголовок."""
#     parent_subtitle = models.ForeignKey('self',
#                                         on_delete=models.CASCADE,
#                                         null=True,
#                                         blank=True,
#                                         related_name="name_subtitle")
#     parent_title = models.ForeignKey(Title,
#                                      on_delete=models.CASCADE,
#                                      null=True,
#                                      blank=True,
#                                      related_name="name_subtitle")
#     name = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = "Подзаголовок"
#         verbose_name_plural = "Подзаголовки"
#
