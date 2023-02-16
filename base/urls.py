from django.urls import path
from . import views

app_name = 'base'

urlpatterns = [
    path('', views.Register.as_view(), name='registration'),
    path('home/', views.Home.as_view(), name='home'),
    path('<int:pk>/update_profile', views.UpdateProfileView.as_view(), name='update'),
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('me/', views.ManageUsersView.as_view(), name='me')
]
