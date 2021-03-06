from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^login/$', views.user_login, name='login'),
    url(r'^home/$',views.view_home,name='home_view'),
    url(r'^home/item/(?P<name>[-\w]+)/$',views.item_details,name='item_details'),
    url(r'^logout/$',views.user_logout,name='logout'),
    url(r'^home/itemqty/$',views.itemqty,name='itemqty'),
    url(r'^home/availableqty/$',views.availqty,name='availqty'),
    url(r'^home/placerequest/$',views.place_request,name='placerequest'),
    url(r'^home/processrequest/$',views.process_request,name='processrequest'),
    url(r'^home/generateoptions/$',views.generateoptions,name='generateoptions'),
    url(r'^home/acknowledge/$',views.acknowledge,name='acknowledge'),
    url(r'^home/historybydate/$',views.historybydate,name='historybydate'),
    url(r'^login/isadmin/$',views.isadmin,name='isadmin'),
    url(r'^myaccount/$',views.myaccount,name='myaccount'),
    url(r'^updatepersonalinfo/$',views.updatepersonalinfo,name='updatepersonalinfo'),
    url(r'^myaccount/login/$',views.user_login,name='user_login'),
    url(r'^users/$', views.users,name='users'),
    url(r'^users/adduser/$',views.adduser, name='adduser'),
    url(r'^vendor/$',views.vendor_view,name='vendor_view'),
    url(r'^vendor/addvendor/$',views.addvendor,name='addvendor'),
    url(r'^item/$',views.item_view, name='item_view'),
    url(r'^item/additem/$',views.add_item,name='add_tem'),
    url(r'^item/addvendor/$',views.addvendor,name='addvendor'),
    url(r'^item/information/$',views.getinfo,name='getinfo'),
    url(r'^item/updateitem/$',views.updateitem,name='updateitem'),
    url(r'^/accounts/login/$',views.user_login,name='login'),

    

]
