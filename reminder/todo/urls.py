from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskListView.as_view(), name='index'),
    path('<int:pk>/', views.TaskDetailView.as_view(), name='details'),
    path('new/', views.TaskCreateView.as_view(), name='new'),
    path('delete/<int:pk>/', views.TaskDeleteView.as_view(), name='update'),
]