from django.db import models


class Title(models.Model):
    """Header model."""
    name = models.CharField(max_length=50)
    # parent = models.ForeignKey('self',
    #                            on_delete=models.CASCADE,
    #                            null=True,
    #                            blank=True,
    #                            related_name="parent_name")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Header"
        verbose_name_plural = "Headers"


# class SubTitle(models.Model):
#     """Subheader model."""
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
#         verbose_name = "Subheader"
#         verbose_name_plural = "Subheaders"
#
