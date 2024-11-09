from django.urls import path 
from . import views
urlpatterns = [
    path('',views.home , name='home'),
    path('about/',views.about , name='about'),
    path('login/',views.login_ , name='login'),
    path('logout/',views.logout_ , name='logout'),
    path('register/',views.register_ , name='register'),
    path('project/<int:pk>',views.product_ , name='product'),
]

