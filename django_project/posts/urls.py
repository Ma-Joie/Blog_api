from django.urls import path
from .views import PostListApiView,PostDetailApiView
urlpatterns = [
    path("" , PostListApiView.as_view() , name='posts'),
    path("<int:pk>/" , PostDetailApiView.as_view() , name='detail')
]
