from django.urls import path
from . import views 

urlpatterns = [
    path('',views.endpoint),
    path('username/<str:username>/',views.advocate_username)
]