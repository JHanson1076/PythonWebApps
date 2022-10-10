from django.contrib import admin
from django.urls import path

from cote.views import CoteDetailView, CoteListView

urlpatterns = [

    # Admin
    path('admin/', admin.site.urls),

    # Note
    path('', CoteListView.as_view()),
    path('<int:pk>', CoteDetailView.as_view()),
]