from django.urls import path, include
from textbox.views import index

urlpatterns = [
    path('', index, name="textbox"),
]