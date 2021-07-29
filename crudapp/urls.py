from django.urls import path
from .views import Home# new
from .views import profile_data, profile_delete, profile_create, profile_update



urlpatterns = [
    path('', Home.as_view(), name="home"), # new,
    path('profile_create/', profile_create, name='profile_create'),
    path('profile_create/', profile_create, name='profile_create'),
    path('profile_data/', profile_data, name='profile_data'),
    path('profile_update/<int:pk>', profile_update, name='profile_update'),
    path('profile_delete/<int:pk>', profile_delete, name='profile_delete')

]