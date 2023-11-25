from core.models import ImageBaseModel  # noqa: F401
from django.db import models


class Achievement(ImageBaseModel):
    """!
    @brief Модель достижения
    @param name Название достижения, максимальная длина - 150 символов
    @param description Описание достижения
    @param photo_album_url ссылка на фото-альбом
    @param link_to_media ссылка на СМИ
    """
    name = models.CharField(
        'название',
        max_length=150,
    )
    description = models.TextField(
        'описание',
    )
    photo_album_url = models.URLField(
        'ссылка на фото-альбом',
    )
    link_to_media = models.URLField(
        'ссылка на СМИ',
    )

    class Meta:
        verbose_name = 'достижение'
        verbose_name_plural = 'достижения'

    @staticmethod
    def get_all_objects_by_id():
        return Achievement.objects.order_by('-id')