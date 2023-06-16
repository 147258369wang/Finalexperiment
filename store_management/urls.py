"""store_management URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from store_management import view_user_owner
from store_management import view_cargo, view_in_store, view_order, view_out_store, view_store, view_user, views
from django.urls import path

urlpatterns = [
    #页面请求
    path('login/', views.login),
    path('admin/', views.admin_store),
    path('admin_store/', views.admin_store),
    path('admin_in_store/', views.admin_in_store),
    path('admin_out_store/', views.admin_out_store),
    path('admin_user/', views.admin_user),

    path('user_owner/', views.user_owner_cargo),
    path('user_owner_cargo/', views.user_owner_cargo),
    path('user_owner_user/', views.user_owner_user),
    path('user_owner_in_store/', views.user_owner_in_store),
    path('user_owner_out_store/', views.user_owner_out_store),

    path('user_buyer/', views.user_buyer_cargo),
    path('user_buyer_cargo/', views.user_buyer_cargo),
    path('user_buyer_order/', views.user_buyer_order),
    path('user_buyer_user/', views.user_buyer_user),

    #数据请求

    #用户
    path('userLogin', view_user.userLogin, name='userLogin'),
    path('userRegister', view_user.userRegister, name='userRegister'),
    path('userEdit', view_user.userEdit, name='userEdit'),
    path('userList', view_user.userList, name='userList'),

    #仓库
    path('storeList', view_store.storeList, name='storeList'),
    path('storeAdd', view_store.storeAdd, name='storeAdd'),

    #货物
    path('cargoAdd', view_cargo.cargoAdd, name='cargoAdd'),
    path('cargoList', view_cargo.cargoList, name='cargoList'),
    path('cargoNumAdd', view_cargo.cargoNumAdd, name='cargoNumAdd'),

    #入库记录
    path('in_storeList', view_in_store.in_storeList, name='in_storeList'),

    #出库记录
    path('out_storeList', view_out_store.out_storeList, name='out_storeList'),

    #采购订单
    path('orderAdd', view_order.orderAdd, name='orderAdd'),
    path('orderList', view_order.orderList, name='orderList'),

]
