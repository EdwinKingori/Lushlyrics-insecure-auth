from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LogoutView
from .views import CustomLoginView

urlpatterns = [
    path("", views.default, name='default'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path("playlist/", views.playlist, name='your_playlists'),
    path("search/", views.search, name='search_page')
]
