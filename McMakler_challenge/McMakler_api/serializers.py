from rest_framework import serializers


class McMacklerSerializer(serializers.Serializer):
    """data serializer, define fields here."""
    result = serializers.CharField()

