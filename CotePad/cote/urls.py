from django.contrib import admin
from django.urls import path, include

from cote.views import CoteDetailView, CoteListView, CoteCreateView, CoteDeleteView, CoteUpdateView

urlpatterns = [

    # Admin
     path('admin/', admin.site.urls),
    

    # Note
    path('',                    CoteListView.as_view(), name='cote_list'),
    path('<int:pk>',            CoteDetailView.as_view(), name='cote_detail'),
    path('add',                 CoteCreateView.as_view(), name='cote_add'),
    path('<int:pk>/',           CoteUpdateView.as_view(), name='cote_edit'),
    path('<int:pk>/delete',     CoteDeleteView.as_view(), name='cote_delete'),
    path('accounts/', include('django.contrib.auth.urls')),
]