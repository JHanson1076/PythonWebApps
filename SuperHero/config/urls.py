from django.contrib import admin
from django.urls import path, include

from hero.views import SuperHeroDetailView, SuperHeroListView, SuperHeroCreateView, SuperHeroDeleteView, SuperHeroUpdateView

urlpatterns = [

    # Admin
     path('admin/', admin.site.urls),
    

    # Note
    path('',                    SuperHeroListView.as_view(), name='hero_list'),
    path('<int:pk>',            SuperHeroDetailView.as_view(), name='hero_detail'),
    path('add',                 SuperHeroCreateView.as_view(), name='hero_add'),
    path('<int:pk>/',           SuperHeroUpdateView.as_view(), name='hero_edit'),
    path('<int:pk>/delete',     SuperHeroDeleteView.as_view(), name='hero_delete'),
    path('accounts/', include('django.contrib.auth.urls')),
]

