from django.urls import path
from .views import *

urlpatterns = [
    path('', BlogListView.as_view(),  name='dashboard'),
    path('blogs/create/', CreateBlogView.as_view(), name='create_blog'),
    path('blogs/edit/list/', BlogEditListView.as_view(),  name='edit_list'),
    path('blogs/edit/<str:pk>/', UpdateBlogView.as_view(),  name='edit_post'),
    path('blogs/<str:pk>/', BlogDetailView.as_view(), name='blog_detail'),

]
