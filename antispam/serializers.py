from rest_framework import serializers

from .models import *


class AntispamDictionarySerializer(serializers.ModelSerializer):

    class Meta:
        model = AntispamDictionary
        fields = '__all__'
        read_only_fields = ('id', 'updated_at', 'created_at')


class PublicChatLogSerializer(serializers.ModelSerializer):

    class Meta:
        model = PublicChatLog
        fields = '__all__'
        read_only_fields = ('id', 'updated_at', 'created_at')
