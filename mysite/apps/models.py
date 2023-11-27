from django.db import models


class Title(models.Model):
    """Header model."""
    name = models.CharField('Name', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Header"
        verbose_name_plural = "Headers"


class SubTitle(models.Model):
    """Subheader model."""
    parent_subtitle = models.ForeignKey('self',
                                        on_delete=models.CASCADE,
                                        null=True,
                                        blank=False,
                                        related_name="name_subtitle")
    parent_title = models.ForeignKey(Title,
                                     on_delete=models.CASCADE,
                                     null=True,
                                     blank=True,
                                     related_name="name_subtitle")
    name = models.CharField('Name', max_length=50)
    url = models.CharField('Link', max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Subheader"
        verbose_name_plural = "Subheaders"

