
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('product/<str:pk>/',views.showProduct,name='product'),
    path('trackproducts/',views.tracking,name='track'),

    path('register/',views.register,name='register'),
    path('login/',views.loginUser,name='login'),
    path('logout/',views.LogoutUser,name='logout')



]
