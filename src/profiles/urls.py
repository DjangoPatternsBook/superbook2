from django.urls import path
from . import views

urlpatterns = [
    path('me/', views.ShowProfile.as_view(), name='show_me'),
    path('signup/', views.SignupView.as_view(), name='sign_up'),
    path('<slug:slug>/', views.ShowProfile.as_view(),
         name='show_user'),
]
