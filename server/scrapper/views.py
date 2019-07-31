from django.shortcuts import render
from rest_framework import generics, views
from rest_framework.response import Response
from .serializers import *
from .scrap import get_word_information
# Create your views here.


class WordAPIView(views.APIView):
    def get(self, request, word=None):
        info = get_word_information(word)
        results = VocabularyAPISerializer(info).data
        return Response(results)
