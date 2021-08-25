from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), #/news
    path('<int:pk>/', views.StoryView.as_view(), name='story'), #/news/story1,2,3 etc
    path('add-story/', views.AddStoryView.as_view(),name='newStory') #/news/add-story
    path('search-stories/<str:author-name>/', views.)
]
