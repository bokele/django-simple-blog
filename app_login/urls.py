from django.urls import path
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from . import views
app_name = 'app_login'

urlpatterns = [
    path('signup/', views.sing_up, name='signup'),
    path('login/', views.signin, name='signin'),
    path('logout/', views.logout_user, name='logout'),
    path('update-profile/', views.UserChangeProfile, name='update_profile'),
    path('password/', views.userPasswordChange, name='update_password'),
    path('change-profile-picture/', views.ProfilePictureChange, name='change_profile_picture'),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
