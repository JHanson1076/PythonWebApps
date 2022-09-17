from django.urls import path
from hero.views import HulkView, Black_WidowView, Iron_ManView, Ghost_RiderView, Spider_ManView

urlpatterns = [
    path('',        HulkView.as_view()),
    path('black_widow',        Black_WidowView.as_view()),
    path('iron_man', Iron_ManView.as_view()),
    path('ghost_rider', Ghost_RiderView.as_view()),
    path('spider_man', Spider_ManView.as_view())
]
