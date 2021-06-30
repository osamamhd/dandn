from django.urls import path

from main import views
urlpatterns = [
    path('', views.StoryListView.as_view(), name='story_list'),
    path('create/', views.StoryCreateView.as_view(), name='story_create'),
    path('<slug:slug>/', views.StoryDetailView.as_view(), name='story_detail'),

    # URLs for endpoints 
    path('api/list/dreams/', views.DreamStoryList.as_view()),
    path('api/list/nightmares/', views.NightmareStoryList.as_view()),
    path('api/<slug:story_slug>/', views.StoryDetail.as_view()),
    path('api/up/<int:pk>/', views.story_upvote),
    path('api/down/<int:pk>/', views.story_downvote),
]