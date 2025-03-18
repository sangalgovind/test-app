from django.urls import path
from .views import htop_view

urlpatterns = [
    path('', htop_view),  # This makes /htop/ work
]
