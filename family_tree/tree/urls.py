from django.urls import path

from . import views


urlpatterns = [
  path('', views.FamilyTree.as_view(), name='index'),
  path('<int:pk>/', views.Children.as_view(), name='children'),
]

