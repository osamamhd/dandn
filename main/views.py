from django.shortcuts import render
from django.views import generic
from main.models import Story

class StoryListView(generic.ListView):
    model = Story
    template_name = 'story_list.html' 