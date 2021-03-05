from django.urls import path

from main.views import StoryListView

urlpatterns = [
    path('', StoryListView.as_view(), name='story_list'),
]