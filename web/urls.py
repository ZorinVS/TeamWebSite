from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('solutions/', views.solutions, name='solutions'),
    path('solutions/<int:pk>/', views.solution_detail, name='solution_detail'),
    path('works/', views.works, name='works'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('contacts/', views.contacts, name='contacts'),
    path('robots.txt', views.robots, name='robots'),
]
