from django.urls import path
from hero.views import HulkView, Black_WidowView

urlpatterns = [
    path('',        HulkView.as_view()),
    path('black_widow',        Black_WidowView.as_view()),
]
