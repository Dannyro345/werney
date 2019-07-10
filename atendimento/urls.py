from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('atendimento/', views.user_list),
    path('user/delete/<int:user_id>/', views.user_delete),
]