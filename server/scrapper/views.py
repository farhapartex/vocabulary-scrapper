from django.shortcuts import render
from rest_framework import generics, views
from rest_framework.response import Response
from .serializers import *
from .scrap import get_word_information
# Create your views here.


class WordAPIView(views.APIView):
    results = None

    def get(self, request, word=None):
        info = get_word_information(word)
        if len(info) > 1:
            results = VocabularyAPISerializer(info).data
        else:
            results = MessageAPISerializer(info).data

        return Response(results)
