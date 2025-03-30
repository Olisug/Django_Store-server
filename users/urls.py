from django.urls import path
from django.contrib.auth import views
from users import views as v
from .views import CustomLoginView, CustomLogoutView

app_name = 'users'

urlpatterns = [
    path('registration/', v.registration, name='registration'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('profile/change_password',
         views.PasswordChangeView.as_view(),
         name='password_change'),
    path('email/', v.contact_view, name='send_email_to_tp'),
    path('success/', v.success_view, name='success'),
    ]
