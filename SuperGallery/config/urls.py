
from django.urls import path
from photos.views import PhotoListView, PhotoView

urlpatterns = [
    path('<str:name>', PhotoView.as_View()),
    path('', PhotoListView.as_view()),
]
