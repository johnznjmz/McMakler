from rest_framework import serializers

"""data serializer, define fields here."""

class McMacklerCharSerializer(serializers.Serializer):

    result = serializers.CharField()


class McMacklerIntSerializer(serializers.Serializer):

    result = serializers.IntegerField()

