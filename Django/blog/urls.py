from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]