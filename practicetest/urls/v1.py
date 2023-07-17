from django.urls import path, include
from rest_framework import routers


urlpatterns = [
    path('fetch/questionbank', views.FetchQuestionAPIView.as_view(), name='questionbank'),
    path('bookmark/question', views.BookmarkQuestionAPIView.as_view(), name='bookmark-question'),
]