from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name="index"),
    path('credits', views.credits_view, name="credits"),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('riders', views.riders_view, name="riders"),
    path('register', views.register_view, name="register"),
    path('profile', views.edit_profile_view, name="profile"),
]