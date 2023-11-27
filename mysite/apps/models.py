from django.db import models


class Title(models.Model):
    """Header model."""
    name = models.CharField('Name',
                            max_length=50)
    url = models.CharField('Link', 
                            null=True,
                            blank=True,
                            max_length=255)
    parent = models.ForeignKey('self', 
                               on_delete=models.CASCADE, 
                               null=True, 
                               blank=True, 
                               related_name='children')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Header"
        verbose_name_plural = "Headers"

