from django.shortcuts import render
from django.views import generic

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status, viewsets, filters

from .models import Diary
# Create your views here.


class IndexView(generic.TemplateView):
    template_name = "index.html"


class testRESTView(APIView):
    def get(self, request):
        return Response({'message', 'Hello REST'})


def diarylistview(request):
    diaries = Diary.objects.order_by('-created_at')
    return render(request, 'diary_list.html', {'diary_list': diaries})


def diarydetailview(request, pk):
    object = Diary.objects.get(pk=pk)
    return render(request, 'diary_detail.html', {'object': object})
