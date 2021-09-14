from django.urls import path

from . import views

urlpatterns = [
    path('get-stats/', views.McMacklerView.as_view()),
]