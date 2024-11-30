from django.urls import path,include
from . import views


urlpatterns = [

    path('',views.home, name= ""),
    path('register', views.register,name = "register"),
    path('my_login', views.my_login,name = "my_login"),
    path('user_logout', views.user_logout, name = "user_logout"),
    path('api/', include('webapp.api.urls')),
    


    #crud
    path('dashboard', views.dashboard,name = "dashboard"),
    path('home',views.home,name = "home"),
    path('create-record/', views.create_record,name = "create-record"),
    path('update-record/<int:pk>', views.update_record, name = "update_record"),
    path('view-record/<int:pk>',views.singular_record,name = "view-record"),
    path('delete-record/<int:pk>',views.delete_record,name = "delete_record"),



]


