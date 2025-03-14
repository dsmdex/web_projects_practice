from django.urls import path
from . import views

urlpatterns = [
    path('', views.fortune_view, name="randomfortune"),
    path('test/', views.test_view, name='test'),
    path('test_two/', views.test_two_view, name="test_two")
]