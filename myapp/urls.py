from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name="login"),
    path('home/',views.home,name="home"),
    path('show/',views.show,name='show'),
    path('delete/<int:id>',views.delete,name='delete'),
]