from django.shortcuts import render
from django.views import generic
from main.models import Story
from django.urls import reverse

class StoryListView(generic.ListView):
    model = Story
    template_name = 'story_list.html' 

class StoryCreateView(generic.CreateView):
    model = Story
    fields = ['title', 'body', 'type_of_story']
    template_name = 'story_create.html'

    def get_success_url(self):
        return reverse('story_list')