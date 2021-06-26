from django.urls import path

from main import views
urlpatterns = [
    path('', views.StoryListView.as_view(), name='story_list'),
    path('create/', views.StoryCreateView.as_view(), name='story_create'),
    path('<slug:slug>/', views.StoryDetailView.as_view(), name='story_detail'),

    # URLs for endpoints 
    path('api/list/dreams/', views.DreamStoryList.as_view()),
    path('api/list/nightmares/', views.NightmareStoryList.as_view()),
    path('api/<int:pk>/', views.StoryDetail.as_view()),
]