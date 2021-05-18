from django.urls import path
from django.urls.resolvers import URLPattern
from .views import BlogListView,BlogDetailView

urlpatterns=[
    path('',BlogListView.as_view(),name='home'),
    path('post/<int:pk>/',BlogDetailView.as_view(),name = 'post_detail'),
]