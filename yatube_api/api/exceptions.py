from rest_framework.serializers import ValidationError


class NoSelfFollow(ValidationError):
    """Нельзя подписываться на самого себя"""
    pass
