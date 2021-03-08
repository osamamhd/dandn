from django.urls import path

from main.views import StoryListView, StoryCreateView

urlpatterns = [
    path('', StoryListView.as_view(), name='story_list'),
    path('create/', StoryCreateView.as_view(), name='story_create'),
]