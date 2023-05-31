from django.urls import path

from . import views
from .views import get_post_list

urlpatterns = [
    path('', views.ListPost.as_view()),
    path('<int:pk>/', views.DetailPost.as_view()),
    path('get/', get_post_list, name='get_post_list'),
]