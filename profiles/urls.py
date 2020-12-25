from django.urls import path

from . import views

app_name = 'profiles'
urlpatterns = [
    path('' , views.Profilesview.as_view() , name = 'profile_list'),
    path('<int:pk>/' , views.ProfileRetrive.as_view() , name = 'profile_retrive')
]