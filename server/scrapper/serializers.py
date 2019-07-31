from rest_framework import serializers
import logging


class VocabularyAPISerializer(serializers.Serializer):
    main_word = serializers.CharField()
    short_description = serializers.CharField()
    long_description = serializers.CharField()
    first_definition = serializers.CharField()
    group_definition = serializers.ListField(
        child=serializers.CharField(), required=False)
