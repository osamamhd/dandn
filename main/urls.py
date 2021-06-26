from django.urls import path

from main import views
urlpatterns = [
    path('', views.StoryListView.as_view(), name='story_list'),
    path('create/', views.StoryCreateView.as_view(), name='story_create'),
    path('<slug:slug>/', views.StoryDetailView.as_view(), name='story_detail'),

    # URLs for endpoints 
    path('api/list/', views.StoryList.as_view())
]