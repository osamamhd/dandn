from django.shortcuts import render
from django.views import generic
from main.models import Story
from django.urls import reverse

# imports for api endpoints
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import StorySerializer
from django.http import Http404
from rest_framework import status


class StoryListView(generic.ListView):
    model = Story
    template_name = 'story_list.html' 

class StoryCreateView(generic.CreateView):
    model = Story
    fields = ['title', 'body', 'type_of_story']
    template_name = 'story_create.html'

    def get_success_url(self):
        return reverse('story_list')

class  StoryDetailView(generic.DetailView):
    model = Story
    template_name = 'story_detail.html'


"""
    GET  ===>>> 'stories/api/list'
    POST ===>>> 'stories/api/list'
"""
class StoryList(APIView):
    def get(self, request, format=None):
        stories = Story.objects.all()
        serilizer = StorySerializer(stories, many=True)
        return Response(serilizer.data)

    def post(self, request, format=None):
        serializer = StorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)