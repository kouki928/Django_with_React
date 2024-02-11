from django.urls import path
from . import views

urlpatterns = [
    # admin page ------------------------------------------------------------ #
    path("staff/", views.site_management, name="topPage"),
    
    # client page ----------------------------------------------------------- #
    path('', views.index, name="index" ),
    
    # error page ------------------------------------------------------------ #
    path("403/", views.Error_403, name="403"),
]