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
from rest_framework import generics
from rest_framework.decorators import api_view


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
    API VIEWS
"""

"""
    GET/POST  ===>>> 'stories/api/list/dreams'
"""
class DreamStoryList(generics.ListCreateAPIView):
    queryset = Story.objects.filter(type_of_story="dream")
    serializer_class = StorySerializer


"""
    GET/POST  ===>>> 'stories/api/list/nightmares'
"""
class NightmareStoryList(generics.ListCreateAPIView):
    queryset = Story.objects.filter(type_of_story="nightmare")
    serializer_class = StorySerializer


"""
    GET  ===>>> 'stories/api/id/'
"""
class StoryDetail(APIView):

    def get_object(self, pk):
        try:
            return Story.objects.get(pk=pk)
        except Story.DoesNotExit:
            raise Http404

    def get(self, request, pk, format=None):
        story = self.get_object(pk)
        serializer = StorySerializer(story)
        return Response(serializer.data)


@api_view(['POST', ])
def story_upvote(request, pk):
    story = generics.get_object_or_404(Story, pk=pk)
    story.points += 1
    story.save()
    data = {
        'success': True
    }
    return Response(data)


@api_view(['POST', ])
def story_downvote(request, pk):
    story = generics.get_object_or_404(Story, pk=pk)
    story.points -= 1
    story.save()
    data = {
        'success': True
    }
    return Response(data)