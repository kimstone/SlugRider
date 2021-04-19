from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name="home"),
    path('registration-success', views.registration_success_view, name="registered"),
    path('credits', views.credits_view, name="credits"),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('riders', views.riders_view, name="riders"),
    path('register', views.create_user_view, name="register"),
    path('profile', views.edit_profile_view, name="profile"),
    path('new-user', views.new_user_form_view, name="new-user"),
    path('logmein', views.login_form_view, name="logmein"),
    path('delete/<int:rider_id>', views.delete_rider_view, name="delete"),
    path('update/<int:rider_id>', views.modify_profile_view, name="update"),
    path('edit/<int:rider_id>', views.edit_profile_view, name="edit"),
    path('view/<int:rider_id>', views.view_profile_view, name="view"),
    path('message', views.show_message_view, name="message"),
]