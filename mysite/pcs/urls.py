from django.urls import path

from pcs.views import AboutView, DetailView, IndexView
from . import views

app_name = 'pcs'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('about/', AboutView.as_view()),
    path('<int:pk>/', DetailView.as_view(), name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
]
