from django.urls import path
from .views import *

urlpatterns = [
    path('', BlogListView.as_view())
    #path('', index)
]
