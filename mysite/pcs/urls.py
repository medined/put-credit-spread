from django.urls import path

from . import views

urlpatterns = [
    # /pcs
    path('', views.index, name='index'),
    # /pcs/4
    path('<int:pcs_id>/', views.detail, name='detail'),
]
