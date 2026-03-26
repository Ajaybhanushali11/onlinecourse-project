from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit),
    path('result/', views.show_exam_result),
]