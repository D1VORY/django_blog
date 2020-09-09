from django.urls import path
from .views import *

urlpatterns = [
    path('', BlogListView.as_view(),  name='dashboard'),
    path('blogs/<str:pk>/', BlogDetailView.as_view(), name='blog_detail'),
    #path('', index)
]
