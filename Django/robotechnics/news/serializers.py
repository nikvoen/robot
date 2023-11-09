from rest_framework import serializers
from news.models import News  # noqa: F401


class NewsSerializer(serializers.ModelSerializer):
    """!
    @brief Сериализатор
    @details Нужен для преобразовывания сложных типов данных в json
    """
    class Meta:
        model = News
        fields = ['name', 'description', 'link_to_news', 'image']