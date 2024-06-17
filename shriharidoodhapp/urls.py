# urls.py
from django.urls import path

from django.contrib.auth.views import LogoutView

from .views import  UserRegistrationView
from .views import  UserLoginView
from .views import  Dashboard
from .views import custom_logout
from .views import ProductAddFormView
from .views import ProductListView
from .views import Product_delete
from .views import Product_edit
from .views import create_package
from .views import PackageListView
from .views import Packagedelete
from .views import Packageedit
from .views import AddCustomerView
from .views import CustomerListView
from .views import Customerdelete
from .views import Customeredit
from .views import order_create, callback
from .views import order_createtwo
from .views import OrderListView
from .views import DailyOrderListView
from .views import Orderdelete
from .views import Orderedit
from .views import ChangeDetails
from .views import AddBoyView
from .views import BoyListView
from .views import Boydelete
from .views import Boyedit
from .views import ChangeDetailss
from .views import DelieverySetup
from .views import DelieverylistView
from .views import ScheduleDelete
from .views import ScheduleEdit
from .views import delievered
from .views import stop
from .views import resume
from .views import DelieverySetupTwo
from .views import stopforcustomer
from .views import forgot_password, reset_password,verify_otp,send_notification
from . import views










urlpatterns = [
     path('', UserRegistrationView.as_view(), name='user_register' ),
     path('login/', UserLoginView.as_view(), name='admin_login'),
     path('dashboard/', Dashboard, name='dashboard'),
     path('logout/', custom_logout, name='logout'),
     path('addproduct/', ProductAddFormView.as_view(), name='add_product'),
     path('productlist/', ProductListView, name='product_list'),
     path('productdelete/<int:pk>/delete/', Product_delete, name='product_delete'),
     path('productedit/<int:pk>/edit/', Product_edit, name='product_edit'),
     path('create_package/', create_package.as_view(), name='create_package'),
     path('packagelist/', PackageListView, name='package_list'),
     path('Packagedelete/<int:pk>/delete/', Packagedelete, name='package_delete'),
     path('Packageedit/<int:pk>/edit/', Packageedit, name='package_edit'),
     path('addcustomer/', AddCustomerView.as_view(), name='add_customer'),
     path('adddelieveryboy/', AddBoyView.as_view(), name='add_delievery_boy'),
     path('customerlist/', CustomerListView, name='customer_list'),
     path('boylist/', BoyListView, name='Boy_list'),
     path('customerdelete/<int:pk>/delete/', Customerdelete, name='customer_delete'),
     path('customeredit/<int:pk>/edit/', Customeredit, name='customer_edit'),
     path('boydelete/<int:pk>/delete/', Boydelete, name='boy_delete'),
     path('boyedit/<int:pk>/edit/', Boyedit, name='boy_edit'),
     path('changedetails/<int:pk>/edit/', ChangeDetails, name='change_details'),
     path('changedetailss/<int:pk>/edit/', ChangeDetailss, name='change_detailss'),
     path('order_create/<int:product_id>/', order_create, name='order_create'),
     path('callback/', callback, name='callback'),
     path('order/createtwo/<int:package_id>/', order_createtwo, name='order_createtwo'),
     path('orderlist/', OrderListView, name='order_list'),
     path('dailylist/', DailyOrderListView, name='daily_list'),
     path('Orderdelete/<int:pk>/delete/', Orderdelete, name='order_delete'),
     path('Orderedit/<int:pk>/edit/', Orderedit, name='order_edit'),
     path('Delieverysetup/', DelieverySetup.as_view(), name='Delievery_setup'),
     path('Delieverysetuptwo/', DelieverySetupTwo.as_view(), name='Delievery_setuptwo'),
     path('Delieverylist/', DelieverylistView, name='Delievery_list'),
     path('scheduledelete/<int:pk>/delete/', ScheduleDelete, name='schedule_delete'),
     path('scheduleedit/<int:pk>/edit/', ScheduleEdit, name='scheduleedit'),
     path('delievered/', delievered, name='delievered'),
     path('stop/', stop, name='stop'),
     path('stopforcustomer/', stopforcustomer, name='stopforcustomer'),
     path('resume/', resume, name='resume'),
     path('forgot-password/', views.forgot_password, name='forgot_password'),
     path('verify-otp/', views.verify_otp, name='verify_otp'),
     path('reset-password/', views.reset_password, name='reset_password'),
     path('send-notification/', views.send_notification, name='send_notification'),
      path('shriharidoodhapp/callback-url/', views.callback, name='callback'),
      path('shriharidoodhapp/redirect-url/', views.redirect, name='redirect'),





]

