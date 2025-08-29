import random
from django.db import models
from django.utils.translation import gettext_lazy as _


class GalleryPhoto(models.Model):
    title = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name=_("Назва")
    )
    image = models.FileField(
        null=True,
        blank=True,
        upload_to='gallery/',
        verbose_name=_("Зображення")
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Дата створення")
    )
    modified_at = models.DateTimeField(
        auto_now=True,
        verbose_name=_("Дата зміни")
    )

    class Meta:
        verbose_name = _("Фото галереї")
        verbose_name_plural = _("Фото галереї")

    def __str__(self):
        if self.title:
            return self.title
        else:
            return f'Зображення {random.randint(0, 10000)}'